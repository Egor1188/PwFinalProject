# Locators are CSS selectors (strings), same as in the Selenium version


class LoginPageLocators:
    LOGIN_LINK = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = "#login_form"
    REGISTER_FORM = "#register_form"
    REGISTER_FORM_EMAIL = '#id_registration-email'
    REGISTER_FORM_PASSWORD = '#id_registration-password1'
    REGISTER_FORM_PASSWORD_REPEAT = '#id_registration-password2'
    REGISTER_BUTTON = '#register_form > button'
    MESSAGE_ABOUT_REGISTRATION = '#messages > div > div'
