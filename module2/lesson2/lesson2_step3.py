from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def get_number(browser, element_id):
    return int(browser.find_element_by_id(element_id).text)


def get_sum(browser):
    return sum(list(map(lambda x: get_number(browser, x), ['num1', 'num2'])))


def main():
    with webdriver.Chrome() as browser:
        link = 'http://suninjuly.github.io/selects1.html'
        browser.get(link)

        sum_of_numbers = get_sum(browser)

        select = Select(browser.find_element_by_tag_name('select'))
        select.select_by_value(f'{sum_of_numbers}')

        btn = browser.find_element_by_tag_name('button')
        btn.click()

        sleep(10)


main()
