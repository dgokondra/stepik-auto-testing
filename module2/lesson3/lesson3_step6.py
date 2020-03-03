import math
from time import sleep

from selenium import webdriver


with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    button = browser.find_element_by_tag_name('button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element_by_id('input_value').text)
    y = math.log(abs(12 * math.sin(x)))

    input = browser.find_element_by_id('answer')
    input.send_keys(str(y))

    btn = browser.find_element_by_tag_name('button')
    btn.click()

    sleep(20)
