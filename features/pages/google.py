from features.pages.search_engine import SearchEngineHomepage,SearchEngineResults
from selenium.webdriver.common.by import By


class GoogleHome(SearchEngineHomepage):

    """Home page action methods come here. I.e. Python.org"""
    FIND_BUTTON = (By.NAME, 'btnK')
    TEXT_SEARCH = (By.NAME, 'q')

    def __init__(self, driver):
        super(GoogleHome, self).__init__(driver)
        self.url = "http://www.google.com"
        self.title = "Google"


class GoogleSearchResults(SearchEngineResults):
    """Search results page action methods come here"""

    RESULT_DIV = (By.CLASS_NAME, 'rc')
    RESULT_TITLE = (By.CSS_SELECTOR, 'a')
