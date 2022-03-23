from selenium.webdriver.common.by import By
from end_to_end.pages.base_page import BasePage


class HomePage:

    # LOCATORS
    ADD_TO_CART_BTN = (By.XPATH, "//a[@data-product_id='23']")

    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(self.driver)

    def click_first_add_to_cart_button(self):
        self.base.wait_and_click(self.ADD_TO_CART_BTN)




