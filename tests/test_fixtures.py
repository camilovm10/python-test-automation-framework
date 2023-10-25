import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# 1 key

@pytest.mark.parametrize("name", ["Juan", "Sarah"])
def test_validation(name):
    assert name == "Sarah"


# 2 or more

@pytest.mark.parametrize("name, role", [("Juan", "QA Auto"), ("Dylan", "Perez")])
def test_naming_checking(name, role):
    assert name == "Juan"
    assert role == "QA Auto"


# Other way to pass params


@pytest.fixture(scope="module", params=["www.google.com", "wwww.amazon.com"])
def param(request):
    return request.param


def test_param(param):
    assert param == "www.google.com"