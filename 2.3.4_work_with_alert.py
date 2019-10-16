from selenium import webdriver
from time import sleep
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    first_btn = browser.find_element_by_class_name('btn')
    first_btn.click()
    sleep(1)
    allert = browser.switch_to.alert
    allert.accept()

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    answer = str(calc(x))

    input_string = browser.find_element_by_id('answer')
    input_string.send_keys(answer)

    submit_btn = browser.find_element_by_class_name('btn')
    submit_btn.click()
    sleep(1)

    allert = browser.switch_to.alert
    text_from_allert = allert.text.split(':')[1]
    allert.accept()
    print(text_from_allert)



finally:
    sleep(4)
    browser.close()