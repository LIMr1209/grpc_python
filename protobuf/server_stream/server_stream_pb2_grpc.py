# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobuf.server_stream import server_stream_pb2 as protobuf_dot_server__stream_dot_server__stream__pb2


class server_streamStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.request = channel.unary_stream(
                '/server_stream.server_stream/request',
                request_serializer=protobuf_dot_server__stream_dot_server__stream__pb2.Request.SerializeToString,
                response_deserializer=protobuf_dot_server__stream_dot_server__stream__pb2.Response.FromString,
                )


class server_streamServicer(object):
    """Missing associated documentation comment in .proto file."""

    def request(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_server_streamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'request': grpc.unary_stream_rpc_method_handler(
                    servicer.request,
                    request_deserializer=protobuf_dot_server__stream_dot_server__stream__pb2.Request.FromString,
                    response_serializer=protobuf_dot_server__stream_dot_server__stream__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'server_stream.server_stream', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class server_stream(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def request(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/server_stream.server_stream/request',
            protobuf_dot_server__stream_dot_server__stream__pb2.Request.SerializeToString,
            protobuf_dot_server__stream_dot_server__stream__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)