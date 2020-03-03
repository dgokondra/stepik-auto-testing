import math
from time import sleep

from selenium import webdriver


link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


with webdriver.Chrome() as browser:
    browser.get(link)

    x = browser.find_element_by_id('treasure').get_attribute('valuex')
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
