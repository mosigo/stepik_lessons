import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait

test_page_url = "http://selenium1py.pythonanywhere.com/accounts/login/"

loc_css_email_input = '#id_registration-email'
loc_css_password1_input = '#id_registration-password1'
loc_css_password2_input = '#id_registration-password2'
loc_css_submit_button = 'button[name="registration_submit"]'
loc_css_success_alert = 'div.alert-success'


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


def test_registration(browser):
    # arrange
    browser.get(test_page_url)

    # act
    email_input = browser.find_element_by_css_selector(loc_css_email_input)
    WebDriverWait(browser, 5).until(
        visibility_of(email_input),
        message=f'Не найдено поле ввода для email'
    )
    # добавляем случайную строчку, чтобы email заведомо был новым, заодно используем её в пароле
    rnd_string = str(int(time.time()))
    email_input.send_keys(f'q_{rnd_string}@ya.ru')

    password = f'qq_{rnd_string}'
    browser.find_element_by_css_selector(loc_css_password1_input).send_keys(password)
    browser.find_element_by_css_selector(loc_css_password2_input).send_keys(password)
    browser.find_element_by_css_selector(loc_css_submit_button).click()

    # assert
    success_div = browser.find_elements_by_css_selector(loc_css_success_alert)
    assert len(success_div) == 1, 'Не появилась плашка с сообщением об успешной регистрации'


