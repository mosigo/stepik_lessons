import allure
import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


@allure.suite("Главная страница")
@allure.feature('Страница с корзиной')
@allure.story('Гость переходит в корзину')
class TestMainPage:
    @allure.title('Гость НЕ должен видеть товаров в корзине, если перешёл в неё с главной страницы, '
                  'не добавляя перед этим товаров')
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # arrange
        page = MainPage(browser, link)
        page.open()

        # act
        page.go_to_basket()

        # assert
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()


@allure.suite("Главная страница")
@allure.feature('Логин / регистрация')
@allure.story('Гость переходит на страницу логина / регистрации с главной страницы')
@pytest.mark.login_guest
class TestLoginFromMainPage:
    @allure.title('Гость должен видеть кнопку перехода на страницу логина / регистрации')
    def test_guest_should_see_login_link(self, browser):
        # arrange
        page = MainPage(browser, link)
        page.open()

        # assert
        page.should_be_login_link()

    @allure.title('Гость может перейти на страницу логина / регистрации')
    def test_guest_can_go_to_login_page(self, browser):
        # arrange
        page = MainPage(browser, link)
        page.open()

        # act
        page.go_to_login_page()

        # assert
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
