import allure

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    @allure.step('Добавляем товар в корзину')
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    @allure.step('Извлекаем название товара из описания на странице')
    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    @allure.step('Извлекаем стоимость товара из описания на странице')
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    @allure.step('Ищем плашку с сообщением об успешном добавлении товара в корзину')
    def get_success_add_to_basket_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_PRODUCT_TITLE).text

    @allure.step('Ищем плашку с сообщением о стоимости товаров в корзине')
    def get_basket_total_price_from_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE_FROM_MESSAGE).text

    @allure.step('Проверяем, что на странице отображается сообщение об успешном добавлении товара в корзину')
    def should_be_success_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), \
            'Нет сообщения об успешном добавлении товара в корзину'

    @allure.step('Проверяем, что на странице отображается сообщение о стоимости товаров в корзине')
    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_PRICE_MESSAGE), \
            'Нет сообщения с новой суммой товаров в корзине после добавления очередного товара'

    @allure.step('Проверяем, что сообщение об успешном добавлении товара в корзину НЕ отображается')
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), \
            'Выведено сообщение об успешном добавлении товара в корзину, ' \
            'хотя оно в данный момент отображаться не должно'

    @allure.step('Проверяем, что исчезло сообщение об успешном добавлении товара в корзину')
    def should_be_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), \
            'Отображается сообщение об успешном добавлении товара в корзину, ' \
            'хотя оно должно исчезнуть'
