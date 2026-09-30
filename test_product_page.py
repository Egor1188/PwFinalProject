import time

import pytest

from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.user_cart import UserCart


items = [
    'coders-at-work_207/?promo=newYear2019',
    'coders-at-work_207/?promo=offer0',
    'coders-at-work_207/?promo=offer1',
    'coders-at-work_207/?promo=offer2',
    'coders-at-work_207/?promo=offer3',
    'coders-at-work_207/?promo=offer4',
    'coders-at-work_207/?promo=offer5',
    'coders-at-work_207/?promo=offer6',
    pytest.param('coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail),
    'coders-at-work_207/?promo=offer8',
    'coders-at-work_207/?promo=offer9',
    'the-shellcoders-handbook_209/?promo=newYear'
]


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, page):
        self.email = str(time.time()) + '@example.com'
        self.password = 'ZgUnV)12345'
        login_page = LoginPage(page, LoginPageLocators.LOGIN_LINK)
        login_page.open()
        login_page.register_new_user(self.email, self.password)

    def test_user_can_add_product_to_basket(self, page):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        product_page = ProductPage(page=page, url=link)
        product_page.open()
        product_page.is_user_authorized()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_message_about_adding()
        product_page.check_cart_worth()

    def test_user_cant_see_success_message(self, page):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        product_page = ProductPage(page=page, url=link)
        product_page.open()
        product_page.is_user_authorized()
        product_page.should_not_be_success_message()


@pytest.mark.parametrize('item', items)
def test_guest_can_add_product_to_basket(page, item):
    link = f'https://selenium1py.pythonanywhere.com/catalogue/{item}'
    product_page = ProductPage(page=page, url=link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_about_adding()
    product_page.check_cart_worth()


@pytest.mark.xfail(reason="Сообщение об успехе появляется и не исчезает — ожидаемое поведение сайта")
def test_guest_cant_see_success_message_after_adding_product_to_basket(page):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(page=page, url=link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(page):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(page=page, url=link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="Сообщение об успехе появляется и не исчезает — ожидаемое поведение сайта")
def test_message_disappeared_after_adding_product_to_basket(page):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(page=page, url=link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(page):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(page, link)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(page):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(page, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(page=page, url=page.url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(page):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(page, link)
    product_page.open()
    product_page.should_be_user_cart()
    product_page.go_to_user_cart()
    cart = UserCart(page, page.url)
    cart.should_be_empty()
