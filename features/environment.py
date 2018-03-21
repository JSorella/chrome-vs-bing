from features.browser import Browser
from features.pages.google import Google
from features.pages.google import SearchResultsPage
from selenium import webdriver


def before_all(context):
    driver = webdriver.Firefox()

    context.browser = Browser(driver)
    context.google = Google(driver)
    context.search_results_page = SearchResultsPage(driver)


def after_all(context):
    context.browser.close()
