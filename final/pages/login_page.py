import allure
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url, 'Страница логина')

    @allure.step('Ищем кнопку "{2}"')
    def get_submit_button(self, locator, button_description):
        button = self.browser.find_element(*locator)
        WebDriverWait(self.browser, 5).until(
            visibility_of(button),
            message=f'Кнопка "{button_description}" не найдена на странице {self.browser.current_url}, '
                    f'невозможно тестировать логин пользователя'
        )
        return button

    @allure.step('Выполняем логин под пользователем с email {1} и паролем {2}')
    def login_user(self, email, password):
        button = self.get_submit_button(LoginPageLocators.LOGIN_FORM_SUBMIT_BUTTON, 'Войти')
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PASSWORD).send_keys(password)
        button.click()

    @allure.step('Регистрируем пользователя с email {1} и паролем {2}')
    def register_new_user(self, email, password):
        button = self.get_submit_button(LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON, 'Зарегистироваться')
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM).send_keys(password)
        button.click()

    @allure.step('Проверяем, что формы логина и регистрации отображаются корректно')
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step('Проверяем, что находимся на странице логина')
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
            'Текущая страница не является страницей логина'

    @allure.step('Проверяем, что отображается форма логина')
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "На странице нет формы логина"

    @allure.step('Проверяем, что отображается форма регистрации')
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "На странице нет формы регистрации"
