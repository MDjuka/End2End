from selenium.webdriver.common.by import By
from end_to_end.pages.base_page import BasePage


class OrderReceivedPage:

    # LOCATORS
    ORDER_RECEIVED_CONFIRMATION = (By.XPATH, "//h1[@class='entry-title']")
    ORDER_NUMBER = (By.CSS_SELECTOR, "li.order strong")

    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(self.driver)

    def verify_order_received_confirmation_loaded(self):
        self.base.wait_until_element_contains_text(self.ORDER_RECEIVED_CONFIRMATION, "Order received")

    def get_order_number(self):
        return self.base.wait_and_get_element_text(self.ORDER_NUMBER)