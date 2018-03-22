from features.element import BasePageElement
from features.browser import Browser
from web_search_engine import WebSearchEngine
from selenium.webdriver.common.by import By


class BingLocators(object):
    """A class for main page locators. All main page locators should come here"""
    FIND_BUTTON = (By.NAME, 'go')
    RESULT_DIV = (By.CLASS_NAME, 'b_algo')
    RESULT_TITLE = (By.CSS_SELECTOR, 'a')



class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class Bing(WebSearchEngine):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def __init__(self, driver):
        super(Bing, self).__init__(driver)
        self.url = "http://www.bing.com"
        self.title = "Bing"

    def _get_find_locator(self):
        return BingLocators.FIND_BUTTON


class BingSearchResults(Browser):
    """Search results page action methods come here"""

    def get_results(self):
        return self.driver.find_elements(*BingLocators.RESULT_DIV)

    def get_first_title(self):
        results = self.get_results()
        title = results[0].find_element(*BingLocators.RESULT_TITLE)

        return title
