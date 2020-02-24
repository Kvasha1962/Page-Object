import pages.login_page as login_page
from pages.main_page import MainPage
# from .pages.login_page import LoginPage
# from .pages.locators import LoginPageLocators


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link, 10)
    # login_page.should_be_login_url()
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page_login = login_page.LoginPage(browser, login_page.LoginPageLocators.LOGIN_URL, 10)
    page_login.should_be_login_page()
