from datetime import datetime

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from abc import abstractmethod
from enum import Enum, auto


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nЗапускаю браузер Chrome")
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'headless-chrome':
        print("\nЗапускаю браузер Chrome c опцией headless")
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nЗапускаю браузер Firefox")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f"Браузер {browser_name} пока не поддерживается в наших тестах")

    browser.maximize_window()
    browser.implicitly_wait(5)

    yield browser

    if request.node.rep_call.failed or request.node.rep_call.skipped or request.node.rep_setup.failed:
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        attach_name = request.function.__name__ + '_' + now
        allure.attach(
            browser.get_screenshot_as_png(),
            name=attach_name,
            attachment_type=allure.attachment_type.PNG
        )

    browser.quit()


@pytest.fixture(scope="session")
def language(request):
    lang = request.config.getoption("language").lower()
    return lang


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Установите язык, который будет передан в заголовок 'accept_languages'")
    parser.addoption('--browser', action='store', default="chrome",
                     help="Выберите браузер: chrome, headless-chrome или firefox")


class Page(Enum):
    MAIN = auto()
    CATALOGUE = auto()
    PRODUCT = auto()
    PRODUCT_PROMO = auto()
    LOGIN = auto()
    BASKET = auto()


class LinkProvider:

    @abstractmethod
    def get_link(self, page):
        pass


class DefaultLinkProvider(LinkProvider):

    def __init__(self):
        self.links = {
            Page.MAIN: 'http://selenium1py.pythonanywhere.com/',
            Page.CATALOGUE: 'http://selenium1py.pythonanywhere.com/catalogue/category/books_2/',
            Page.PRODUCT: 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/',
            Page.PRODUCT_PROMO: 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/',
            Page.LOGIN: 'http://selenium1py.pythonanywhere.com/accounts/login/',
            Page.BASKET: 'http://selenium1py.pythonanywhere.com/basket/'
        }

    def get_link(self, page):
        return self.links.get(page)


@pytest.fixture(scope="session")
def link_provider():
    return DefaultLinkProvider()
