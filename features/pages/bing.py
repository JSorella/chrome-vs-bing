from search_engine import SearchEngineHomepage, SearchEngineResults
from selenium.webdriver.common.by import By


class BingHome(SearchEngineHomepage):
    """Home page action methods come here. I.e. Python.org"""

    FIND_BUTTON = (By.NAME, 'go')
    TEXT_SEARCH = (By.NAME, 'q')

    def __init__(self, driver):
        super(BingHome, self).__init__(driver)
        self.url = "http://www.bing.com"
        self.title = "Bing"

    def get_results_page(self):
        return BingSearchResults(self.driver)


class BingSearchResults(SearchEngineResults):
    """Search results page action methods come here"""

    RESULT_DIV = (By.CLASS_NAME, 'b_algo')
    RESULT_TITLE = (By.CSS_SELECTOR, 'a')
