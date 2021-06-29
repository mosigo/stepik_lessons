import allure
import pytest

from .conftest import Page
from .pages.catalogue_page import CataloguePage


@allure.feature('Каталог товаров')
@allure.story('Гость переходит по страницам каталога при помощи пейджера')
@allure.suite('Страница каталога')
@allure.sub_suite('Переходы по страницам пейждера')
@pytest.mark.guest
@pytest.mark.personal_tests
class TestCataloguePager:
    @allure.title('Гость должен осуществлять переход на вторую страницу '
                  'и видеть корректную статистику про кол-во страниц в каталоге')
    def test_go_to_the_next_page(self, browser, link_provider):
        # arrange
        page = CataloguePage(browser, link_provider.get_link(Page.CATALOGUE))
        page.open()

        # act
        page.click_by_next_button()

        # arrange
        page.should_be_correct_pager_statistic_for_second_page()

    @allure.title('Гость переходит на вторую страницу, возращается на первую, после чего '
                  'должен видеть корректную статистику про кол-во страниц в каталоге')
    def test_go_to_the_previous_page(self, browser, link_provider):
        # arrange
        page = CataloguePage(browser, link_provider.get_link(Page.CATALOGUE))
        page.open()
        page.click_by_next_button()

        # act
        page.click_by_previous_button()

        # arrange
        page.should_be_correct_pager_statistic_for_first_page()
