from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1 = num1_element.text
    num2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2 = num2_element.text
    answer = (int(num1) + int(num2))
  
    print(answer)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(answer))

    button = browser.find_element(By.CSS_SELECTOR, ".btn").click()



finally:
     # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла