# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protobuf/unary/unary.proto
import asyncio
import time
import grpc
from grpc import aio

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


async def run():
    grpc_server = aio.server(futures.ThreadPoolExecutor(max_workers=40), options=[
        ('grpc.so_reuseport', 0),
        ('grpc.max_send_message_length', 100 * 1024 * 1024),
        ('grpc.max_receive_message_length', 100 * 1024 * 1024),
        ('grpc.enable_retries', 1),
    ])
    pb2_grpc.add_unaryServicer_to_server(Bili(), grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:5000')
    print('server start..')
    await grpc_server.start()

    try:
        await grpc_server.wait_for_termination()
    except KeyboardInterrupt:
        await grpc_server.stop(0)


if __name__ == '__main__':
    asyncio.run(run())
