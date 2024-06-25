from selene import browser, have, by
import pytest

def test_google_should_find_selene(google_search):
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_should_not_find(google_search):
    browser.element('[name="q"]').type(';ko/l.ik,gmjhndgbfvdcavzsbfxgn,vjhl.b/kn;ml/.k,jbmhvngcfbx').press_enter()
    browser.element('[id="center_col"]').should(have.text('ничего не найдено'))


def test_yandex_should_find_selene(yandex_search):
    browser.element(by.xpath("//input[@placeholder='Найдётся всё']")).type('yashaka/selene').press_enter()
    browser.element(by.xpath("//ul[@id='search-result']")).should(have.text('yashaka/selene'))

def test_duck_should_find_selene(duck_search):
    browser.element(by.xpath("//input[@placeholder='Поиск без отслеживания']")).type('yashaka/selene').press_enter()
    browser.element(by.xpath("//ol[@class='react-results--main']")).should(have.text('yashaka/selene'))

