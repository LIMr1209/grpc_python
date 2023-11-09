from dns import resolver

import grpc
from dns.exception import DNSException

import protobuf.unary.unary_pb2_grpc as pb2_grpc
import protobuf.unary.unary_pb2 as pb2

consul_resolver = resolver.Resolver()
consul_resolver.port = 8600
consul_resolver.nameservers = ["127.0.0.1"]


def get_ip_port(server_name):
    '''查询出可用的一个ip，和端口'''
    try:
        dnsanswer = consul_resolver.resolve(f'{server_name}.service.consul', "A")
        dnsanswer_srv = consul_resolver.resolve(f"{server_name}.service.consul", "SRV")
    except DNSException:
        return None, None
    return dnsanswer[0].address, dnsanswer_srv[0].port


def run():
    ip, port = get_ip_port("unary")
    print(ip)
    print(port)
    conn = grpc.insecure_channel(f'{ip}:{port}')
    client = pb2_grpc.unaryStub(channel=conn)
    response = client.request(pb2.Request(
        name='hello fly',
        age=33
    ), )
    print(response.result)


if __name__ == '__main__':
    run()
