from autorit.services.external import tripshot
from flask import Flask, request
from threading import Thread
from time import sleep
import credentials
import logging

tripshot_client = tripshot.Client(username=credentials.tripshot_username, password=credentials.tripshot_password)
logging.info("Successfully initialized TripShot Client")

app = Flask(__name__)

@app.route("/get_route_times")
def get_route_times():
    with open("")

if __name__ == "__main__":
    Thread(target=poll_routes, daemon=True).start()
    app.run(host="0.0.0.0")
