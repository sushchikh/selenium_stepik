import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        first_name_field = browser.find_element_by_css_selector('div.first_block > div.first_class > input')
        first_name_field.send_keys('Artem')
        second_name_field = browser.find_element_by_css_selector('div.first_block > div.second_class > input')
        second_name_field.send_keys('Sushchikh')
        email_field = browser.find_element_by_css_selector('div.first_block > div.third_class > input')
        email_field.send_keys('a89638857493@gmail.com')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test_1 fail")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        first_name_field = browser.find_element_by_css_selector('div.first_block > div.first_class > input')
        first_name_field.send_keys('Ivan')
        second_name_field = browser.find_element_by_css_selector('div.first_block > div.second_class > input')
        second_name_field.send_keys('Ivanov')
        email_field = browser.find_element_by_css_selector('div.first_block > div.third_class > input')
        email_field.send_keys('super_ivan@gmail.com')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test_2 fail")


if __name__ == "__main__":
    unittest.main()