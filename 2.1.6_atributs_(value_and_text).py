from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # time.sleep(2)
    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector('label > span:nth-child(2)')
    x = int(x_element.text)
    # print(x)
    y = calc(x)
    # print(str(y))

    radio_2 = browser.find_element_by_id('peopleRule')
    raio_cheked = radio_2.get_attribute('checked')
    print(raio_cheked)
    assert raio_cheked is not None, 'не выбрано по дефолту'
    assert raio_cheked == "true", "Не выбрано по дефолту"
    # assert  raio_cheked == "some", "Alert!!!111"
    answer = browser.find_element_by_id('answer')

    answer.send_keys(y)

    chech_1 = browser.find_element_by_id('robotCheckbox')
    chech_1.click()

    radio_1 = browser.find_element_by_id('robotsRule')
    radio_1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()