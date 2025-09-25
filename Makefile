all: protogen

protogen:
	uv run -m grpc_tools.protoc -I proto \
    --mypy_out=./typed --mypy_grpc_out=./typed \
    --python_out=./typed --grpc_python_out=./typed \
    proto/dummy.proto

	uv run -m grpc_tools.protoc -I proto \
    --pyi_out=./untyped \
    --python_out=./untyped --grpc_python_out=./untyped \
    proto/dummy.proto
