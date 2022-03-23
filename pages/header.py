from selenium.webdriver.common.by import By
from end_to_end.pages.base_page import BasePage

class Header:

    # LOCATORS
    CART = (By.ID, "site-header-cart")
    CART_ITEM_COUNT = (By.CSS_SELECTOR, 'a.cart-contents span.count')

    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(self.driver)

    def click_on_cart_on_right_header(self):
        self.base.wait_and_click(self.CART)

    def wait_until_cart_item_count(self, count):
        expected_text = str(count) + ' item'
        self.base.wait_until_element_contains_text(self.CART_ITEM_COUNT, expected_text)
