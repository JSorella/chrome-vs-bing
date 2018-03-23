from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.remote.webelement import WebElement


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    @staticmethod
    def find_element(driver, timeout, locator):

        result = WebDriverWait(
            driver, timeout, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException]).until(
                lambda s: expected_conditions.visibility_of_element_located(locator)(driver)
            )

        if isinstance(result, WebElement):
            return result
        else:
            raise NoSuchElementException("The element was not found on DOM")

    @staticmethod
    def find_elements(driver, timeout, locator):

        results = WebDriverWait(
            driver, timeout, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException]).until(
            lambda s: expected_conditions.visibility_of_any_elements_located(locator)(driver)
        )

        if all(isinstance(result, WebElement) for result in results):
            return results
        else:
            raise NoSuchElementException("The element was not found on DOM")
