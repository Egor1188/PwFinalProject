from pages.base_page import BasePage
from locators.user_cart_locators import UserCartLocators


class UserCart(BasePage):
    def should_be_empty(self):
        assert self.is_element_present(UserCartLocators.CART_IS_EMPTY), "Message about empty cart is not present"
        assert self.is_not_element_present(UserCartLocators.CART_ITEM), "Cart contains items, but should be empty"
