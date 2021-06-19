import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f"Browser {browser_name} still is not implemented")

    browser.maximize_window()
    browser.implicitly_wait(5)

    yield browser

    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    browser.save_screenshot(f'screenshot-{now}.png')
    browser.quit()


@pytest.fixture(scope="function")
def language(request):
    lang = request.config.getoption("language").lower()
    return lang


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Set language for browser header 'accept_languages'")
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

