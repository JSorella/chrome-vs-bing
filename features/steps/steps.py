from behave import *


@given('a Firefox navigator')
def step_impl(context):
    pass


@when('the user access to {engine}')
def step_impl(context, engine):
    engine_page = getattr(context, engine.lower())
    engine_page.access_page()


@then('the homepage title says "{engine}"')
def step_impl(context, engine):
    engine_page = getattr(context, engine.lower())
    assert engine_page.is_title_matches


@given('a {engine} home page in Firefox')
def step_impl(context, engine):
    engine_page = getattr(context, engine.lower())
    engine_page.access_page()


@when('the user search for "{term}" using {engine}')
def step_impl(context, term, engine):
    engine_page = getattr(context, engine.lower())
    engine_page.search_text_element = term
    engine_page.click_find()


@then('the {engine} engine returns more than 3 results')
def step_impl(context, engine):
    engine_page = getattr(context, engine.lower() + '_search_results')
    results = engine_page.get_results()
    assert (len(results) > 3)


@then('{engine_a} returns more results than {engine_b}')
def step_impl(context, engine_a, engine_b):
    engine_a_page = getattr(context, engine_a.lower() + '_search_results')
    engine_b_page = getattr(context, engine_b.lower() + '_search_results')
    results_a = engine_a_page.get_results()
    results_b = engine_b_page.get_results()
    assert (len(results_a) > len(results_b))


@then('the first result in {engine_a} is not the same as in {engine_b}')
def step_impl(context, engine_a, engine_b):
    engine_a_page = getattr(context, engine_a.lower() + '_search_results')
    engine_b_page = getattr(context, engine_b.lower() + '_search_results')
    title_a = engine_a_page.get_first_title()
    title_b = engine_b_page.get_first_title()
    assert (title_a != title_b)
