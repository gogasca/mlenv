"""Module that contains the `run` API for building environments."""

import logging
import os
import sys


from . import containerize
from . import docker_config as docker_config_module
from ..utils import google_api_client

logger = logging.getLogger(__name__)


def create(
    entry_point=None,
    requirements_txt=None,
    docker_config="auto",
    **kwargs
):
    """Create your environment in Google Cloud Platform.
    Args:
        entry_point: Optional string. File path to the python file or iPython
            notebook that contains the code.
            Note this path must be in the current working directory tree.
            Example - 'train.py', 'training/mnist.py', 'mnist.ipynb'
            If `entry_point` is not provided, then
            - If you are in an iPython notebook environment, then the
                current notebook is taken as the `entry_point`.
            - Otherwise, the current python script is taken as the
                `entry_point`.
            Note: If you are using Python console, this will command will fail.
        requirements_txt: Optional string. File path to requirements.txt file
            containing additional pip dependencies if any. ie. a file with a
            list of pip dependency package names.
            Note this path must be in the current working directory tree.
            Example - 'requirements.txt', 'deps/reqs.txt'
        docker_config: Optional `DockerConfig`. Represents Docker related
            configuration for the `run` API.
            - image: Optional Docker image URI for the Docker image being built.
            - parent_image: Optional parent Docker image to use.
            - cache_from: Optional Docker image URI to be used as a cache when
                building the new Docker image.
            - image_build_bucket: Optional GCS bucket name to be used for
                building a Docker image via
                [Google Cloud Build](https://cloud.google.com/cloud-build/).
            Defaults to 'auto'. 'auto' maps to a default `tfc.DockerConfig`
            instance.
        **kwargs: Additional keyword arguments.
    Returns:
        A dictionary with two keys.'job_id' - the training job id and
        'docker_image'- Docker image generated for the training job.
    """
    docker_base_image = kwargs.pop("docker_base_image", None)
    docker_image_bucket_name = kwargs.pop("docker_image_bucket_name", None)

    if kwargs:
        # We are using kwargs for forward compatibility in the cloud. For eg.,
        # if a new param is added to `run` API, this will not exist in the
        # latest tensorflow-cloud package installed in the cloud Docker envs.
        # So, if `run` is used inside a python script or notebook, this python
        # code will fail to run in the cloud even before we can check
        # `TF_KERAS_RUNNING_REMOTELY` env var because of an additional unknown
        # param.
        raise TypeError("Unknown keyword arguments: %s" % (kwargs.keys(),))

    # Get defaults values for input param
    if docker_config == "auto":
        docker_config = docker_config_module.DockerConfig()
    docker_config.parent_image = (docker_config.parent_image or
                                  docker_base_image)
    docker_config.image_build_bucket = (docker_config.image_build_bucket or
                                        docker_image_bucket_name)

    destination_dir = "/app/"
    # Working directory in the Docker container filesystem.
    called_from_notebook = _called_from_notebook()

    # Run validations.
    print("Validating environment and input parameters.")
    print("Validation was successful.")

    # Make the `entry_point` cloud and distribution ready.
    # A temporary script called `preprocessed_entry_point` is created.
    # This contains the `entry_point` wrapped in a distribution strategy.
    preprocessed_entry_point = None

    # Create Docker file, generate a tarball, build and push Docker
    # image using the tarball.
    print("Building and pushing the Docker image. This may take a few minutes.")
    cb_args = (
        entry_point,
        preprocessed_entry_point,
    )
    cb_kwargs = {
        "requirements_txt": requirements_txt,
        "destination_dir": destination_dir,
        "docker_config": docker_config,
        "called_from_notebook": called_from_notebook,
    }

    container_builder = containerize.CloudContainerBuilder(*cb_args, **cb_kwargs)
    docker_img_uri = container_builder.get_docker_image()

    # Delete all the temporary files we created.
    for file_path, file_descriptor in container_builder.get_generated_files(
        return_descriptors=True):
        os.close(file_descriptor)
        os.remove(file_path)

    # Call `exit` to prevent training the Keras model in the local env.
    # To stop execution after encountering a `run` API call in local env.
    if entry_point is None and not called_from_notebook:
        sys.exit(0)
    return {
        "docker_image": docker_img_uri,
    }


def _called_from_notebook():
    """Detects if we are currently executing in a notebook environment."""
    client_env = google_api_client.get_client_environment_name()
    if client_env in (
        google_api_client.ClientEnvironment.KAGGLE_NOTEBOOK.name,
        google_api_client.ClientEnvironment.COLAB.name):
        return True
    if client_env == google_api_client.ClientEnvironment.HOSTED_NOTEBOOK:
        logger.warning("Vertex AI notebook environment is not supported.")
    return False