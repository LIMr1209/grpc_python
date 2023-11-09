# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protobuf/client_stream/client_stream.proto

import time
import grpc
import protobuf.client_stream.client_stream_pb2 as pb2
import protobuf.client_stream.client_stream_pb2_grpc as pb2_grpc
from concurrent import futures


class Bili(pb2_grpc.client_streamServicer):
    def request(self, request_iterator, context):
        index = 0  # 接收到客户端5次数据后，进行return 使得客户端断开
        for request in request_iterator:
            print(request.data)
            if index > 5:
                break
            index += 1
        return pb2.Response(result='ok')


def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=1),  # 并发连接数
    )
    pb2_grpc.add_client_streamServicer_to_server(Bili(), grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:5000')
    print('server start..')
    grpc_server.start()

    try:
        grpc_server.wait_for_termination()
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    run()
