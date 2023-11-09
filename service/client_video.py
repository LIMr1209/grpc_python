# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protobuf/client_video/client_video.proto
import pathlib

import grpc
import protobuf.client_video.client_video_pb2 as pb2
import protobuf.client_video.client_video_pb2_grpc as pb2_grpc
from concurrent import futures


class Bili(pb2_grpc.client_videoServicer):
    def request(self, request_iterator, context):
        file = pathlib.Path(pathlib.Path(__file__).parent.parent, "static/output.jpg")
        with open(file, 'wb') as f:
            for i in request_iterator:
                f.write(i.data)

        print('接收完成')
        return pb2.Response(result='ok')


def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=1),  # 并发连接数
    )
    pb2_grpc.add_client_videoServicer_to_server(Bili(), grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:5000')
    print('server start..')
    grpc_server.start()

    try:
        grpc_server.wait_for_termination()
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    run()
