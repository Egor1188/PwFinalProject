from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, expect

from locators.base_page_locators import BasePageLocators
from loguru import logger


class BasePage:
    def __init__(self, page: Page, url, timeout=10):
        self.page = page
        self.url = url
        # default timeout for waits (in seconds, same as in the Selenium version)
        self.timeout = timeout
        self.page.set_default_timeout(timeout * 1000)

    def go_to_login_page(self):
        logger.info('Going to the login page')
        self.page.locator(BasePageLocators.LOGIN_LINK).click()

    def open(self):
        logger.info('Opening {}', self.url)
        self.page.goto(self.url)

    def is_element_present(self, selector, timeout=None):
        if timeout is None:
            timeout = self.timeout
        try:
            self.page.locator(selector).first.wait_for(state="attached", timeout=timeout * 1000)
        except PlaywrightTimeoutError:
            logger.debug('Element not found within {} s: {}', timeout, selector)
            return False
        logger.debug('Element found: {}', selector)
        return True

    def is_not_element_present(self, selector, timeout=2):
        return not self.is_element_present(selector, timeout)

    def is_disappeared(self, selector, timeout=4):
        try:
            self.page.locator(selector).first.wait_for(state="detached", timeout=timeout * 1000)
        except PlaywrightTimeoutError:
            logger.warning('Element did not disappear within {} s: {}', timeout, selector)
            return False
        logger.debug('Element disappeared: {}', selector)
        return True

    def should_have_text(self, selector, expected_text, exact=True, timeout=None):
        # exact=True - the element text matches fully (like have.text), exact=False - contains the substring
        if timeout is None:
            timeout = self.timeout
        locator = self.page.locator(selector).first
        if exact:
            expect(locator).to_have_text(expected_text, timeout=timeout * 1000)
        else:
            expect(locator).to_contain_text(expected_text, timeout=timeout * 1000)

    def should_be_login_link(self):
        assert self.is_element_present(BasePageLocators.LOGIN_LINK), "Login link is not present"

    def should_be_user_cart(self):
        assert self.is_element_present(BasePageLocators.USER_CART), "User cart is not present"

    def go_to_user_cart(self):
        logger.info('Going to the cart')
        self.page.locator(BasePageLocators.USER_CART).click()

    def is_user_authorized(self):
        assert self.is_element_present(BasePageLocators.USER_ICON), 'User icon is absent, probably unauthorized user'
