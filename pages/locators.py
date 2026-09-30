# Локаторы — CSS-селекторы (строки), как и в Selenium-версии


class MainPageLocators:
    MAIN_PAGE_LINK = 'https://selenium1py.pythonanywhere.com/'
    USER_CART = ('#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > '
                 'span > a')


class LoginPageLocators:
    LOGIN_LINK = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = "#login_form"
    REGISTER_FORM = "#register_form"
    REGISTER_FORM_EMAIL = '#id_registration-email'
    REGISTER_FORM_PASSWORD = '#id_registration-password1'
    REGISTER_FORM_PASSWORD_REPEAT = '#id_registration-password2'
    REGISTER_BUTTON = '#register_form > button'
    MESSAGE_ABOUT_REGISTRATION = '#messages > div > div'


class ProductPageLocators:
    ADD_TO_CART_BUTTON = ".btn-add-to-basket"
    ITEM_ADDED_MESSAGE = '#messages > div > div > strong'
    ITEM_NAME = '.col-sm-6.product_main > h1'
    CART_WORTH = '#messages > :nth-child(3) > div > p > strong'
    ITEM_WORTH = '.col-sm-6.product_main > .price_color'


class BasePageLocators:
    LOGIN_LINK = "#login_link"
    LOGIN_LINK_INVALID = "#login_link_inc"
    USER_CART = ('#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > '
                 'span > a')
    USER_ICON = ".icon-user"


class UserCartLocators:
    CART_IS_EMPTY = '#content_inner > p'
    CART_ITEM = '#basket_formset > div'
