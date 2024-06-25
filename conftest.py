import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def browser_options():
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'


@pytest.fixture(scope="function")
def google_search():
    browser.open('https://google.com')
    yield
    browser.quit()

@pytest.fixture(scope="function")
def yandex_search():
    browser.open('https://ya.ru/')
    yield
    browser.quit()

@pytest.fixture(scope="function")
def duck_search():
    browser.open('https://duckduckgo.com')
    yield
    browser.quit()

