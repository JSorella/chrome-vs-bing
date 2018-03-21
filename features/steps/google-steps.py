from behave import *


@given('a Firefox navigator')
def step_impl(context):
    pass

@when('the user access to Google')
def step_impl(context):
    context.google.access_page()

@then('the homepage title says "Google"')
def step_impl(context):
    assert context.google.is_title_matches

############################

@given('a Google home page in Firefox')
def step_impl(context):
    context.google.access_page()

@when('the user searchs for "Globant"')
def step_impl(context):
    context.google.search_text_element = 'Globant'
    context.google.click_find()

@then('the engine returns more than 3 results')
def step_impl(context):
    results = context.search_results_page.get_results()
    assert (len(results) > 3)
