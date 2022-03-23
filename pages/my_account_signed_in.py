from selenium.webdriver.common.by import By
from end_to_end.pages.base_page import BasePage


class MyAccountSignedIn:

    # LOCATORS
    LOGOUT_BTN = (By.LINK_TEXT, 'Logout')

    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(self.driver)

    def verify_user_is_signed_in(self):
        self.base.wait_until_element_is_visible(self.LOGOUT_BTN)