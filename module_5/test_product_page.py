import time

import allure
import pytest

from allure_commons.types import AttachmentType

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
link_with_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="


@allure.feature('Логин / регистрация')
@allure.story('Гость переходит на страницу логина / регистрации со страницы товара')
@pytest.mark.login_guest
class TestLoginButtonInProductPage:
    @allure.title('Гость должен видеть кнопку перехода на страницу логина / регистрации')
    def test_guest_should_see_login_link_on_product_page(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # assert
        page.should_be_login_link()

    @allure.title('Гость может перейти на страницу логина / регистрации')
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # assert
        login_page.should_be_login_page()


@allure.feature('Добавление товаров в корзину')
@allure.story('Гость добавляет товары в корзину')
class TestProductPage:
    @allure.title('Гость может добавить товар в корзину (проверка промо)')
    @pytest.mark.xfail
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7", "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # arrange
        full_link = link_with_promo + promo_offer
        with allure.step(f'Открываем страницу товара {full_link}'):
            page = ProductPage(browser, full_link)
            page.open()

        # act
        with allure.step("Добавляем товар в корзину"):
            page.add_to_basket()
        with allure.step("Решаем задачку и получаем код для вставки на Степик"):
            page.solve_quiz_and_get_code()

        # assert
        with allure.step("Проверяем, что видим сообщение об успешном добавлении товара"):
            page.should_be_success_add_to_basket_message()

        with allure.step("Извлекаем название товара со страницы товара, на которой находимся"):
            expected_product_title = page.get_product_title()
        with allure.step("Извлекаем название товара из сообщения об успешном добавлении"):
            actual_product_title = page.get_success_add_to_basket_product_name()
        with allure.step("Проверяем, что в сообщении об успешном добавлении товара указано верное название товара"):
            assert expected_product_title == actual_product_title, \
                f'В сообщение об успешном добавлении товара в корзину указано неверное название товара ' \
                f'"{actual_product_title}", а должно быть "{expected_product_title}"'

        with allure.step("Проверяем, что появилось сообщение о стоимости добавленных в корзину товаров"):
            page.should_be_basket_price_message()

        with allure.step("Извлекаем стоимость товара со страницы товара, на которой находимся"):
            expected_basket_price = page.get_product_price()
        with allure.step("Извлекаем стоимость товаров в корзине из сообщения о стоимости товаров в корзине"):
            actual_basket_price = page.get_basket_total_price_from_message()
        with allure.step("Проверяем, что стоимость товаров в корзине равна стоимости добавленного товара"):
            assert expected_basket_price == actual_basket_price, \
                f'Неверная стоимость товаров в корзине после добавления очередного товара: указано ' \
                f'"{actual_basket_price}", а должно быть "{expected_basket_price}"'

    @allure.title('Гость НЕ должен видеть сообщение об успешном добавлении товара в корзину')
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # act
        page.add_to_basket()
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        # assert
        page.should_not_be_success_message()

    @allure.title('Гость НЕ должен видеть сообщения об успешном добавлении товара в корзину '
                  'сразу после перехода на страницу товара')
    def test_guest_cant_see_success_message(self, browser):
        # arrange
        page = ProductPage(browser, link_with_promo)
        page.open()

        # assert
        page.should_not_be_success_message()

    @allure.title('Сообщение об успешном добавлении товара в корзину должно исчезать после добавления товара в корзину')
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # act
        page.add_to_basket()

        # assert
        page.should_be_success_message_disappear()

    @allure.title('Гость НЕ должен видеть товаров в корзине, если перешёл в неё, не добавляя перед этим товаров')
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # act
        basket_page = BasketPage(browser, browser.current_url)

        # and assert
        basket_page.should_be_empty_basket()


@allure.feature('Добавление товаров в корзину')
@allure.story('Залогиненный пользователь добавляет товары в корзину')
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, link)
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
    def test_user_cant_see_success_message(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # assert
        page.should_not_be_success_message()

    @allure.title('Залогиненный пользователь после добавления товара в корзину видит корректные сообщения '
                  'об успешности операции')
    @pytest.mark.xfail
    def test_user_can_add_product_to_basket(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # act
        page.add_to_basket()

        # assert
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
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
