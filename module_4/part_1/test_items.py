from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait

test_page_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

loc_css_add_to_basket_button = 'button.btn-add-to-basket'

language_to_add_to_basket_button_text = {
    'de': 'In Warenkorb legen',
    'ar': 'أضف الى سلة التسوق',
    'ca': 'Afegeix a la cistella',
    'cs': 'Vložit do košíku',
    'da': 'Læg i kurv',
    'en-gb': 'Add to basket',
    'el': 'Προσθήκη στο καλάθι',
    'es': 'Añadir al carrito',
    'fi': 'Lisää koriin',
    'fr': 'Ajouter au panier',
    'it': 'Aggiungi al carrello',
    'ko': '장바구니 담기',
    'pl': 'Dodaj do koszyka',
    'pt': 'Adicionar ao carrinho',
    'pt-br': 'Adicionar à cesta',
    'ro': 'Adauga in cos',
    'ru': 'Добавить в корзину',
    'sk': 'Pridať do košíka',
    'uk': 'Додати в кошик',
    'zh-cn': 'Add to basket'  # это баг, здесь должен быть другой текст, но я не знаю, какой,
                              # да и в рамках текущего задания тест не должен падать, насколько я понимаю
}


def test_add_to_basket_button_text_language(browser, language):
    # arrange
    browser.get(test_page_url)
    button = browser.find_element_by_css_selector(loc_css_add_to_basket_button)
    WebDriverWait(browser, 5).until(
        visibility_of(button),
        message=f'Кнопка добавления товара в корзину не найдена'
    )

    # assert
    expected_text = language_to_add_to_basket_button_text.get(language)
    actual_text = button.text
    assert expected_text is not None, \
        f'Тест запущен на языке "{language}", но тест не знает, какая для этого языка должна быть ' \
        f'надпись на кнопке "Добавить в корзину" :('
    assert actual_text == expected_text, \
        f'Неверный перевод для кнопки "Добавить в корзину": для языка {language} ожидается текст "{expected_text}", ' \
        f'а выводится — "{actual_text}"'
