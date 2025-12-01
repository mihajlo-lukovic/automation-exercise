import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions

from framework.common import get_app_config
from framework.enums import Actions

TIMEOUT = Actions.TIMEOUT.value


_locator_types = {
    'class': (By.CLASS_NAME, lambda value: value),
    'css': (By.CSS_SELECTOR, lambda value: value),
    'id': (By.ID, lambda value: value),
    'xpath': (By.XPATH, lambda value: value)
}


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver.driver

    @classmethod
    def parse_locator(cls, locator):
        try:
            locator_type, locator_value = locator.split('=', 1)
            by_param, value_param = _locator_types[locator_type]
            return by_param, value_param(locator_value)
        except KeyError:
            raise NoSuchElementException(f'Invalid locator type: {locator}')

    def find_element_by_locator(self, locator, parent=None):
        by, value = self.parse_locator(locator=locator)

        if parent is not None:
            return parent.find_element(by=by, value=value)

        return self.driver.find_element(by=by, value=value)

    def find_elements_by_locator(self, locator):
        by, value = self.parse_locator(locator=locator)
        return self.driver.find_elements(by=by, value=value)

    def is_element_present(self, locator):
        try:
            self.find_element_by_locator(locator=locator)
            return True
        except NoSuchElementException:
            return False

    def wait_to_be_displayed(self, locator, timeout=TIMEOUT, message=None):
        if message is None:
            message = (
                f'Element {locator} is not displayed in a given time {timeout}'
            )
        return WebDriverWait(self.driver, timeout).until(
            conditions.visibility_of_element_located(
                self.parse_locator(locator=locator)
            ),
            message=message
        )

    def wait_to_be_clickable(self, locator, timeout=TIMEOUT, message=None):
        if message is None:
            message = (
                f'Element {locator} is not clickable in a given time {timeout}'
            )
        return WebDriverWait(self.driver, timeout).until(
            conditions.element_to_be_clickable(
                self.parse_locator(locator=locator)
            ),
            message=message
        )

    def wait_for_url_to_be(self, url, timeout=TIMEOUT, message=None):
        return WebDriverWait(self.driver, timeout).until(
            conditions.url_to_be(url),
            message=message
        )

    def accept_js_alert(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            conditions.alert_is_present()
        )
        alert = self.driver.switch_to.alert
        alert.accept()

    def scroll_to(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def click(self, locator):
        element = self.find_element_by_locator(locator=locator)
        self.scroll_to(element=element)
        element.click()

    def wait_and_click(self, locator, timeout=TIMEOUT, message=None):
        self.wait_to_be_clickable(
            locator=locator,
            timeout=timeout,
            message=message
        )

        self.click(locator=locator)

    def attribute_text(self, locator, attribute, timeout=TIMEOUT):
        now = time.time()
        while time.time() - now < timeout:
            if self.is_element_present(locator=locator):
                element = self.find_element_by_locator(locator=locator)
                return element.get_attribute(attribute)
            else:
                time.sleep(0.5)
        else:
            raise TimeoutException(
                f'Element {locator} is not visible in a given time {timeout}.'
            )

    def text(self, locator, timeout=TIMEOUT):
        now = time.time()
        while time.time() - now < timeout:
            if self.is_element_present(locator=locator):
                element = self.find_element_by_locator(locator=locator)
                return element.text
            else:
                time.sleep(0.5)
        else:
            raise TimeoutException(
                f'Element {locator} is not visible in a given time {timeout}.'
            )

    def clear(self, locator):
        self.find_element_by_locator(locator=locator).clear()

    def type(self, locator, keys, clear=False):
        if clear:
            self.clear(locator=locator)

        self.find_element_by_locator(locator=locator).send_keys(keys)

    def navigate(self, url=None):
        if url is None:
            # Use default platform URL
            config = get_app_config()
            url = config.get('platform').get('url')

        self.driver.get(url)

    def select_by_text(self, locator, option):
        select_option = Select(self.find_element_by_locator(locator=locator))
        select_option.select_by_visible_text(text=option)
