from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element(By.CSS_SELECTOR, ".btn").click()
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)

button2 = browser.find_element(By.CSS_SELECTOR, ".btn").click()

time.sleep(10)
browser.quit()

