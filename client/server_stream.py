import grpc
import protobuf.server_stream.server_stream_pb2_grpc as pb2_grpc
import protobuf.server_stream.server_stream_pb2 as pb2


def run():
    conn = grpc.insecure_channel('127.0.0.1:5000')
    client = pb2_grpc.server_streamStub(channel=conn)
    response = client.request(pb2.Request(
        data='fly'
    ))
    for item in response:
        print(item.result)


if __name__ == '__main__':
    run()
