from selenium import webdriver
from time import sleep
import time
import math
answer = math.log(int(time.time()))
browser = webdriver.Chrome()
link = 'https://stepik.org/lesson/236897/step/1'

browser.get(link)
browser.implicitly_wait(5)
textarea = browser.find_element_by_tag_name('textarea')
textarea.send_keys(str(answer))
btn_submit = browser.find_element_by_class_name('submit-submission')
btn_submit.click()
result_field = browser.find_element_by_tag_name('pre').text
print(result_field)
assert result_field == 'Correct!', 'correct! != correct!'
sleep(5)
browser.close()