import allure

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url, 'Страница корзины')

    @allure.step('Проверяем, что в корзине нет товаров')
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LIST_TITLE), \
            'В корзине есть товары, хотя их быть не должно'
