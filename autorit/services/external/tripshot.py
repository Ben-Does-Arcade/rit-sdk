from autorit import ExternalService
from playwright.sync_api import expect, Locator
from time import sleep
import logging

class RouteError(Exception):
    pass

class Client(ExternalService):
    def __init__(self, username: str, password: str) -> None:
        super().__init__()

        self.page.goto("https://rit.tripshot.com/g/tms/TMS.html")
        logging.debug("Typing username")
        self.page.locator('[aria-label="Username"]').fill(username)
        logging.debug("Typing username")
        self.page.locator('[aria-label="Password"]').fill(password)
        logging.debug("Logging in")
        self.page.locator('button[type="submit"]').click()

        self.wait_for_redirect('button[type="submit"]')

    def get_routes(self) -> list[str]:
        routes = []
        # self.page.locator('[aria-label="Routes"]').click()
        self.page.locator('[href^="#RoutesPlace"][aria-label="Routes"]').click()

        while len(routes) == 0:
            for route in self.page.locator('[role="listitem"]').all():
                route_content = route.text_content()
                logging.debug(f"Discovered route '{route_content}'")
                routes.append(route_content)

            sleep(0.1)

        return routes

    def get_route_stop_times(self, route: str) -> dict:
        self.page.locator('[href^="#RoutesPlace"][aria-label="Routes"]').click()
        routes_selector = '[role="list"][aria-label="Routes"]'
        expect(self.page.locator(routes_selector)).to_be_visible()
        labels = self.page.locator(f"{routes_selector} div.gwt-Label").all()

        for label in labels:
            label_text = label.text_content()
            logging.debug(f"Scanning for '{route}', found '{label_text}'")
            if route in (label_text or ""):
                logging.debug(f"Activating route '{label_text}'")
                label.click()
                sleep(0.5)

                with open("autorit/services/helpers/tripshot_get_stops.js", "r") as f:
                    js_code = f.read()

                data_out = self.page.evaluate(js_code)
                return data_out

        raise RouteError(f"Cannot find route '{route}'")
