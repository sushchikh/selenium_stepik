from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/find_xpath_form"
    browser.get(link)
    # link_name = str(math.ceil(math.pow(math.pi, math.e)*10000))
    # link = browser.find_element_by_link_text(link_name)
    # link.click()
    # browser.get(link)

    input1 = browser.find_element_by_name('first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    # button = browser.find_element_by_css_selector("div:last-of-type > button:nth-child(3)")
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()





finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла