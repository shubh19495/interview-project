from selenium.webdriver.common.by import By
from base_page import BasePage

class CartPage(BasePage):
    def verify_cart_items(self):
        self.driver.find_element(By.ID, "cartur").click()
        items = self.driver.find_elements(By.CLASS_NAME, "success")
        return len(items) > 0

    def checkout(self):
        self.driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
