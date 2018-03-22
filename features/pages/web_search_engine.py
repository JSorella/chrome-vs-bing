from features.browser import Browser
from abc import ABCMeta, abstractmethod


class WebSearchEngine(Browser):

    def is_title_matches(self):
        """Verifies that the hardcoded text "Google" appears in page title"""
        return self.title in self.driver.title

    def click_find(self):
        """Triggers the search"""
        find_locator = self._get_find_locator()
        element = self.driver.find_element(*find_locator)
        element.click()

    @abstractmethod
    def _get_find_locator(self):
        pass
