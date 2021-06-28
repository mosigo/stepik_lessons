from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCT_LIST_TITLE = (By.CSS_SELECTOR, '#content_inner div.basket-title')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')

    SUCCESS_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert:nth-child(1)')
    SUCCESS_ADD_TO_BASKET_PRODUCT_TITLE = (By.CSS_SELECTOR, '#messages div.alert:nth-child(1) div.alertinner strong')

    BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert:nth-child(3)')
    BASKET_TOTAL_PRICE_FROM_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert:nth-child(3) div.alertinner strong')


class CataloguePageLocators:
    PAGER_STATISTICS = (By.CSS_SELECTOR, 'form.form-horizontal strong')
    PREV_BUTTON = (By.CSS_SELECTOR, 'ul.pager li.previous a')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'ul.pager li.next a')
