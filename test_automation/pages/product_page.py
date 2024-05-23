from selenium.webdriver.common.by import By
from base_page import BasePage

class ProductPage(BasePage):
    def navigate_to_last_page_and_select_last_product(self):
        while True:
            try:
                next_button = self.driver.find_element(By.ID, "next2")
                next_button.click()
            except:
                break
        products = self.driver.find_elements(By.CLASS_NAME, "card-title")
        products[-1].click()
        self.driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
