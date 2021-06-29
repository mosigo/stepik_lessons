import allure

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url, 'Главная страница')

    @allure.step('Проверяем, что есть меню с навигацией по каталогу')
    def should_be_navbar(self):
        assert self.is_element_present(*MainPageLocators.NAVBAR), 'Нет навигации на главной странице'
