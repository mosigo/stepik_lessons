import time

import allure
import pytest

from .conftest import Page
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@allure.feature('Добавление товаров в корзину')
@allure.story('Гость добавляет товары в корзину со страницы товара')
@allure.suite('Страница продукта')
@allure.sub_suite("Добавление товаровов в корзину (ПРОМО)")
@pytest.mark.guest
class TestAddProductToBasketPROMO:
    @pytest.mark.parametrize(
        'promo_offer',
        [
            "offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
            pytest.param("offer7", marks=pytest.mark.xfail(reason='Промо 7 пока не работает')),
            "offer8", "offer9"
        ])
    def test_guest_can_add_product_to_basket(self, browser, link_provider, promo_offer):
        # arrange
        allure.dynamic.title(f'Промо {promo_offer[-1]}. Гость может добавить товар в корзину')
        full_link = link_provider.get_link(Page.PRODUCT_PROMO) + '?promo=' + promo_offer
        page = ProductPage(browser, full_link)
        page.open()

        # act
        page.add_to_basket()
        page.solve_quiz_and_get_code()

        # assert
        page.should_be_success_add_to_basket_message()
        page.should_be_correct_product_title_in_success_message()
        page.should_be_basket_price_message()
        page.should_be_correct_product_price_in_basket()


@allure.feature('Добавление товаров в корзину')
@allure.story('Гость добавляет товары в корзину со страницы товара')
@allure.suite('Страница продукта')
@allure.sub_suite('Нет сообщений об успешном добавлении товара в корзину там, где их не должно быть')
@pytest.mark.guest
@pytest.mark.cur
class TestNoSuccessMessageAboutAddToBasket:
    @allure.title('Гость НЕ должен видеть сообщение об успешном добавлении товара в корзину')
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link_provider):
        # arrange
        page = ProductPage(browser, link_provider.get_link(Page.PRODUCT))
        page.open()

        # act
        page.add_to_basket()

        # assert
        page.should_not_be_success_message()

    @allure.title('Гость НЕ должен видеть сообщения об успешном добавлении товара в корзину '
                  'сразу после перехода на страницу товара')
    def test_guest_cant_see_success_message(self, browser, link_provider):
        # arrange
        page = ProductPage(browser, link_provider.get_link(Page.PRODUCT))
        page.open()

        # assert
        page.should_not_be_success_message()

    @allure.title('Сообщение об успешном добавлении товара в корзину должно исчезать '
                  'после добавления товара в корзину')
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link_provider):
        # arrange
        page = ProductPage(browser, link_provider.get_link(Page.PRODUCT))
        page.open()

        # act
        page.add_to_basket()

        # assert
        page.should_be_success_message_disappear()


@allure.suite("Страница продукта")
@allure.feature('Добавление товаров в корзину')
@allure.story('Залогиненный пользователь добавляет товары в корзину со страницы каталога')
@allure.suite('Страница продукта')
@allure.sub_suite('Залогиненный пользователь. Добавление товара в корзину')
@pytest.mark.cur
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, link_provider):
        page = ProductPage(browser, link_provider.get_link(Page.PRODUCT))
        page.open()

        # открыть страницу регистрации
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # зарегистрировать нового пользователя
        rnd_string = str(int(time.time()))
        email = f'q_{rnd_string}@ya.ru'
        password = f'qq_{rnd_string}'
        login_page.register_new_user(email, password)

        # проверить, что пользователь залогинен
        login_page.should_be_authorized_user()

    @allure.title('Залогиненный пользователь НЕ должен видеть сообщения об успешном добавлении товара в корзину '
                  'сразу после перехода на страницу товара')
    def test_user_cant_see_success_message(self, browser, link_provider):
        # arrange
        page = ProductPage(browser, link_provider.get_link(Page.PRODUCT))
        page.open()

        # assert
        page.should_not_be_success_message()

    @allure.title('Залогиненный пользователь после добавления товара в корзину видит корректные сообщения '
                  'об успешности операции')
    @pytest.mark.xfail
    def test_user_can_add_product_to_basket(self, browser, link_provider):
        # arrange
        page = ProductPage(browser, link_provider.get_link(Page.PRODUCT))
        page.open()

        # act
        page.add_to_basket()

        # assert
        page.should_be_success_add_to_basket_message()
        page.should_be_correct_product_title_in_success_message()
        page.should_be_basket_price_message()
        page.should_be_correct_product_price_in_basket()
