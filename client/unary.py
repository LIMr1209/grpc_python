import os.path
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import grpc
import protobuf.unary.unary_pb2_grpc as pb2_grpc
import protobuf.unary.unary_pb2 as pb2


def run():
    conn = grpc.insecure_channel('127.0.0.1:5000')
    client = pb2_grpc.unaryStub(channel=conn)
    response = client.request(pb2.Request(
            name='hello fly',
            age=33
        ),)
    print(response.result)


if __name__ == '__main__':
    run()