from concurrent import futures
import grpc
import profile_pb2
import profile_pb2_grpc

class ProfileService(profile_pb2_grpc.ProfileServiceServicer):
    def GetUserProfile(self, request, context):
        # Mock user data
        users = {
            "user1": ["AAPL", "GOOGL", "MSFT"],
            "user2": ["TSLA", "AMZN"]
        }
        stocks = users.get(request.user_id, [])
        for stock in stocks:
            yield profile_pb2.Stock(symbol=stock)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    profile_pb2_grpc.add_ProfileServiceServicer_to_server(ProfileService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
