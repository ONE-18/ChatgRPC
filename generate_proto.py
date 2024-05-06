import grpc_tools
from grpc_tools import protoc

protoc_command = [
    grpc_tools.__file__.replace("__init__.py", "protoc.exe"),
    "--proto_path=.",
    "--python_out=.",
    "--grpc_python_out=.",
    "chat.proto"
]

if __name__ == "__main__":
    protoc.main(protoc_command)