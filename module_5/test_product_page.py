import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="


class TestProductPage:
    @pytest.mark.xfail
    @pytest.mark.skip
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7", "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # arrange
        page = ProductPage(browser, link + promo_offer)
        page.open()

        # act
        page.add_to_basket()
        page.solve_quiz_and_get_code()

        # assert
        page.should_be_success_add_to_basket_message()

        expected_product_title = page.get_product_title()
        actual_product_title = page.get_success_add_to_basket_product_name()
        assert expected_product_title == actual_product_title, \
            f'В сообщение об успешном добавлении товара в корзину указано неверное название товара ' \
            f'"{actual_product_title}", а должно быть "{expected_product_title}"'

        page.should_be_basket_price_message()

        expected_basket_price = page.get_product_price()
        actual_basket_price = page.get_basket_total_price_from_message()
        assert expected_basket_price == actual_basket_price, \
            f'Неверная стоимость товаров в корзине после добавления очередного товара: указано ' \
            f'"{actual_basket_price}", а должно быть "{expected_basket_price}"'

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # act
        page.add_to_basket()

        # assert
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # assert
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # act
        page.add_to_basket()

        # assert
        page.should_be_success_message_disappear()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # arrange
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()

        # assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # arrange
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()

        # act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # assert
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # arrange
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()

        # act
        basket_page = BasketPage(browser, browser.current_url)

        # and assert
        basket_page.should_be_empty_basket()



