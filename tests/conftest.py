import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(options=Options())
    yield driver
    driver.quit()
