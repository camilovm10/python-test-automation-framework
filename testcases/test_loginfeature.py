import pytest

from conftest import base_url
from pages.login_page import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_login:

    def setup_class(self):
        self.driver.get(base_url)
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.login("Admin", "admin123")

    def teardown_class(self):
        self.driver.quit()