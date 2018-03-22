from features.browser import Browser
from features.pages.bing import Bing
from features.pages.bing import BingSearchResults
from features.pages.google import Google
from features.pages.google import GoogleSearchResults
from selenium import webdriver


def before_all(context):
    google_driver = webdriver.Firefox()
    bing_driver = webdriver.Firefox()

    context.google = Google(google_driver)
    context.bing = Bing(bing_driver)
    context.google_search_results = GoogleSearchResults(google_driver)
    context.bing_search_results = BingSearchResults(bing_driver)


def after_all(context):
    context.google.close()
    context.bing.close()
