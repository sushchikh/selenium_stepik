import os
from selenium import webdriver
from time import sleep

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'find_elements.txt')  # добавляем к этому пути имя файла
print(file_path)

try:
    browser.get(link)
    first_name_form = browser.find_element_by_name('firstname')
    first_name_form.send_keys('SomeName')
    last_name_form = browser.find_element_by_name('lastname')
    last_name_form.send_keys('SomeLastName')
    email_form = browser.find_element_by_name('email')
    email_form.send_keys('some@mail.some')
    attach_file = browser.find_element_by_id('file')
    attach_file.send_keys(file_path)
    send_btn = browser.find_element_by_class_name('btn')
    send_btn.click()

    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))
    # element.send_keys(file_path)
finally:
    sleep(100)
    browser.close()

