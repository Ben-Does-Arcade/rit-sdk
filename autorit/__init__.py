from playwright.sync_api import sync_playwright, expect
from time import sleep
import logging
import credentials
from autorit.common import exceptions
from sys import stdout

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(stdout)
    ]
)

class Browser:
    def __init__(self) -> None:
        expect.set_options(timeout=3000)
        browser = sync_playwright().start().chromium.launch(headless=True)
        page = browser.new_page()
        self.page = page

    def wait_for_redirect(self, selector: str) -> None:
        try:
            expect(self.page.locator(selector)).not_to_be_visible()
            logging.debug("Redirection complete")
        except TimeoutError:
            raise exceptions.DuoError("Redirection took too long")

class PublicService(Browser):
    pass

class ExternalService(Browser):
    pass

class PrivateService(Browser):
    def __init__(self, auth_callback: str) -> None:
        super().__init__()
        self.page.goto(auth_callback)
        logging.debug("Typing username")
        self.page.locator("#ritUsername").fill(credentials.username)
        logging.debug("Typing password")
        self.page.locator("#ritPassword").fill(credentials.password)
        logging.debug("Logging in")
        self.page.locator("#loginButton").click()

        try:
            duo_code = self.page.locator(".code-text").text_content()
            logging.info(f"Enter code {duo_code}")
        except TimeoutError:
            # No redirect happened, something probably went wrong
            page_error = self.page.locator("message--error")

            if page_error.visible:
                # Error is showing, report it
                logging.error(f"Site error displaying {page_error.text_content()}")
                raise exceptions.CredentialsError(page_error.text_content())

        while True:
            # Handle state changes from the card text, this is where the user is entering their code
            sleep(0.25)
            header_text = self.page.get_by_test_id("card-text").text_content()

            if header_text == "Is this your device?":
                logging.debug("Acknowledging that this device belongs to the user")
                self.page.get_by_text("Yes, this is my device").click()
            elif header_text == "Duo Push timed out":
                logging.error("Timed out")
                raise exceptions.DuoError("Timed out")
            elif header_text == "Success!":
                logging.info("Successful authentication")
                break

        # self.wait_for_redirect('[data-test="card-text"]')
        sleep(3)
