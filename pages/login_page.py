from selenium.webdriver.common.by import By

from helper.selenium_helper import Selenium_Helper


class LoginPage(Selenium_Helper):
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        Selenium_Helper.send_keys(self.username_input, username)
        Selenium_Helper.send_keys(self.password_input, password)
        Selenium_Helper.click(self.login_button)
