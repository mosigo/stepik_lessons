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
        print("\nЗапускаю браузер Chrome")
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

    # now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # browser.save_screenshot(f'screenshot-{now}.png')
    browser.quit()


@pytest.fixture(scope="function")
def language(request):
    lang = request.config.getoption("language").lower()
    return lang


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Установите язык, который будет передан в заголовок 'accept_languages'")
    parser.addoption('--browser', action='store', default="chrome",
                     help="Выберите браузер: chrome или firefox")

