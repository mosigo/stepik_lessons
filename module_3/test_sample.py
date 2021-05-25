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

catalogue_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/"

default_page_size = 20
min_cards_cnt = default_page_size + 1

loc_css_pager_statistics = 'form.form-horizontal strong'
loc_css_prev_button = 'ul.pager li.previous a'
loc_css_next_button = 'ul.pager li.next a'


def get_pager_statistics(browser):
    [elem_cnt, elem_from, elem_to] = browser.find_elements_by_css_selector(loc_css_pager_statistics)
    results_cnt = int(elem_cnt.text)
    results_from = int(elem_from.text)
    results_to = int(elem_to.text)
    return results_cnt, results_from, results_to


def get_calculated_from_and_to_for_pager(page_size, page_num):
    from_num = (page_num - 1) * page_size + 1
    to_num = page_num * page_size
    return from_num, to_num


def test_go_to_the_next_page_and_come_back():
    failed_precondition_message = 'невозможно тестировать переход по страницам каталога'

    browser = webdriver.Chrome()
    try:
        # arrange
        browser.implicitly_wait(5)
        browser.get(catalogue_link)
        results_cnt, _, _ = get_pager_statistics(browser)

        assert results_cnt >= min_cards_cnt, f'На странице {catalogue_link} менее {min_cards_cnt} товаров, ' \
                                             f'{failed_precondition_message}'

        # act
        next_button = browser.find_element_by_css_selector(loc_css_next_button)
        assert next_button is not None, f'Кнопка "вперёд" не найдена на странице {catalogue_link}, ' \
                                        f'{failed_precondition_message}'
        next_button.click()

        # assert
        _, cur_from1, cur_to1 = get_pager_statistics(browser)
        real_from_for_page2, real_to_for_page2 = \
            get_calculated_from_and_to_for_pager(default_page_size, page_num=2)
        assert cur_from1 == real_from_for_page2, \
            f'Неверная нумерация товаров после перехода на вторую страницу выдачи: при размере страницы ' \
            f'в {default_page_size} товаров на второй странице должны отображаться товары, начиная с ' \
            f'{real_from_for_page2}, а отображаются, начиная с {cur_from1}'
        assert cur_to1 == real_to_for_page2, \
            f'Неверная нумерация товаров после перехода на вторую страницу выдачи: при размере страницы ' \
            f'в {default_page_size} товаров на второй странице должны отображаться товары, ' \
            f'с {real_from_for_page2} по {real_to_for_page2}, а отображаются по {cur_to1}'

        # act
        prev_button = browser.find_element_by_css_selector(loc_css_prev_button)
        assert prev_button is not None, f'Кнопка "назад" не найдена на странице {catalogue_link} после однократного ' \
                                        f'перехода на следующую страницу с первой страницы каталога'
        prev_button.click()

        # assert
        _, cur_from2, cur_to2 = get_pager_statistics(browser)
        real_from_for_page1, real_to_for_page1 = \
            get_calculated_from_and_to_for_pager(default_page_size, page_num=1)
        assert cur_from2 == real_from_for_page1, \
            f'Неверная нумерация товаров после перехода на вторую страницу выдачи и возврата обратно на первую: ' \
            f'на странице должны отображаться товары, начиная с {real_from_for_page1}, а отображаются, ' \
            f'начиная с {cur_from2}'
        assert cur_to2 == real_to_for_page1, \
            f'Неверная нумерация товаров после перехода на вторую страницу выдачи и возврата обратно на первую: ' \
            f'при размере страницы в {default_page_size} товаров должны отображаться товары с ' \
            f'{real_from_for_page1} по {real_to_for_page1}, а отображаются по {cur_to2}'
        prev_button = browser.find_elements_by_css_selector(loc_css_prev_button)
        assert len(prev_button) == 0, \
            'Не исчезла кнопка "назад" после перехода на вторую страницу выдачи и возврата обратно на первую'
        next_button = browser.find_elements_by_css_selector(loc_css_next_button)
        assert len(next_button) > 0, \
            'Исчезла кнопка "вперёд" после перехода на вторую страницу выдачи и возврата обратно на первую'

    finally:
        browser.quit()


if __name__ == '__main__':
    test_go_to_the_next_page_and_come_back()
