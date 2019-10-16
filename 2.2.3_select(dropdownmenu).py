from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'
link = 'http://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()

try:
    browser.get(link)
    x_element = browser.find_element_by_id('num1')
    x = int(x_element.text)
    y_element = browser.find_element_by_id('num2')
    y = int(y_element.text)
    # print(type(x), type(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x+y))
    button = browser.find_element_by_class_name('btn')
    button.click()
    time.sleep(5)
finally:
    browser.close()