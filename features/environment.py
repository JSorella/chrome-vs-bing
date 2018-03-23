from features.pages.bing import BingHome
from features.pages.bing import BingSearchResults
from features.pages.google import GoogleHome
from features.pages.google import GoogleSearchResults
from selenium import webdriver


def before_all(context):
    driver = webdriver.Firefox()

    context.google = GoogleHome(driver)
    context.bing = BingHome(driver)
    context.google_search_results = GoogleSearchResults(driver)
    context.bing_search_results = BingSearchResults(driver)


def after_all(context):
    context.google.close()
    context.bing.close()
    context.google_search_results.close()
    context.bing_search_results.close()
