from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
input1.send_keys("Alexey")
input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
input2.send_keys("Repin")
input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
input3.send_keys("alexeyrepin@local.ru")
input4 = browser.find_element(By.CSS_SELECTOR, "#file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
input4.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, ".btn").click()

time.sleep(10)
browser.quit()

