
class ContainerBuilder(object):
    """Container builder for building and pushing a Docker image."""

    def __init__(
        self,
        entry_point,
        preprocessed_entry_point,
        chief_config,
        worker_config,
        requirements_txt=None,
        destination_dir="/app/",
        docker_config=None,
        called_from_notebook=False,
    ):
        """Constructor.
        Args:
            entry_point: Optional string. File path to the python file or
                iPython notebook that contains the TensorFlow code.
                Note) This path must be in the current working directory tree.
                Example) 'train.py', 'training/mnist.py', 'mnist.ipynb'
                If `entry_point` is not provided, then
                - If you are in an iPython notebook environment, then the
                    current notebook is taken as the `entry_point`.
                - Otherwise, the current python script is taken as the
                    `entry_point`.
            preprocessed_entry_point: Optional `preprocessed_entry_point`
                file path.
            chief_config: `MachineConfig` that represents the configuration for
                the chief worker in a distribution cluster.
            worker_config: `MachineConfig` that represents the configuration
                for the workers in a distribution cluster.
            requirements_txt: Optional string. File path to requirements.txt
                file containing additionally pip dependencies, if any.
            destination_dir: Optional working directory in the Docker container
                filesystem.
            docker_config: Optional Docker configuration.
            called_from_notebook: Optional boolean which indicates whether run
                has been called in a notebook environment.
        """
        self.entry_point = entry_point
        self.preprocessed_entry_point = preprocessed_entry_point
        self.chief_config = chief_config
        self.worker_config = worker_config
        self.requirements_txt = requirements_txt
        self.destination_dir = destination_dir
        self.docker_config = docker_config
        self.called_from_notebook = called_from_notebook
        self.project_id = gcp.get_project_name()

        # Those will be populated lazily.
        self.tar_file_path = None
        self.docker_client = None
        self.tar_file_descriptor = None
        self.docker_file_descriptor = None

    def get_docker_image(
        self, max_status_check_attempts=None, delay_between_status_checks=None
    ):
        """Builds, publishes and returns a Docker image.
        Args:
            max_status_check_attempts: Maximum number of times allowed to check
                build status. Applicable only to cloud container builder.
            delay_between_status_checks: Time is seconds to wait between status
                checks.
        """
        raise NotImplementedError

    def get_generated_files(self, return_descriptors=False):
        """Get generated file paths and/or descriptors for generated files.
        Args:
            return_descriptors: Whether to return descriptors as well.
        Returns:
          Docker and tar file paths. Depending on return_descriptors, possibly
          their file descriptors as well.
        """
        if return_descriptors:
            return [
                (self.docker_file_path, self.docker_file_descriptor),
                (self.tar_file_path, self.tar_file_descriptor)
            ]
        else:
            return [self.docker_file_path, self.tar_file_path]

    def _get_tar_file_path(self):
        """Packages files into a tarball."""
        self._create_docker_file()
        file_path_map = self._get_file_path_map()

        self.tar_file_descriptor, self.tar_file_path = tempfile.mkstemp()
        with tarfile.open(self.tar_file_path, "w:gz", dereference=True) as tar:
            for source, destination in file_path_map.items():
                tar.add(source, arcname=destination)

    def _get_docker_base_image(self):
        """Returns the docker image to be used as the default base image."""
        # If in a Kaggle environment, use the `KAGGLE_DOCKER_IMAGE` as the base
        # image.
        img = os.getenv("KAGGLE_DOCKER_IMAGE")
        if img:
            return img

        tf_version = tf_utils.get_version()
        if tf_version is not None:
            # Updating the name for RC's to match with the TF generated
            # RC Docker image names.
            tf_version = tf_version.replace("-rc", "rc")
            # Get the TF Docker parent image to use based on the current
            # TF version.
            img = "tensorflow/tensorflow:{}".format(tf_version)
            if (self.chief_config.accelerator_type !=
                machine_config.AcceleratorType.NO_ACCELERATOR):
                img += "-gpu"

            # Add python 3 tag for TF version <= 2.1.0
            # https://hub.docker.com/r/tensorflow/tensorflow
            v = tf_version.split(".")
            if float(v[0] + "." + v[1]) <= 2.1:
                img += "-py3"

        # Use the latest TF docker image if a local installation is not
        # available or if the docker image corresponding to the `tf_version`
        # does not exist.
        if not (img and self._image_exists(img)):
            warnings.warn(
                "TF Cloud `run` API uses docker, with a TF parent image "
                "matching your local TF version, for containerizing your "
                "code. A TF Docker image does not exist for the TF version "
                "you are using: {}"
                "We are replacing this with the latest stable TF Docker "
                "image available: `tensorflow/tensorflow:latest`"
                "Please see "
                "https://hub.docker.com/r/tensorflow/tensorflow/ "
                "for details on the available Docker images."
                "If you are seeing any code compatibility issues because of"
                " the TF version change, please try using a custom "
                "`docker_config.parent_image` with the required "
                "TF version.".format(tf_version))
            new_img = "tensorflow/tensorflow:latest"
            if img and img.endswith("-gpu"):
                new_img += "-gpu"
            img = new_img
        return img

    def _create_docker_file(self):
        """Creates a Dockerfile."""
        if self.docker_config:
          parent_image = self.docker_config.parent_image
        else:
          parent_image = None
        if parent_image is None:
            parent_image = self._get_docker_base_image()

        lines = [
            "FROM {}".format(parent_image),
            "WORKDIR {}".format(self.destination_dir),
        ]

        if self.requirements_txt is not None:
            _, requirements_txt_name = os.path.split(self.requirements_txt)
            dst_requirements_txt = os.path.join(requirements_txt_name)
            requirements_txt_path = os.path.join(
                self.destination_dir, requirements_txt_name
            )
            lines.append(
                "COPY {requirements_txt} {requirements_txt}".format(
                    requirements_txt=requirements_txt_path)
            )
            # install pip requirements from requirements_txt if it exists.
            lines.append(
                "RUN if [ -e {requirements_txt} ]; "
                "then pip install --no-cache -r {requirements_txt}; "
                "fi".format(requirements_txt=dst_requirements_txt)
            )
        if self.entry_point is None:
            lines.append("RUN pip install tensorflow-cloud")

        if self.worker_config is not None and machine_config.is_tpu_config(
            self.worker_config
        ):
            lines.append("RUN pip install cloud-tpu-client")

        # Copies the files from the `destination_dir` in Docker daemon location
        # to the `destination_dir` in Docker container filesystem.
        lines.append("COPY {} {}".format(self.destination_dir,
                                         self.destination_dir))

        docker_entry_point = self.preprocessed_entry_point or self.entry_point
        _, docker_entry_point_file_name = os.path.split(docker_entry_point)

        # Using `ENTRYPOINT` here instead of `CMD` specifically because
        # we want to support passing user code flags.
        lines.extend(
            ['ENTRYPOINT ["python", "{}"]'.format(docker_entry_point_file_name)]
        )

        content = "\n".join(lines)
        self.docker_file_descriptor, self.docker_file_path = tempfile.mkstemp()
        with open(self.docker_file_path, "w") as f:
            f.write(content)

    def _image_exists(self, image):
        """Checks whether the image exists on dockerhub using Docker v2 api.
        Args:
            image: image to check for.
        Returns:
            True if the image is found on dockerhub.
        """
        repo_name, tag_name = image.split(":")
        r = requests.get(
            "http://hub.docker.com/v2/repositories/{}/tags/{}".format(
                repo_name, tag_name
            )
        )
        return r.ok

    def _get_file_path_map(self):
        """Maps local file paths to the Docker daemon process location.
        Dictionary mapping file paths in the local file system to the paths
        in the Docker daemon process location. The `key` or source is the path
        of the file that will be used when creating the archive. The `value`
        or destination is set as the `arcname` for the file at this time.
        When extracting files from the archive, they are extracted to the
        destination path.
        Returns:
            A file path map.
        """
        location_map = {}
        if self.entry_point is None and sys.argv[0].endswith("py"):
            self.entry_point = sys.argv[0]

        # Map entry_point directory to the dst directory.
        if not self.called_from_notebook or self.entry_point is not None:
            entry_point_dir, _ = os.path.split(self.entry_point)
            if not entry_point_dir:  # Current directory
                entry_point_dir = ""
            location_map[entry_point_dir] = self.destination_dir

        # Place preprocessed_entry_point in the dst directory.
        if self.preprocessed_entry_point is not None:
            _, preprocessed_entry_point_file_name = os.path.split(
                self.preprocessed_entry_point
            )
            location_map[self.preprocessed_entry_point] = os.path.join(
                self.destination_dir, preprocessed_entry_point_file_name
            )

        # Place requirements_txt in the dst directory.
        if self.requirements_txt is not None:
            _, requirements_txt_name = os.path.split(self.requirements_txt)
            location_map[self.requirements_txt] = os.path.join(
                self.destination_dir, requirements_txt_name
            )

        # Place Docker file in the root directory.
        location_map[self.docker_file_path] = "Dockerfile"
        return location_map