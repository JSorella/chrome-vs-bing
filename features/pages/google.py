from features.element import BasePageElement
from features.pages.locators import GoogleLocators
from features.browser import Browser


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class Google(Browser):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def access_page(self):
        self.driver.get("http://www.google.com")

    def is_title_matches(self):
        """Verifies that the hardcoded text "Google" appears in page title"""
        return "Google" in self.driver.title

    def click_find(self):
        """Triggers the search"""
        element = self.driver.find_element(*GoogleLocators.FIND_BUTTON)
        element.click()


class SearchResultsPage(Browser):
    """Search results page action methods come here"""

    def get_results(self):
        return self.driver.find_elements(*GoogleLocators.RESULT_DIV)
