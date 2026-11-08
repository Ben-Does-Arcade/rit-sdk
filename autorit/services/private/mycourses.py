from autorit import PrivateService
from playwright.sync_api import expect
from time import sleep

class Client(PrivateService):
    def __init__(self) -> None:
        super().__init__(auth_callback="https://mycourses.rit.edu/d2l/lp/auth/saml/initiate-login?entityId=https://shibboleth.main.ad.rit.edu/idp/shibboleth")

    def get_homework(self) -> None:
        self.page.goto("https://mycourses.rit.edu/d2l/le/worktodo/view")
        # TODO: finish later

    def get_calendar_link(self) -> None:
        pass
        # Home page
        self.page.goto("https://mycourses.rit.edu/d2l/home")
        # Click all
        sleep(3)
        self.page.evaluate('document.querySelector("d2l-my-courses-v2").shadowRoot.querySelector("d2l-my-courses-container-v2").shadowRoot.querySelector("d2l-tabs").querySelector("#search-my-enrollments").click()')
        # Click course according to whether it starts with numbers and numbers (course code)
        
        # Click Calendar
        # Check that calendar feeds are enabled. If it is not:
        #   Click settings
        #   Click enable calendar feeds
        #   Click save
        # Click subscribe
        # Extract link
        # DONE
