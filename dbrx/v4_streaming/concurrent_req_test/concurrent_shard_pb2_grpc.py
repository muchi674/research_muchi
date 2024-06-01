# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import concurrent_shard_pb2 as concurrent__shard__pb2


class ConcurrentShardStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Start = channel.unary_unary(
                '/ConcurrentShard/Start',
                request_serializer=concurrent__shard__pb2.TestIns.SerializeToString,
                response_deserializer=concurrent__shard__pb2.Empty.FromString,
                )


class ConcurrentShardServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConcurrentShardServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=concurrent__shard__pb2.TestIns.FromString,
                    response_serializer=concurrent__shard__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ConcurrentShard', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ConcurrentShard(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ConcurrentShard/Start',
            concurrent__shard__pb2.TestIns.SerializeToString,
            concurrent__shard__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)