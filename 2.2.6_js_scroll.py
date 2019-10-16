from selenium import webdriver
from time import sleep
import math

link = 'http://suninjuly.github.io/execute_script.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    print(x)

    res = str(calc(x))

    form = browser.find_element_by_class_name('form-control')
    form.send_keys(res)

    browser.execute_script("window.scrollBy(0, 120);")
    
    robotochek = browser.find_element_by_id('robotCheckbox')
    robotochek.click()

    robotoradio = browser.find_element_by_id('robotsRule')
    robotoradio.click()

    button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    sleep(5)
    browser.close()