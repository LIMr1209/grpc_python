import asyncio

import grpc
import protobuf.unary.unary_pb2_grpc as pb2_grpc
import protobuf.unary.unary_pb2 as pb2


async def run():
    conn = grpc.aio.insecure_channel('127.0.0.1:5000')
    client = pb2_grpc.unaryStub(channel=conn)
    try:
        response = await client.request(pb2.Request(
                name='hello fly',
                age=33
            ),timeout=2)
    except grpc.RpcError as e:
        print(type(e))


if __name__ == '__main__':
    asyncio.run(run())