# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protobuf/both_stream/both_stream.proto

import time
import grpc
import protobuf.both_stream.both_stream_pb2 as pb2
import protobuf.both_stream.both_stream_pb2_grpc as pb2_grpc
from concurrent import futures


class Bili(pb2_grpc.both_streamServicer):
    def request(self, request_iterator, context):
        for request in request_iterator:
            data = request.data
            yield pb2.Response(result='service send back %s' % data)
            #　context.cancel()  # 服务端主动取消连接


def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=1),  # 并发连接数
    )
    pb2_grpc.add_both_streamServicer_to_server(Bili(), grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:5000')
    print('server start..')
    grpc_server.start()

    try:
        grpc_server.wait_for_termination()
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    run()
