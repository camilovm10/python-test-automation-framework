from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Selenium_Helper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def send_keys(self, element, keys):
        self.wait.until(expected_conditions.visibility_of(element)).send_keys(keys)

    def click(self, element):
        self.wait.until(expected_conditions.visibility_of(element)).click()
