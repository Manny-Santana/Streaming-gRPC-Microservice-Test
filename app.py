from flask import Flask, Response, render_template
import grpc
import aggregator_pb2
import aggregator_pb2_grpc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream/<user_id>')
def stream(user_id):
    def generate():
        with grpc.insecure_channel('localhost:50053') as channel:
            stub = aggregator_pb2_grpc.AggregatorStub(channel)
            for stock_update in stub.GetStockData(aggregator_pb2.UserRequest(user_id=user_id)):
                yield f"data: {stock_update.company} - ${stock_update.price:.2f} ({stock_update.timestamp})\n\n"
    return Response(generate(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
