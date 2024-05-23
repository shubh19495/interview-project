import pytest
from selenium.webdriver.common.by import By

def test_logout(driver):
    driver.find_element(By.ID, "logout2").click()
    # Add assertions to verify successful logout
