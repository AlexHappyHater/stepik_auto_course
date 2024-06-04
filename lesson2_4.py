from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    browser.execute_script("window.scrollBy(0, 800)")
    option2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
     # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла