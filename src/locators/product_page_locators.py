# Locators are CSS selectors (strings), same as in the Selenium version


class ProductPageLocators:
    ADD_TO_CART_BUTTON = ".btn-add-to-basket"
    ITEM_ADDED_MESSAGE = '#messages > div > div > strong'
    ITEM_NAME = '.col-sm-6.product_main > h1'
    CART_WORTH = '#messages > :nth-child(3) > div > p > strong'
    ITEM_WORTH = '.col-sm-6.product_main > .price_color'
