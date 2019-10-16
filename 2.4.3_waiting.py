from selenium import webdriver
from time import sleep

link = 'http://suninjuly.github.io/wait1.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    sleep(5)
    submit_btn = browser.find_element_by_class_name('btn')
    submit_btn.click()
    sleep(3)
    check_elemetn_text = browser.find_element_by_id('verify_message').text
    print(check_elemetn_text)
finally:
    sleep(5)
    browser.close()

