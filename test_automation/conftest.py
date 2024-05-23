import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com")
    yield driver
    driver.quit()
