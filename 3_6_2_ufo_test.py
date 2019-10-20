import pytest
import time
import math

@pytest.mark.parametrize('ufo', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1",
                                 "236903/step/1", "236904/step/1", "236905/step/1"])
# @pytest.mark.parametrize('ufo', ["236895/step/1", "236896/step/1"])
def test_ufo(browser, ufo):
    link = f"https://stepik.org/lesson/{ufo}/"
    browser.get(link)
    browser.implicitly_wait(5)
    textarea = browser.find_element_by_tag_name('textarea')
    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))
    btn_submit = browser.find_element_by_class_name('submit-submission')
    btn_submit.click()
    result_field = browser.find_element_by_tag_name('pre').text
    print(result_field)
    assert result_field == 'Correct!', 'correct! != correct!'
