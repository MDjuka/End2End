from selenium.webdriver.common.by import By
from end_to_end.pages.base_page import BasePage
import logging as logger


class MyAccountSignedOut:

    # LOCATORS
    LOGIN_USER_NAME = (By.ID, "username")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login']")
    ERROR_MSG_TXT = (By.CSS_SELECTOR, "ul.woocommerce-error")
    REGISTER_EMAIL = (By.ID, "reg_email")
    REGISTER_PASSWORD = (By.ID, "reg_password")
    REGISTER_BUTTON = (By.XPATH, "//button[@value='Register']")

    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(self.driver)

    def input_login_username(self, username):
        self.base.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.base.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        logger.debug("Clicking 'login' button.")
        self.base.wait_and_click(self.LOGIN_BUTTON)

    def wait_until_error_is_displayed(self, expected_error):
        self.base.wait_until_element_contains_text(self.ERROR_MSG_TXT, expected_error)

    def input_register_email(self, email):
        self.base.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.base.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        logger.debug("Clicking 'register' button.")
        self.base.wait_and_click(self.REGISTER_BUTTON)
