from selenium.webdriver.common.by import By
from base_page import BasePage


class HomePage(BasePage):
    def navigate_to_category(self, category):
        self.driver.find_element(By.LINK_TEXT, category).click()

    def verify_products_displayed(self):
        products = self.driver.find_elements(By.CLASS_NAME, "card-title")
        return len(products) > 0
