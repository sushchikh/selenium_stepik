from selenium import webdriver
import math
from time import sleep


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser.get(link)
    first_window = browser.window_handles[0]
    current_window = browser.current_window_handle
    troll_btn = browser.find_element_by_class_name('btn')
    troll_btn.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)

    answer = calc(x)
    answer_form = browser.find_element_by_id('answer')
    answer_form.send_keys(str(answer))

    submit_btn = browser.find_element_by_class_name('btn')
    submit_btn.click()

    sleep(1)
    allert = browser.switch_to.alert
    stepic_answer = allert.text.split(':')[1]
    allert.accept()
    print(stepic_answer)
finally:
    sleep(5)
    browser.close()
    browser.switch_to.window(first_window)
    browser.close()