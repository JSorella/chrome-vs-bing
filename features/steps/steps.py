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
    engine_page.search(term)


@then('the {engine} engine returns more than 3 results')
def step_impl(context, engine):
    engine_page = getattr(context, engine.lower() + '_search_results')
    results = engine_page.get_results()
    assert (len(results) > 3)


@given('two web search engines: {engine_a} and {engine_b}')
def step_impl(context, engine_a, engine_b):
    context.engine_page_a = getattr(context, engine_a.lower())
    context.engine_page_b = getattr(context, engine_b.lower())


@when('the user search for "{term}" in {engine_a} and {engine_b}')
def step_impl(context, term, engine_a, engine_b):
    context.engine_page_a.access_page()
    context.engine_page_a.search(term)
    results_a_page = getattr(context, engine_a.lower() + '_search_results')
    context.results_a = results_a_page.get_results()
    context.first_title_a = results_a_page.get_first_title(context.results_a)

    context.engine_page_b.access_page()
    context.engine_page_b.search(term)
    results_b_page = getattr(context, engine_b.lower() + '_search_results')
    context.results_b = results_b_page.get_results()
    context.first_title_b = results_b_page.get_first_title(context.results_b)


@then('{engine_b} returns more results than {engine_a}')
def step_impl(context, engine_a, engine_b):
    assert (len(context.results_b) > len(context.results_a))


@then('the first result in {engine_a} is not the same as in {engine_b}')
def step_impl(context, engine_a, engine_b):
    assert (context.first_title_a != context.first_title_b)
