import math

from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators
from loguru import logger


class ProductPage(BasePage):
    def __init__(self, page, url, timeout=10):
        super().__init__(page, url, timeout)
        self.quiz_code = None
        self._dialogs_handled = 0
        # In Playwright dialogs (alert/prompt) are dismissed automatically by default,
        # so the handler is attached in advance, before the click that triggers the dialog
        self.page.on("dialog", self._handle_dialog)

    def _handle_dialog(self, dialog):
        if dialog.type == "prompt":
            x = dialog.message.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            logger.info('Prompt: {!r}, answer: {}', dialog.message, answer)
            dialog.accept(answer)
        else:
            self.quiz_code = dialog.message
            logger.info("Your code: {}", dialog.message)
            dialog.accept()
        self._dialogs_handled += 1

    def add_to_cart(self):
        logger.info('Adding the product to the cart')
        self.page.locator(ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def solve_quiz_and_get_code(self):
        # The handler solves the dialogs; here we wait for the first one (quiz), then up to 2 seconds for the second (code)
        self._wait_dialogs(1, self.timeout)
        if not self._wait_dialogs(2, 2):
            logger.warning("No second alert presented")

    def _wait_dialogs(self, count, timeout):
        waited = 0
        while self._dialogs_handled < count:
            if waited >= timeout * 1000:
                return False
            self.page.wait_for_timeout(100)
            waited += 100
        return True

    def should_be_message_about_adding(self):
        assert self.is_element_present(ProductPageLocators.ITEM_NAME), (
            "Product name is not presented")
        assert self.is_element_present(ProductPageLocators.ITEM_ADDED_MESSAGE), (
            "Message about adding is not presented")
        message = self.page.locator(ProductPageLocators.ITEM_ADDED_MESSAGE).first.inner_text()
        item_name = self.page.locator(ProductPageLocators.ITEM_NAME).first.inner_text()
        assert message == item_name

    def check_cart_worth(self):
        assert self.is_element_present(ProductPageLocators.CART_WORTH), (
            "Message cart total is not presented")
        assert self.is_element_present(ProductPageLocators.ITEM_WORTH), (
            "Product price is not presented")
        cart_worth = self.page.locator(ProductPageLocators.CART_WORTH).first.inner_text()
        item_worth = self.page.locator(ProductPageLocators.ITEM_WORTH).first.inner_text()
        assert cart_worth == item_worth

    def should_not_be_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.ITEM_ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(ProductPageLocators.ITEM_ADDED_MESSAGE), \
            'Success message is not disappeared, but should be'
