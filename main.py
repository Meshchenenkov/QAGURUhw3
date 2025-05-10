from selene import browser, be, have  # , _multibytecodec
import pytest
#из conftest.py подтягивается фикстура 'browser_width_height'

def test_successSearch(browser_width_height):
    browser.open('https://duckduckgo.com')
    requestText = 'yashaka/selene'
    browser.element('[name="q"]').should(be.blank).type(requestText).press_enter()
    assert browser.element('html').should(have.text('DuckDuckGo'))
    print(f'Запрос "{requestText}" найден в браузере')


def test_notSuccessSearch(browser_width_height):
    browser.open('https://duckduckgo.com')
    requestText = 'фваукффаувавфвфмсям'
    browser.element('[name="q"]').should(be.blank).type(requestText).press_enter()
    assert browser.element('html').should(have.text('ничего не найдено'))
    print(f'Запрос "{requestText}" НЕ найден в браузере') #используя старые знания автотестов передал переменную прямо в тексте
