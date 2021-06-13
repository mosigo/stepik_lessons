import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def language(request):
    lang = request.config.getoption("language").lower()
    return lang


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Set language for browser header 'accept_languages'")
