"""GRPC server."""
from concurrent import futures
import random
import grpc

from builder_pb2 import (
    ContainerImage,
    Build,
    BuildType,
    BuildStatus,
    BuildEnvironmentResponse,
)
import builder_pb2_grpc

build_type = BuildType.BUILD_TYPE_CONTAINER
container = ContainerImage(repository="gcr.io/deeplearning-platform-release/tf-cpu", tag="latest")

build_responses = [
    Build(version=1, sha1="F49CF6381E322B147053B74E4500AF8533AC1E4C", build_type=build_type, build_status=BuildStatus.BUILD_STATUS_STARTING,
          build_information="Starting",
          log_location="gs://mlenv/logs/env1.txt", container_image=container),
    Build(version=2, sha1="BF5AFC18DFBCA6FF28E36AC47BDA8AB40D47C990", build_type=build_type, build_status=BuildStatus.BUILD_STATUS_COMPLETED,
          build_information="Finished",
          log_location="gs://mlenv/logs/env2.txt", container_image=container),
    Build(version=3, sha1="82ED488F48871082D683D733384134CCB3DB5622", build_type=build_type, build_status=BuildStatus.BUILD_STATUS_FAILURE,
          build_information="Finished",
          log_location="gs://mlenv/logs/env3.txt", container_image=container),
]


class BuildService(builder_pb2_grpc.Builder):
    def BuildEnvironment(self, request, context):
        if request.user_id != 1:
            context.abort(grpc.StatusCode.NOT_FOUND, "User not found")
        # Pick random build from build_responses
        idx = random.sample(set([0, 1, 2]), 1)
        build = build_responses[idx[0]]
        return BuildEnvironmentResponse(build=build)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    builder_pb2_grpc.add_BuilderServicer_to_server(
        BuildService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
