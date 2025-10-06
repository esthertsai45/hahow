import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from locators.locator import Locators
from pages.common import Base

logger = logging.getLogger(__name__)
WAIT_TIME = 15


class FrontendMDPage(Base):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def load(self, url):
        logging.info(f"go to {url} website...")
        self.driver.get(url)
        self.wait_for_element(*Locators.FRONTEND_MD_PAGE)

    def check_the_image_exists(self):
        wireframe_img1_element = self.find_element(*Locators.IMAGE1_XPATH)
        image_url1 = wireframe_img1_element.get_attribute("src")
        wireframe_img2_element = self.find_element(*Locators.IMAGE2_XPATH)
        image_url2 = wireframe_img2_element.get_attribute("src")
        self.scroll_to_element_by_locator(*Locators.IMAGE1_XPATH)
        self.take_screenshot("wireframe.png")
        return (("/hahow/hahow-recruit/raw/master/assets/hero-list-page.png" in image_url1) and
                ("/hahow/hahow-recruit/raw/master/assets/hero-profile-page.png" in image_url2))

    def check_the_latest_commitor(self):
        latest_commit_container = self.find_element(*Locators.LATEST_COMMIT_CONTAINER_XPATH)
        commitor_name = latest_commit_container.find_element(*Locators.COMMITOR_NAME_XPATH)
        return commitor_name.text