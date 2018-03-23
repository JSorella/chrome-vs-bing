from features.browser import Browser
from features.element import BasePageElement


class SearchEngineHomepage(Browser):

    def is_title_matches(self):
        """Verifies that the hardcoded text "Google" appears in page title"""
        return self.title in self.driver.title

    def search(self, value):
        """Triggers the search"""
        BasePageElement.find_element(self.driver, 60, self.TEXT_SEARCH).send_keys(value)
        BasePageElement.find_element(self.driver, 60, self.FIND_BUTTON).click()


class SearchEngineResults(Browser):

    def get_results(self):
        return BasePageElement.find_elements(self.driver, 10, self.RESULT_DIV)

    def get_first_title(self, results):
        title = results[0].find_element(*self.RESULT_TITLE)

        return title
