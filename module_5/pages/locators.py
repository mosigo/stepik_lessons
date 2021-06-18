from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a")


class BasketPageLocators:
    PRODUCT_LIST_TITLE = (By.CSS_SELECTOR, '#content_inner div.basket-title')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')

    SUCCESS_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert:nth-child(1)')
    SUCCESS_ADD_TO_BASKET_PRODUCT_TITLE = (By.CSS_SELECTOR, '#messages div.alert:nth-child(1) div.alertinner strong')

    BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert:nth-child(3)')
    BASKET_TOTAL_PRICE_FROM_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert:nth-child(3) div.alertinner strong')
