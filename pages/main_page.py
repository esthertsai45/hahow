import logging

from selenium.webdriver.common.keys import Keys

from locators.locator import Locators
from pages.common import Base
from pages.contributor_page import ContributorPage

logger = logging.getLogger(__name__)


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver = driver)

    def load(self, url):
        logging.info(f"go to {url} website...")
        self.driver.get(url)
        self.wait_for_element_visible(*Locators.MAIN_PAGE)
    
    def find_contributors(self):
        contributors_block = self.find_element(*Locators.CONTRIBUTORS_BLOCK)
        contributor_links = contributors_block.find_elements(*Locators.CONTRIBUTOR_LINKS)
        contributors = []
        for link in contributor_links:
            href = link.get_attribute("href")
            name = href.split("/")[-1]
            contributors.append(name)
        print(f"{contributors}")
        return contributors