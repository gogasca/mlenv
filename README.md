
Now, to generate Python code from the protobufs, run the following:

```commandline
python3 -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/builder.proto
```

This generates several Python files from the .proto file. Here’s a breakdown:

```commandline
    python -m grpc_tools.protoc runs the protobuf compiler, which will generate Python code from the protobuf code.
    -I ../protobufs tells the compiler where to find files that your protobuf code imports. You don’t actually use the import feature, but the -I flag is required nonetheless.
    --python_out=. --grpc_python_out=. tells the compiler where to output the Python files. As you’ll see shortly, it will generate two files, and you could put each in a separate directory with these options if you wanted to.
    ../protobufs/builder.proto is the path to the protobuf file, which will be used to generate the Python code.
```


## The RPC Client
The code that’s generated is something only a motherboard could love. That is to say, it’s not very pretty Python. This is because it’s not really meant to be read by humans. Open a Python shell to see how to interact with it:


```python
from builder_pb2 import (
    ContainerImage, 
    Environment, 
    BuildParams, 
    BuildEnvironmentRequest, 
    Scripts
 )

container = ContainerImage(repository="gcr.io/deeplearning-platform-release/tf-cpu", tag="latest")
env = Environment(id=1, name="env1", owner="gogasca", container_image=container)
scripts = Scripts(startup_script="gs://mybucket/script1.sh") 
build_params = BuildParams(scripts=scripts, max_build_timeout=90)
request = BuildEnvironmentRequest(user_id=1, environment=env, build_params=build_params)
```

Start Server

```commandline
python3 builds.py
```

Send Request

```python
import grpc
from builder_pb2_grpc import BuilderStub
channel = grpc.insecure_channel("localhost:50051")
client = BuilderStub(channel)

container = ContainerImage(repository="gcr.io/deeplearning-platform-release/tf-cpu", tag="latest")
env = Environment(id=1, name="env1", owner="gogasca", container_image=container)
scripts = Scripts(startup_script="gs://mybucket/script1.sh") 
build_params = BuildParams(scripts=scripts, max_build_timeout=90)

request = BuildEnvironmentRequest(user_id=1, environment=env, build_params=build_params)
```

Build Flow

1. User sends authenticated API request
2. Create a new Environment
3. Sends a Build request for Environment. Build request includes:
 - Container
 - requirements.txt file
 - Conda environment
