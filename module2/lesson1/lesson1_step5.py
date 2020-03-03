import math
from time import sleep

from selenium import webdriver


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/math.html'
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(str(y))

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobtn = browser.find_element_by_id('robotsRule')
    radiobtn.click()

    btn = browser.find_element_by_tag_name('button')
    btn.click()

    sleep(5)
