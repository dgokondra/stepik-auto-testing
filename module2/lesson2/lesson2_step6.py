import math
from time import sleep

from selenium import webdriver


def calc(x):
    return math.log(abs(12 * math.sin(x)))


with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser.get(link)

    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)

    answer_input = browser.find_element_by_id('answer')
    answer_input.send_keys(str(y))

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobtn = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
    radiobtn.click()

    btn = browser.find_element_by_tag_name('button')
    btn.click()

    sleep(8)
