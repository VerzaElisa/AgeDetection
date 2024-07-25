#!/bin/sh

# Compila i file protobuf
python -m grpc_tools.protoc -I./protos --python_out=./ --grpc_python_out=./ ./protos/grpc_calls.proto

# Esegui il client Python
python server.py

# Mantieni il container attivo
while true; do sleep 1; done