import os
from selenium import webdriver
from time import sleep

link = ''
# browser = webdriver.Chrome()
try:
    # browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(''))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    print(file_path)
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))
    # element.send_keys(file_path)
finally:
    sleep(0.5)
    # browser.close()

