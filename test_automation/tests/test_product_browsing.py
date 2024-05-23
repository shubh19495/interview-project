import pytest
from pages.home_page import HomePage

def test_verify_products_displayed(driver):
    home_page = HomePage(driver)
    assert home_page.verify_products_displayed(), "Products are not displayed on the homepage"

def test_verify_category_navigation(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_category("Laptops")
    assert home_page.verify_products_displayed(), "Products are not displayed in the selected category"
