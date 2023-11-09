import pathlib
import os

import grpc
import protobuf.client_video.client_video_pb2_grpc as pb2_grpc
import protobuf.client_video.client_video_pb2 as pb2


def test():
    file = pathlib.Path(pathlib.Path(__file__).parent.parent, "static/example.jpg")
    with open(file, 'rb') as f:
        size = os.path.getsize(file) / 1024
        n = 0
        while True:
            content = f.read(1024)
            if content:
                n = n + 1
                yield pb2.Request(data=content)
                print('传输进度:{}%'.format(round(n / size * 100, 2)))
            else:
                break



def run():
    try:
        # 执行RPC操作
        conn = grpc.insecure_channel('127.0.0.1:5000')
        client = pb2_grpc.client_videoStub(channel=conn)
        response = client.request(test(), timeout=0.01)
        print(response.result)
    except grpc.FutureTimeoutError as e:
        print(str(e))
    except Exception as e:
        print(type(e))


if __name__ == '__main__':
    run()
