# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protobuf/unary/unary.proto

import time

import consul
import grpc
import protobuf.unary.unary_pb2 as pb2
import protobuf.unary.unary_pb2_grpc as pb2_grpc
from concurrent import futures


def register(server_name, ip, port):
    c = consul.Consul()  # 连接consul 服务器，默认是127.0.0.1，可用host参数指定host
    print(f"开始注册服务{server_name}")
    check = consul.Check.tcp(ip, port, "10s")  # 健康检查的ip，端口，检查时间
    c.agent.service.register(server_name, f"{server_name}-{ip}-{port}",
                             address=ip, port=port, check=check)  # 注册服务部分
    print(f"注册服务{server_name}成功")


def unregister(server_name, ip, port):
    c = consul.Consul()
    print(f"开始退出服务{server_name}")
    c.agent.service.deregister(f'{server_name}-{ip}-{port}')


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
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=1),  # 并发连接数
    )
    pb2_grpc.add_unaryServicer_to_server(Bili(), grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:5000')
    print('server start..')
    register("unary", "10.25.10.132", 5000)
    grpc_server.start()

    try:
        grpc_server.wait_for_termination()
    except KeyboardInterrupt:
        unregister("unary", "10.25.10.132", 5000)
        grpc_server.stop(0)


if __name__ == '__main__':
    run()
