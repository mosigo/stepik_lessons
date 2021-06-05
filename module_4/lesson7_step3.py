import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)

    textarea = browser.find_element_by_tag_name("textarea.ember-text-area")
    WebDriverWait(browser, 5).until(
        visibility_of(textarea),
        message=f'Не загрузилось поле ввода для ответа'
    )
    answer = str(math.log(int(time.time())))
    textarea.send_keys(answer)

    button = browser.find_element_by_css_selector("button.submit-submission")
    WebDriverWait(browser, 5).until(
        visibility_of(button),
        message=f'Кнопка "Отправить" не найдена'
    )
    button.click()

    feedback = browser.find_element_by_css_selector(".smart-hints__feedback pre.smart-hints__hint")
    WebDriverWait(browser, 5).until(
        visibility_of(feedback),
        message=f'Опциональный фидбек не появился'
    )
    feedback_message = feedback.text
    assert feedback_message == 'Correct!', \
        f'"{feedback_message}"'
