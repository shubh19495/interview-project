from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_signup(self):
        self.click_with_retry(By.ID, "signin2")

    def click_with_retry(self, by, value, retries=3):
        for _ in range(retries):
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((by, value))
                )
                element.click()
                return
            except ElementClickInterceptedException:
                self.close_active_modal()
        raise ElementClickInterceptedException(f"Could not click the element: {value}")

    def close_active_modal(self):
        try:
            close_buttons = self.driver.find_elements(By.XPATH, "//div[@class='modal fade show']//button[contains(text(), 'Close')]")
            for button in close_buttons:
                try:
                    button.click()
                    WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(button))
                except (ElementClickInterceptedException, NoSuchElementException, TimeoutException):
                    continue
        except NoSuchElementException:
            pass  # Modal is not present

    def sign_up(self, username, password):
        self.driver.find_element(By.ID, "sign-username").send_keys(username)
        self.driver.find_element(By.ID, "sign-password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Sign up')]").click()

    def is_signed_up_successfully(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return "Sign up successful." in alert_text
        except TimeoutException:
            return False

    def is_error_message_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return "This user already exist." in alert_text
        except TimeoutException:
            return False
