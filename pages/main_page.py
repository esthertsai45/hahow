import logging

from selenium.webdriver.common.keys import Keys

from locators.locator import Locators
from pages.common import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver = driver)

    def load(self, url):
        logging.info(f"go to {url} website...")
        self.driver.get(url)
        self.wait_for_element_visible(*Locators.MAIN_PAGE)

