from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "pass")
    CONFIRM_BUTTON = (By.NAME, "commit")
