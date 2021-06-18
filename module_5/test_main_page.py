from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # arrange
        page = MainPage(browser, link)
        page.open()

        # act
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

        # assert
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # arrange
        page = MainPage(browser, link)
        page.open()

        # assert
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # arrange
        page = MainPage(browser, link)
        page.open()

        # act
        basket_page = BasketPage(browser, browser.current_url)

        # and assert
        basket_page.should_be_empty_basket()


