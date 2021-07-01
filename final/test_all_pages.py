import allure
import pytest

from .conftest import DefaultLinkProvider, Page
from .pages.basket_page import BasketPage
from .pages.catalogue_page import CataloguePage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


def all_pages():
    link_provider = DefaultLinkProvider()
    return [
        lambda browser: MainPage(browser, link_provider.get_link(Page.MAIN)),
        lambda browser: CataloguePage(browser, link_provider.get_link(Page.CATALOGUE)),
        lambda browser: ProductPage(browser, link_provider.get_link(Page.PRODUCT)),
        lambda browser: LoginPage(browser, link_provider.get_link(Page.LOGIN))
    ]


@allure.feature('Логин / регистрация')
@allure.story('Пользователь переходит на страницу логина')
@allure.suite('Все страницы')
@allure.sub_suite('Переход на страницу логина со всех других страниц')
@pytest.mark.guest
class TestGuestGoToLogin:

    @pytest.mark.parametrize('page_creator', all_pages())
    def test_guest_should_see_login_link(self, browser, page_creator):
        # arrange
        page = page_creator(browser)
        allure.dynamic.title(f'{page.name}. Гость должен видеть кнопку перехода на страницу логина / регистрации')
        page.open()

        # assert
        page.should_be_login_link()

    @pytest.mark.parametrize('page_creator', all_pages())
    def test_guest_can_go_to_login_page(self, browser, page_creator):
        # arrange
        page = page_creator(browser)
        allure.dynamic.title(f'{page.name}. Гость может перейти на страницу логина / регистрации')
        page.open()

        # act
        page.go_to_login_page()

        # assert
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@allure.feature('Работа с корзиной')
@allure.story('Пользователь переходит на страницу с корзиной')
@allure.suite('Все страницы')
@allure.sub_suite('Переход на страницу корзины со всех других страниц')
@pytest.mark.guest
@pytest.mark.personal_tests
class TestGuestGoToBasket:

    @pytest.mark.parametrize('page_creator', all_pages())
    def test_guest_should_see_basket_link(self, browser, page_creator):
        # arrange
        page = page_creator(browser)
        allure.dynamic.title(f'{page.name}. Гость должен видеть кнопку перехода на страницу с корзиной')
        page.open()

        # assert
        page.should_be_basket_link()

    @pytest.mark.parametrize('page_creator', all_pages())
    def test_guest_can_go_to_basket_page(self, browser, page_creator):
        # arrange
        page = page_creator(browser)
        allure.dynamic.title(f'{page.name}. Гость видит пустую корзину, потому что НЕ добавлял в неё товаров')
        page.open()

        # act
        page.go_to_basket()

        # assert
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
