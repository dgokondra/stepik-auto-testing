import math
from time import sleep

from selenium import webdriver


def calc(x):
    return math.log(abs(12 * math.sin(x)))


with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)

    button = browser.find_element_by_tag_name('button')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(y))

    btn = browser.find_element_by_tag_name('button')
    btn.click()

    sleep(8)
