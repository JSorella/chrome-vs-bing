from features.pages.bing import BingHome
from features.pages.google import GoogleHome
from selenium import webdriver


def before_all(context):
    driver = webdriver.Firefox()

    context.google = GoogleHome(driver)
    context.bing = BingHome(driver)


def after_all(context):
    context.google.close()
    context.bing.close()
