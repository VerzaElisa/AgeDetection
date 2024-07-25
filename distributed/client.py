from __future__ import print_function

import logging
import random

import grpc
import grpc_calls_pb2
import grpc_calls_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("server:50051") as channel:
        stub = grpc_calls_pb2_grpc.SumServiceStub(channel)
        print("-------------- Sum --------------")
        response = stub.Sum(grpc_calls_pb2.SumRequest(a=3, b=4))
    print(f"Result: {response.result}")


if __name__ == "__main__":
    logging.basicConfig()
    run()