import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")

wait = WebDriverWait(driver, 30)


#Markers
@pytest.mark.regression
def test_login():
    loginLink = driver.find_element(By.LINK_TEXT, "Form Authentication")

    click(loginLink)

    usernameInput = driver.find_element(By.ID, "username")
    passwordInput = driver.find_element(By.ID, "password")

    wait.until(expected_conditions.visibility_of(usernameInput)).send_keys("tomsmith")
    wait.until(expected_conditions.visibility_of(passwordInput)).send_keys("SuperSecretPassword!")

    loginButton = driver.find_element(By.CSS_SELECTOR, "button")

    click(loginButton)

    login_succeed_msg = wait.until(expected_conditions.visibility_of(driver.find_element(By.ID, "flash")))

    assert login_succeed_msg.text == "You logged into a secure area!\n×"


def click(element: WebElement):
    wait.until(expected_conditions.visibility_of(element)).click()
