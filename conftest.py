import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nОТКРЫЛИ БРАУЗЕР")
    browser=webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    print("\nЗАКРЫЛИ БРАУЗЕР")
    browser.quit()

