import allure
from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Checking presence of all elements ")
    def all_elements_login_page_present(self):
        self.should_be_login_field()
        self.should_be_password_field()
        self.should_be_confirm_button()

    @allure.step("Checking presence of login field ")
    def should_be_login_field(self):
        assert self.has_element_appeared(*LoginPageLocators.EMAIL_INPUT), \
            "Login Input Field is missing on the Login Page!"

    @allure.step("Checking presence of password field ")
    def should_be_password_field(self):
        assert self.has_element_appeared(*LoginPageLocators.PASSWORD_INPUT), \
            "Password Input Field is missing on the Login Page!"

    @allure.step("Checking presence of confirm button")
    def should_be_confirm_button(self):
        assert self.has_element_appeared(*LoginPageLocators.CONFIRM_BUTTON), \
            "Confirm Button is missing on the Login Page!"
