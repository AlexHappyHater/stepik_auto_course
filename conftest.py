import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nЗАПУСКАЕМ ХРОМ")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nЗАПУСКАЕМ ОГНЕЛИСА")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nЗАКРЫЛИ БРАУЗЕР")
    browser.quit()