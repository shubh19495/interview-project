import pytest
from pages.product_page import ProductPage

def test_add_to_cart(driver):
    product_page = ProductPage(driver)
    product_page.navigate_to_last_page_and_select_last_product()
    # Add assertions to verify product is added to the cart
