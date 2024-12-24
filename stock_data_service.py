import random
import time
from concurrent import futures
import grpc
import stockdata_pb2
import stockdata_pb2_grpc

class StockDataService(stockdata_pb2_grpc.StockDataServiceServicer):
    def GetStockPrices(self, request, context):
        print("getting stock data...")
        # Mock real-time stock data
        while True:
            print("sending stock data...")
            yield stockdata_pb2.StockUpdate(
                company=request.company,
                price=random.uniform(100, 500),
                timestamp=str(time.time())
            )
            time.sleep(1)

def serve():
    print("server instantiated.......")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stockdata_pb2_grpc.add_StockDataServiceServicer_to_server(StockDataService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    print("server is running ....")
    serve()
