from module_5.pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        # arrange
        page = ProductPage(browser, link)
        page.open()

        # act
        page.add_to_basket()
        page.solve_quiz_and_get_code()

        # assert
        page.should_be_success_add_to_basket_message()

        expected_product_title = page.get_product_title()
        actual_product_title = page.get_success_add_to_basket_product_name()
        assert expected_product_title == actual_product_title, \
            f'В сообщение об успешном добавлении товара в корзину указано неверное название товара ' \
            f'"{actual_product_title}", а должно быть "{expected_product_title}"'

        page.should_be_basket_price_message()

        expected_basket_price = page.get_product_price()
        actual_basket_price = page.get_basket_total_price_from_message()
        assert expected_basket_price == actual_basket_price, \
            f'Неверная стоимость товаров в корзине после добавления очередного товара: указано ' \
            f'"{actual_basket_price}", а должно быть "{expected_basket_price}"'






