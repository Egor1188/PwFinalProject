from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from loguru import logger


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.page.url

    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # checks that the registration form is present on the page
        assert self.is_element_present(LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        logger.info('Registering user {}', email)
        self.page.locator(LoginPageLocators.REGISTER_FORM_EMAIL).fill(email)
        self.page.locator(LoginPageLocators.REGISTER_FORM_PASSWORD).fill(password)
        self.page.locator(LoginPageLocators.REGISTER_FORM_PASSWORD_REPEAT).fill(password)
        self.page.locator(LoginPageLocators.REGISTER_BUTTON).click()
        assert self.is_element_present(LoginPageLocators.MESSAGE_ABOUT_REGISTRATION)
