import allure
import pytest

from .conftest import Page
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


@allure.feature('Каталог товаров')
@allure.story('Гость может переходить по разделам каталога')
@allure.suite('Главная страница')
@allure.sub_suite('Навигация по разделам каталога')
@pytest.mark.guest
@pytest.mark.personal_tests
class TestNavBar:
    @allure.title('Гость видит навигацию по разделам каталога')
    def test_guest_should_see_navbar(self, browser, link_provider):
        # arrange
        page = MainPage(browser, link_provider.get_link(Page.MAIN))
        page.open()

        # arrange
        page.should_be_navbar()
