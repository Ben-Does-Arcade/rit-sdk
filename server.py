from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
from json import loads

app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/get_route_times")
def get_route_times():
    with open("data.json", "r") as f:
        latest_data = f.read()

    return loads(latest_data)[request.headers["route"]]

@app.route("/get_all_route_times")
def get_all_route_times():
    with open("data.json", "r") as f:
        latest_data = f.read()

    return loads(latest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
