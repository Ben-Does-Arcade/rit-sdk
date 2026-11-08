from autorit.services.external import tripshot
from time import sleep
from json import dumps
import credentials
import logging

tripshot_client = tripshot.Client(username=credentials.tripshot_username, password=credentials.tripshot_password)
logging.info("Successfully initialized TripShot Client")

def main() -> None:
    global tripshot_client

    while True:
        accumulated_data = {}

        logging.info("Polling now")
        routes = tripshot_client.get_routes()

        for route in routes:
            logging.debug(f"Getting info for route '{route}'")
            data = tripshot_client.get_route_stop_times(route)
            accumulated_data[route] = data

        with open("data.json", "w") as f:
            f.write(dumps(accumulated_data))

        logging.info("Successfully written data to file")
        sleep(10)

if __name__ == "__main__":
    main()
