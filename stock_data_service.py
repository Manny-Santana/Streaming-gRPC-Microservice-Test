import random
import time
from concurrent import futures
import grpc
import stock_pb2
import stock_pb2_grpc

class StockDataService(stock_pb2_grpc.StockDataServiceServicer):
    def GetStockPrices(self, request, context):
        # Mock real-time stock data
        while True:
            yield stock_pb2.StockUpdate(
                company=request.company,
                price=random.uniform(100, 500),
                timestamp=str(time.time())
            )
            time.sleep(1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stock_pb2_grpc.add_StockDataServiceServicer_to_server(StockDataService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
