import pytest

from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.user_cart import UserCart


@pytest.mark.login_test
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, page):
        link = MainPageLocators.MAIN_PAGE_LINK
        main_page = MainPage(page, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(page=page, url=page.url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, page):
        link = MainPageLocators.MAIN_PAGE_LINK
        main_page = MainPage(page, link)
        main_page.open()
        main_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(page):
    link = MainPageLocators.MAIN_PAGE_LINK
    main_page = MainPage(page, link)
    main_page.open()
    main_page.should_be_user_cart()
    main_page.go_to_user_cart()
    cart = UserCart(page, page.url)
    cart.should_be_empty()
