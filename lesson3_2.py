from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет ОБЯЗАТЕЛЬНЫЕ поля
        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
        input1.send_keys("Alex")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
        input2.send_keys("Repin")
        input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
        input3.send_keys("TLT")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Success")



    def test_reg2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет ОБЯЗАТЕЛЬНЫЕ поля
        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
        input1.send_keys("Alex")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
        input2.send_keys("Repin")
        input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
        input3.send_keys("TLT")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Success")


if __name__=="__main__":
    unittest.main()    