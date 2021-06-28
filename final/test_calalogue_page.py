import allure
import pytest

from .pages.basket_page import BasketPage
from .pages.catalogue_page import CataloguePage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/category/books_2/"


@allure.feature('Каталог товаров')
@allure.story('Гость переходит по страницам каталога при помощи пейджера')
@allure.suite("Переходы по страницам пейждера")
@pytest.mark.guest
@pytest.mark.personal_tests
class TestCataloguePager:
    @allure.title('Гость должен осуществлять переход на вторую страницу '
                  'и видеть корректную статистику про кол-во страниц в каталоге')
    def test_go_to_the_next_page(self, browser):
        # arrange
        page = CataloguePage(browser, link)
        page.open()

        # act
        page.click_by_next_button()

        # arrange
        page.should_be_correct_pager_statistic_for_second_page()

    @allure.title('Гость переходит на вторую страницу, возращается на первую, после чего '
                  'должен видеть корректную статистику про кол-во страниц в каталоге')
    def test_go_to_the_previous_page(self, browser):
        # arrange
        page = CataloguePage(browser, link)
        page.open()
        page.click_by_next_button()

        # act
        page.click_by_previous_button()

        # arrange
        page.should_be_correct_pager_statistic_for_first_page()


@allure.feature('Логин / регистрация')
@allure.story('Гость переходит на страницу логина / регистрации со страницы каталога')
@allure.suite('Страница каталога')
@pytest.mark.guest
@pytest.mark.personal_tests
class TestLoginFromCataloguePage:
    @allure.title('Гость должен видеть кнопку перехода на страницу логина / регистрации')
    def test_guest_should_see_login_link(self, browser):
        # arrange
        page = CataloguePage(browser, link)
        page.open()

        # assert
        page.should_be_login_link()

    @allure.title('Гость может перейти на страницу логина / регистрации')
    def test_guest_can_go_to_login_page(self, browser):
        # arrange
        page = CataloguePage(browser, link)
        page.open()

        # act
        page.go_to_login_page()

        # assert
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@allure.feature('Добавление товаров в корзину')
@allure.story('Гость добавляет товары в корзину со страницы каталога')
@allure.suite('Страница каталога')
@pytest.mark.guest
@pytest.mark.personal_tests
class TestBasketFromCataloguePage:
    @allure.title('Гость НЕ должен видеть товаров в корзине, если перешёл в неё, не добавляя перед этим товаров')
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # arrange
        page = CataloguePage(browser, link)
        page.open()

        # act
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)

        # assert
        basket_page.should_be_empty_basket()
