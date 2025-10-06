import logging
import time
from pathlib import Path

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class Base:
    def __init__(self, driver) -> None:
        self.driver = driver

    def __wait(self, timeout=15) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    def go_to_link(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        try:
            logging.debug("find locator: %s", str(locator))
            self.wait_for_element(*locator)
            element = self.driver.find_element(*locator)
            return element
        except (NoSuchElementException, TimeoutException) as error:
            logging.error(str(error))
            return None

    def find_element_in_element(self, element, *locator):
        try:
            logging.debug("find locator: %s", str(locator))
            inside_element = element.find_element(*locator)
            return inside_element
        except (NoSuchElementException, TimeoutException) as error:
            logging.error(str(error))
            return None

    def find_element_visible(self, *locator):
        try:
            logging.debug("find locator: %s", str(locator))
            self.wait_for_element_visible(*locator)
            element = self.driver.find_element(*locator)
            return element
        except (NoSuchElementException, TimeoutException) as error:
            logging.error(str(error))
            return None

    def find_elements(self, *locator):
        try:
            logging.debug("find locator: %s", str(locator))
            self.wait_for_element(*locator)
            elements = self.driver.find_elements(*locator)
            return elements
        except (NoSuchElementException, TimeoutException) as error:
            logging.error(str(error))
            return None

    def wait_for_element(self, *locator, timeout=0):
        logging.debug("wait for locator to be located: %s", str(locator))
        return self.__wait(timeout if timeout > 0 else 10).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_visible(self, *locator, timeout=0):
        logging.debug("wait for locator to be located: %s", str(locator))
        return self.__wait(timeout if timeout > 0 else 10).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_invisible(self, *locator, timeout=0):
        logging.debug("wait for locator becomes invisible: %s", str(locator))
        return self.__wait(timeout if timeout > 0 else 10).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, *locator, timeout=0):
        logging.debug("wait for locator to be clickable: %s", str(locator))
        return self.__wait(timeout if timeout > 0 else 10).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_not_present(self, *locator, timeout=0):
        return self.__wait(timeout if timeout > 0 else 10).until(
            EC.invisibility_of_element_located(locator)
        )

    def scroll_to_position(self, x, y) -> None:
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def take_screenshot(self, file_name: str):
        current_dir = Path(__file__).resolve()
        parent_dir = current_dir.parent.parent
        print(parent_dir)
        self.driver.save_screenshot(file_name)
        allure.attach.file(
            f"{parent_dir}{file_name}",
            file_name,
            attachment_type=allure.attachment_type.PNG,
        )

    def scroll_to_element_by_locator(self, *locator):
        element = self.find_element(*locator)
        x = element.location["x"]
        y = element.location["y"]
        self.scroll_to_position(x / 2, y)
        time.sleep(1)

    def click_element_by_locator(self, *locator) -> None:
        element = self.wait_for_element_clickable(*locator, timeout=20)
        if element is not None:
            self.click_element_by_element(element)
        else:
            logging.debug("cannot find element")

    def click_element_by_element(self, element):
        logging.debug("click element: %s", str(element))
        element.click()

    def select_element(self, *locator):
        try:
            logging.debug("find locator: %s", str(locator))
            self.wait_for_element(*locator)
            element = self.driver.find_element(*locator)
            time.sleep(1)
            return Select(element)
        except (NoSuchElementException, TimeoutException) as error:
            logging.error(str(error))
            return None

    def input_keys(self, keys: str, *locator) -> None:
        logging.info('input keys "%s" to element: %s', keys, str(locator))
        txt = self.find_element(*locator)
        txt.send_keys(keys)

    def get_webdriver(self):
        return self.driver

    def get_window_size(self):
        logging.warning(self.driver.get_window_size())
        return self.driver.get_window_size()

    def switch_to_iframe(self, *locator):
        iframe = self.driver.find_element(*locator)
        self.driver.switch_to.frame(iframe)

    def back_to_default_content(self):
        self.driver.switch_to.default_content()

    # def wait_for_alert(self):
    #     WebDriverWait(self.driver, self.TIME_OUT).until(EC.alert_is_present())

    # def click_alert_accept(self):
    #     self.driver.switch_to.alert.accept()

    # def click_alert_dismiss(self):
    #     self.driver.switch_to.alert.dismiss()

    def teardown_webdriver(self):
        self.driver.close()
        self.driver.quit()