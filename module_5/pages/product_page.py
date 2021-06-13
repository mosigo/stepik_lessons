from module_5.pages.base_page import BasePage
from module_5.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_add_to_basket_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_PRODUCT_TITLE).text

    def get_basket_total_price_from_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE_FROM_MESSAGE).text

    def should_be_success_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), \
            'Нет сообщения об успешном добавлении товара в корзину'

    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_PRICE_MESSAGE), \
            'Нет сообщения с новой суммой товаров в корзине после добавления очередного товара'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), \
            'Выведено сообщение об успешном добавлении товара в корзину, ' \
            'хотя оно в данный момент отображаться не должно'

    def should_be_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), \
            'Отображается сообщение об успешном добавлении товара в корзину, ' \
            'хотя оно должно исчезнуть'
