import pytest
from test_automation.pages.login_page import LoginPage
import openpyxl

def get_login_data():
    try:
        workbook = openpyxl.load_workbook('data/login_data.xlsx')
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(row)
        return data
    except Exception as e:
        print(f"Error reading login data: {e}")
        return []

@pytest.mark.parametrize("username,password", get_login_data())
def test_login_positive(driver, username, password):
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.login(username, password)
    # Add assertions to verify successful login
    assert login_page.is_logged_in(), "Login was not successful"

def test_login_negative(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.login("invalidUser", "invalidPassword")
    # Add assertions to verify error message
    assert login_page.is_error_message_displayed(), "Error message was not displayed"
