from time import sleep
from os.path import join, dirname

from selenium import webdriver


with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)

    name = browser.find_element_by_name('firstname')
    name.send_keys('Вася')

    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Иванов')

    email = browser.find_element_by_name('email')
    email.send_keys('test@test.ru')

    filepath = join(dirname(__file__), 'empty.txt')

    file_sender = browser.find_element_by_name('file')
    file_sender.send_keys(filepath)

    btn = browser.find_element_by_tag_name('button')
    btn.click()

    sleep(8)
