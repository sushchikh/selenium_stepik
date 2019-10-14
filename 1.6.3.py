from selenium import webdriver
import time

browser = webdriver.Chrome()
link = 'https://instrument.ms/?utm_source=google&utm_medium=cpc&utm_campaign=poisk-brend-kirov&utm_term=%2B%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%20%2B%D0%BA%D0%B8%D1%80%D0%BE%D0%B2%20%2B%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3&gclid=Cj0KCQjwuZDtBRDvARIsAPXFx3CvR8Gk6uyb-3BMOdj9pWh-drjfApJ96GxHyWs89Q911djf8Om9FVkaAnurEALw_wcB'
try:
    browser.get(link)
    button = browser.find_element_by_class_name('z-depth-0')
    # button = browser.find_element_by_css_selector('#nav-search-form > div > span > button')

finally:
    time.sleep(4)
    browser.quit()
