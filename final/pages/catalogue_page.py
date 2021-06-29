import allure
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import CataloguePageLocators


class CataloguePage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url, 'Страница каталога')

    @allure.step('Получаем отображаемую информацию о кол-ве элементов в текущем разделе каталога')
    def get_actual_pager_statistic(self):
        [elem_cnt, elem_from, elem_to] = \
            self.browser.find_elements(*CataloguePageLocators.PAGER_STATISTICS)
        results_cnt = int(elem_cnt.text)
        results_from = int(elem_from.text)
        results_to = int(elem_to.text)
        return results_cnt, results_from, results_to

    @allure.step('Получаем ожидаемую информацию о кол-ве элементов для страницы {2}, если размер страницы = {1}')
    def get_expected_pager_statistic(self, page_size, page_num):
        from_num = (page_num - 1) * page_size + 1
        to_num = page_num * page_size
        print(f'from={from_num}, to={to_num}')
        return from_num, to_num

    @allure.step('Кликаем по кнопке "{2}"')
    def __click_by_button(self, locator, name_for_message):
        button = self.browser.find_element(*locator)
        WebDriverWait(self.browser, 5).until(
            visibility_of(button),
            message=f'Кнопка "{name_for_message}" не найдена на странице, '
                    f'невозможно тестировать переход по страницам каталога'
        )
        button.click()

    def click_by_next_button(self):
        self.__click_by_button(CataloguePageLocators.NEXT_BUTTON, 'вперёд')

    def click_by_previous_button(self):
        self.__click_by_button(CataloguePageLocators.PREV_BUTTON, 'назад')

    @allure.step('Проверяем, что для страницы 2 в пейджере отображается верная статистика про кол-во товаров')
    def should_be_correct_pager_statistic_for_second_page(self, default_page_size=20):
        page_num = 2
        _, actual_from, actual_to = self.get_actual_pager_statistic()
        expected_from, expected_to = self.get_expected_pager_statistic(default_page_size, page_num)
        assert actual_from == expected_from, \
            f'Неверная нумерация товаров после перехода на вторую страницу выдачи: при размере страницы ' \
            f'в {default_page_size} товаров на второй странице должны отображаться товары, начиная с ' \
            f'{expected_from}, а отображаются, начиная с {actual_from}'
        assert actual_to == expected_to, \
            f'Неверная нумерация товаров после перехода на вторую страницу выдачи: при размере страницы ' \
            f'в {default_page_size} товаров на второй странице должны отображаться товары, ' \
            f'с {expected_from} по {expected_to}, а отображаются по {actual_to}'
        with allure.step(f'Ищем кнопку "назад" после перехода на страницу {page_num}'):
            assert self.is_element_present(*CataloguePageLocators.PREV_BUTTON), \
                f'Не появилась кнопка "назад" после перехода на страницу {page_num}'

    @allure.step('Проверяем, что для страницы 1 в пейджере отображается верная статистика про кол-во товаров')
    def should_be_correct_pager_statistic_for_first_page(self, default_page_size=20):
        page_num = 1
        _, actual_from, actual_to = self.get_actual_pager_statistic()
        expected_from, expected_to = self.get_expected_pager_statistic(default_page_size, page_num)
        assert actual_from == expected_from, \
            f'Неверная нумерация товаров: ' \
            f'на странице должны отображаться товары, начиная с {expected_from}, а отображаются, ' \
            f'начиная с {actual_from}'
        assert actual_to == expected_to, \
            f'Неверная нумерация товаров: ' \
            f'при размере страницы в {default_page_size} товаров должны отображаться товары с ' \
            f'{expected_from} по {expected_to}, а отображаются по {actual_to}'
        assert self.is_not_element_present(*CataloguePageLocators.PREV_BUTTON), \
            'НЕ исчезла кнопка "назад", хотя должна была'
        assert self.is_element_present(*CataloguePageLocators.NEXT_BUTTON), \
            'Исчезла кнопка "вперёд", хотя не должна была'
