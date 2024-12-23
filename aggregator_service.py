from concurrent import futures
import grpc
import aggregator_pb2
import aggregator_pb2_grpc
import profile_pb2_grpc
import profile_pb2
import stock_pb2_grpc
import stock_pb2

class AggregatorService(aggregator_pb2_grpc.AggregatorServicer):
    def GetStockData(self, request, context):
        # Connect to the Profile Service
        with grpc.insecure_channel('localhost:50051') as profile_channel:
            profile_stub = profile_pb2_grpc.ProfileServiceStub(profile_channel)
            stock_list = profile_stub.GetUserProfile(profile_pb2.UserRequest(user_id=request.user_id))

            for stock in stock_list:
                # Connect to the Stock Data Service
                with grpc.insecure_channel('localhost:50052') as stock_channel:
                    stock_stub = stock_pb2_grpc.StockDataServiceStub(stock_channel)
                    stock_stream = stock_stub.GetStockPrices(stock_pb2.StockRequest(company=stock.symbol))

                    for stock_update in stock_stream:
                        yield aggregator_pb2.StockUpdate(
                            company=stock_update.company,
                            price=stock_update.price,
                            timestamp=stock_update.timestamp
                        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    aggregator_pb2_grpc.add_AggregatorServicer_to_server(AggregatorService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
