from time import sleep

from selenium import webdriver


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/wait1.html")

    sleep(1)
    button = browser.find_element_by_id('verify')
    button.click()
    message = browser.find_element_by_id('verify_message')

    assert 'successful' in message.text
