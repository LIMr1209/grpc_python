# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protobuf/unary/unary.proto

import time
import grpc
import protobuf.unary.unary_pb2 as pb2
import protobuf.unary.unary_pb2_grpc as pb2_grpc
from concurrent import futures


class Bili(pb2_grpc.unaryServicer):
    def request(self, request, context):
        name = request.name
        age = request.age
        print(11111)
        time.sleep(10)
        print(22222)
        result = f'my name is {name}, i am {age} year old'
        return pb2.Response(result=result)


def run():
    # options = (('gprc.so_reuseport', 1),)
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),  # 线程并发 适合IO
        # options=options
    )
    pb2_grpc.add_unaryServicer_to_server(Bili(), grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:5000')
    print('server start..')
    grpc_server.start()

    try:
        grpc_server.wait_for_termination()
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    run()
