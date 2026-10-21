# Locators are CSS selectors (strings), same as in the Selenium version


class BasePageLocators:
    LOGIN_LINK = "#login_link"
    LOGIN_LINK_INVALID = "#login_link_inc"
    USER_CART = ('#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > '
                 'span > a')
    USER_ICON = ".icon-user"
