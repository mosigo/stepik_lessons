import allure

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    @allure.step('Проверяем, что в корзине нет товаров')
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LIST_TITLE), \
            'В корзине есть товары, хотя их быть не должно'
