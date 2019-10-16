from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser.get(link)
    # находим элемент прайс по айди, и ждем в течении 13 секунд момента, пока в нем значение текста не станет
    book_btn = browser.find_element_by_id('book')
    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')  # expected_conditions (ожилаемые условия), ищем элемент по айди
    )
    book_btn.click()
    x = browser.find_element_by_id('input_value').text
    answer = calc(x)

    answer_form = browser.find_element_by_id('answer')
    answer_form.send_keys(answer)

    submit_btn = browser.find_element_by_id('solve')
    submit_btn.click()

    allert = browser.switch_to.alert
    stepic_answer = allert.text.split(':')[1]
    print(stepic_answer)
    allert.accept()
finally:
    sleep(25)
    browser.close()