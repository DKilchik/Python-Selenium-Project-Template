import pytest
import allure
from pages.login_page import LoginPage
from pages.base_page import BasePage


@pytest.mark.login_page
@allure.suite("Test Login Page")
@allure.title("URL validation after login page opening ")
def test_should_be_login_page_url(browser):
    with allure.step("Open login page"):
        base_page = BasePage()
        link = (base_page.get_conf_param('DEFAULT', 'host')) + '/login'
        page = LoginPage(browser, link)
        page.open()

    with allure.step("URL validation"):
        assert 'login' in browser.current_url, "Substring 'login' is missing in login page URL!"


@pytest.mark.login_page
@allure.suite("Test Login Page")
@allure.title("Checking presence of all login page elements ")
def test_all_elements_login_page_present(browser):
    with allure.step("Open login page"):
        base_page = BasePage()
        link = (base_page.get_conf_param('DEFAULT', 'host')) + '/login'
        page = LoginPage(browser, link)
        page.open()

    page.all_elements_login_page_present()
