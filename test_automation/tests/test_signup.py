import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, ElementClickInterceptedException, NoSuchElementException
from pages.signup_page import SignUpPage



@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com")
    yield driver
    driver.quit()

def handle_alert(driver):
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text
    except Exception as e:
        return None

def test_signup_positive(driver):
    signup_page = SignUpPage(driver)
    signup_page.navigate_to_signup()

    # Wait for the username field to be visible and enabled
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "sign-username"))
    )

    signup_page.sign_up("validUser", "validPassword")



def test_signup_negative(driver):
    signup_page = SignUpPage(driver)
    signup_page.navigate_to_signup()

    try:
        # Wait for the sign-up modal to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "sign-username"))
        )
        print("Sign-up modal is visible.")
    except (ElementNotInteractableException, ElementClickInterceptedException) as e:
        print(f"Failed to interact with sign-up modal: {e}")
        assert False, "Test failed due to element not being interactable"

    # Attempt to sign up with empty credentials
    signup_page.sign_up("", "")

    # Handle potential alert
    alert_text = handle_alert(driver)
    if alert_text:
        print(f"Alert detected: {alert_text}")

    # Check for validation messages or error indications
    try:
        error_message = driver.find_element(By.ID, "sign-username").get_attribute("validationMessage")
        print(f"Validation message: {error_message}")
        assert error_message, "Expected validation message is not displayed."
    except NoSuchElementException as e:
        print(f"No validation message element found: {e}")
        assert False, "Validation message element not found."

    # Optionally check for other error messages or indicators specific to your application
    # For example, if there's a specific error message element for invalid sign-ups
    try:
        error_message = driver.find_element(By.ID, "error-message-id").text
        print(f"Error message: {error_message}")
        assert "Expected error text" in error_message, "Expected error message not found."
    except NoSuchElementException:
        print("No specific error message element found.")


