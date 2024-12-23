# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import stockdata_pb2 as stockdata__pb2


class StockDataServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStockPrices = channel.unary_stream(
                '/StockDataService/GetStockPrices',
                request_serializer=stockdata__pb2.StockRequest.SerializeToString,
                response_deserializer=stockdata__pb2.StockUpdate.FromString,
                )


class StockDataServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStockPrices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StockDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStockPrices': grpc.unary_stream_rpc_method_handler(
                    servicer.GetStockPrices,
                    request_deserializer=stockdata__pb2.StockRequest.FromString,
                    response_serializer=stockdata__pb2.StockUpdate.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'StockDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StockDataService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStockPrices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/StockDataService/GetStockPrices',
            stockdata__pb2.StockRequest.SerializeToString,
            stockdata__pb2.StockUpdate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
