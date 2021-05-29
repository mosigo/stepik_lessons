from selenium import webdriver

# 1.1.1 Переходы по страницам каталога
# Предусловия: раздел каталога "Books" существует и доступен на сайте, в нём более 40 товаров.
#
# - 1) Открыть страницу с разделом каталога "Books": на странице оотображается кнопка "вперёд"
# для перехода на следующую страницу каталога.
# - 2) Нажать на кнопку "вперёд": под заголовком раздела указано, что отобразились результаты
# "с 21 по 40", появилась кнопка "назад" для перехода обратно на первую страницу каталога.
# - 3) Нажать на кнопку "назад": под заголовком раздела указано, что отобразились результаты
# "с 1 по 20", кнопка "назад" исчезла, кнопка "вперёд" доступна.
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait

catalogue_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/"

default_page_size = 20
min_cards_cnt = default_page_size + 1

loc_css_pager_statistics = 'form.form-horizontal strong'
loc_css_prev_button = 'ul.pager li.previous a'
loc_css_next_button = 'ul.pager li.next a'


# получает текущие значения "с" и "по" пейджера, которые в данный момент отображаются на странице
def get_actual_pager_statistic(browser):
    [elem_cnt, elem_from, elem_to] = browser.find_elements_by_css_selector(loc_css_pager_statistics)
    results_cnt = int(elem_cnt.text)
    results_from = int(elem_from.text)
    results_to = int(elem_to.text)
    return results_cnt, results_from, results_to


# вычисляет ожидаемые "с" и "по" по заданному номеру страницы и размеру страницы
def get_expected_pager_statistic(page_size, page_num):
    from_num = (page_num - 1) * page_size + 1
    to_num = page_num * page_size
    return from_num, to_num


# вспомогательная функция для перехода через клик по кнопке пейджера
def click_by_button(browser, css_locator, name_for_message):
    button = browser.find_element_by_css_selector(css_locator)
    WebDriverWait(browser, 5).until(
        visibility_of(button),
        message=f'Кнопка "{name_for_message}" не найдена на странице {catalogue_link}, '
                f'невозможно тестировать переход по страницам каталога'
    )
    button.click()


# вспомогательная функция для проверки существования и отсутствия кнопки на странице
def assert_button_exists(browser, css_locator, error_message, must_exists=True):
    button = browser.find_elements_by_css_selector(css_locator)
    if must_exists:
        assert len(button) > 0, error_message
    else:
        assert len(button) == 0, error_message


def test_go_to_the_next_page():
    browser = webdriver.Chrome()
    try:
        # arrange
        browser.implicitly_wait(5)
        browser.get(catalogue_link)

        # act
        click_by_button(browser, loc_css_next_button, 'вперёд')

        # assert
        _, actual_from, actual_to = get_actual_pager_statistic(browser)
        expected_from, expected_to = get_expected_pager_statistic(default_page_size, page_num=2)
        assert actual_from == expected_from, \
            f'Неверная нумерация товаров после перехода на вторую страницу выдачи: при размере страницы ' \
            f'в {default_page_size} товаров на второй странице должны отображаться товары, начиная с ' \
            f'{expected_from}, а отображаются, начиная с {actual_from}'
        assert actual_to == expected_to, \
            f'Неверная нумерация товаров после перехода на вторую страницу выдачи: при размере страницы ' \
            f'в {default_page_size} товаров на второй странице должны отображаться товары, ' \
            f'с {expected_from} по {expected_to}, а отображаются по {actual_to}'
        assert_button_exists(browser, loc_css_prev_button,
                             'Не появилась кнопка "назад" после перехода на вторую страницу выдачи', must_exists=True)

    finally:
        browser.quit()


def test_go_to_the_previous_page():
    browser = webdriver.Chrome()
    try:
        # arrange
        browser.implicitly_wait(5)
        browser.get(catalogue_link)
        click_by_button(browser, loc_css_next_button, 'вперёд')

        # act
        click_by_button(browser, loc_css_prev_button, 'назад')

        # assert
        _, actual_from, actual_to = get_actual_pager_statistic(browser)
        expected_from, expected_to = get_expected_pager_statistic(default_page_size, page_num=1)
        assert actual_from == expected_from, \
            f'Неверная нумерация товаров после перехода на вторую страницу выдачи и возврата обратно на первую: ' \
            f'на странице должны отображаться товары, начиная с {expected_from}, а отображаются, ' \
            f'начиная с {actual_from}'
        assert actual_to == expected_to, \
            f'Неверная нумерация товаров после перехода на вторую страницу выдачи и возврата обратно на первую: ' \
            f'при размере страницы в {default_page_size} товаров должны отображаться товары с ' \
            f'{expected_from} по {expected_to}, а отображаются по {actual_to}'
        assert_button_exists(browser, loc_css_prev_button,
                             'Не исчезла кнопка "назад" после перехода на вторую страницу выдачи '
                             'и возврата обратно на первую', must_exists=False)
        assert_button_exists(browser, loc_css_next_button,
                             'Исчезла кнопка "вперёд" после перехода на вторую страницу выдачи '
                             'и возврата обратно на первую', must_exists=True)

    finally:
        browser.quit()


if __name__ == '__main__':
    test_go_to_the_next_page()
    test_go_to_the_previous_page()
