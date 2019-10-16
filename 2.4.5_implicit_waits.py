from selenium import webdriver
from time import sleep

link = 'http://suninjuly.github.io/wait1.html'
browser = webdriver.Chrome()
browser.implicitly_wait(5)  # браузер будет ждать появление (прогрузку) каждого элемента 5 секунду и пытаться достучаться до него каждые 500 милисекунд
try:
    browser.get(link)
    submit_btn = browser.find_element_by_class_name('btn')
    submit_btn.click()
    check_elemetn_text = browser.find_element_by_id('verify_message').text
    print(check_elemetn_text)
finally:
    sleep(2)
    browser.close()

