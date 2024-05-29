# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import shard_envoy_pb2 as shard__envoy__pb2


class ShardEnvoyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Start = channel.unary_unary(
                '/ShardEnvoy/Start',
                request_serializer=shard__envoy__pb2.TestIns.SerializeToString,
                response_deserializer=shard__envoy__pb2.Empty.FromString,
                )
        self.SignalReady = channel.unary_unary(
                '/ShardEnvoy/SignalReady',
                request_serializer=shard__envoy__pb2.Empty.SerializeToString,
                response_deserializer=shard__envoy__pb2.Empty.FromString,
                )
        self.Receive = channel.unary_unary(
                '/ShardEnvoy/Receive',
                request_serializer=shard__envoy__pb2.ShardOuts.SerializeToString,
                response_deserializer=shard__envoy__pb2.Empty.FromString,
                )


class ShardEnvoyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignalReady(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Receive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShardEnvoyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=shard__envoy__pb2.TestIns.FromString,
                    response_serializer=shard__envoy__pb2.Empty.SerializeToString,
            ),
            'SignalReady': grpc.unary_unary_rpc_method_handler(
                    servicer.SignalReady,
                    request_deserializer=shard__envoy__pb2.Empty.FromString,
                    response_serializer=shard__envoy__pb2.Empty.SerializeToString,
            ),
            'Receive': grpc.unary_unary_rpc_method_handler(
                    servicer.Receive,
                    request_deserializer=shard__envoy__pb2.ShardOuts.FromString,
                    response_serializer=shard__envoy__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ShardEnvoy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ShardEnvoy(object):
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
        return grpc.experimental.unary_unary(request, target, '/ShardEnvoy/Start',
            shard__envoy__pb2.TestIns.SerializeToString,
            shard__envoy__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignalReady(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ShardEnvoy/SignalReady',
            shard__envoy__pb2.Empty.SerializeToString,
            shard__envoy__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Receive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ShardEnvoy/Receive',
            shard__envoy__pb2.ShardOuts.SerializeToString,
            shard__envoy__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
