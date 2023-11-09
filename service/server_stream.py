# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protobuf/server_stream/server_stream.proto

import time
import grpc
import protobuf.server_stream.server_stream_pb2 as pb2
import protobuf.server_stream.server_stream_pb2_grpc as pb2_grpc
from concurrent import futures


class Bili(pb2_grpc.server_streamServicer):
    def request(self, request, context):
        num = 1
        while context.is_active():
            data = request.data
            if num == 5:
                break
            num += 1
            yield pb2.Response(
                result=f'send {data}'
            )


def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=1),  # 并发连接数
    )
    pb2_grpc.add_server_streamServicer_to_server(Bili(), grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:5000')
    print('server start..')
    grpc_server.start()

    try:
        grpc_server.wait_for_termination()
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    run()
