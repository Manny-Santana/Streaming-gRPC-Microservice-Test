from flask import Flask, Response, render_template
from flask_cors import CORS
import grpc
import aggregator_pb2
import aggregator_pb2_grpc

app = Flask(__name__)


# Allow both localhost and 127.0.0.1 as valid origins
CORS(app, origins=["http://localhost:5500", "http://127.0.0.1:5500"])

@app.route('/')
def index():
    print("hit / route")
    return render_template('index.html')

@app.route('/stream/<user_id>', methods=['GET'])
def stream(user_id):
    print("hit /stream/<user_id> route")
    print("request recieved from font end generating request to aggregator...")
    def generate():
        with grpc.insecure_channel('localhost:50053') as channel:
            print("getting stub...")
            stub = aggregator_pb2_grpc.AggregatorStub(channel)
            print("got stub...")
            for stock_update in stub.GetStockData(aggregator_pb2.ClientRequest(user_id=user_id)):
                print("got data...")
                print(stock_update)
                
                yield f"data: {stock_update.company} - ${stock_update.price:.2f} ({stock_update.timestamp})\n\n"
    return Response(generate(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
