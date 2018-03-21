from selenium.webdriver.common.by import By

class GoogleLocators(object):
    """A class for main page locators. All main page locators should come here"""
    FIND_BUTTON = (By.NAME, 'btnK')
    RESULT_DIV = (By.CLASS_NAME, 'rc')

class BingLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass
