from concurrent import futures
import logging

import grpc
import grpc_calls_pb2
import grpc_calls_pb2_grpc

class SumServicer(grpc_calls_pb2_grpc.SumServiceServicer):
    def Sum(self, request, context):
        return grpc_calls_pb2.SumResponse(result=request.a + request.b)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_calls_pb2_grpc.add_SumServiceServicer_to_server(
        SumServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()