import random
import time

import grpc
import protobuf.both_stream.both_stream_pb2_grpc as pb2_grpc
import protobuf.both_stream.both_stream_pb2 as pb2


def test():
    index = 0  # 用来操作客户端主动退出
    while 1:
        time.sleep(1)
        data = str(random.random())
        if index > 4:
            break
        print(index)
        index += 1
        yield pb2.Request(data=data)


def run():
    conn = grpc.insecure_channel('127.0.0.1:5000')
    client = pb2_grpc.both_streamStub(channel=conn)
    #　conn.close() 关闭链接
    response = client.request(test())
    for item in response:
        print(item.result)


if __name__ == '__main__':
    run()
