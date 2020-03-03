import math
from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver


def calc(x):
    return math.log(abs(12 * math.sin(x)))


with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)

    title = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    button = browser.find_element_by_tag_name('button')
    button.click()

    x = int(browser.find_element_by_id('input_value').text)
    y = str(calc(x))

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    solve = browser.find_element_by_id('solve')
    solve.click()

    sleep(10)
