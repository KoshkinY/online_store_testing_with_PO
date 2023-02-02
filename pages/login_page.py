from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "there is not 'login' in url"

    def should_be_login_form(self):
        #login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login link is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        #register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Login link is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register link is not presented"


    #class MainPage(BasePage):
    #def go_to_login_page(self):
    #    login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #    login_link.click()
    #def should_be_login_link(self):
    #    assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"