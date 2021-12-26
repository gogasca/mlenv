"""Google Cloud Build client."""

import os
import google.auth
from google.protobuf import duration_pb2
from google.cloud.devtools import cloudbuild_v1

CONTAINER_NAME = "us-central1-docker.pkg.dev/news-ml-257304/mlenv/jupyter:v1"
_BUILD_TIMEOUT = 900


def build_steps(container_name, timeout=600):
    """Authenticates with local credentials."""
    if not container_name:
        raise ValueError("Invalid container name")
    print('Building container: {} Timeout: {} seconds'.format(container_name, timeout))
    duration = duration_pb2.Duration()
    duration.seconds = timeout
    steps = [
        {
            "name": "gcr.io/cloud-builders/docker",
            "args": [
                "build", "-t", container_name, "--file=./Dockerfile", "."],
            "timeout": duration,
        },
        {
            "name": "gcr.io/cloud-builders/docker",
            "args": [
                "push", container_name]
        },
    ]
    return steps


def get_client():
    _, project_id = google.auth.default()
    client = cloudbuild_v1.services.cloud_build.CloudBuildClient()
    return project_id, client


def build_request():
    """Create and execute a simple Google Cloud Build configuration,
    print the in-progress status and print the completed status."""

    # Authorize the client with Google defaults
    project_id, client = get_client()
    build = cloudbuild_v1.Build()
    storage_source = cloudbuild_v1.StorageSource(
        {
            "bucket": "news-ml-257304_cloudbuild",
            "object_": "source/1640509283.923616-66b513c5411242b39834793db6f5e481.tgz"
        }
    )
    # The following build steps will output "hello world"
    # For more information on build configuration, see
    # https://cloud.google.com/build/docs/configuring-builds/create-basic-configuration
    build.source = cloudbuild_v1.Source(
        {
            "storage_source": storage_source,
        }
    )
    build.steps = build_steps(container_name=CONTAINER_NAME, timeout=600)
    operation = client.create_build(project_id=project_id, build=build, timeout=_BUILD_TIMEOUT)
    # Print the in-progress operation
    print("IN PROGRESS:")
    print(operation.metadata)

    result = operation.result()
    # Print the completed status
    print("RESULT:", result.status)


def verify_file_structure():
    cwd = os.getcwd()
    print(cwd)
    print(os.listdir("."))


if __name__ == "__main__":
    verify_file_structure()
    build_request()
