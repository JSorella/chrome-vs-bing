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
    context.result_page = engine_page.search(term)


@then('the {engine} engine returns more than 3 results')
def step_impl(context, engine):
    results = context.result_page.get_results()
    assert (len(results) > 3)


@then('the first title result in {engine} contains "{term}" on it')
def step_impl(context, engine, term):
    results = context.result_page.get_results()
    first_title = context.result_page.get_first_title(results)

    assert (term in first_title.text.lower())


@given('two web search engines: {engine_a} and {engine_b}')
def step_impl(context, engine_a, engine_b):
    context.engine_page_a = getattr(context, engine_a.lower())
    context.engine_page_b = getattr(context, engine_b.lower())


@when('the user search for "{term}" in {engine_a} and {engine_b}')
def step_impl(context, term, engine_a, engine_b):
    context.engine_page_a.access_page()
    context.result_page = context.engine_page_a.search(term)
    context.results_a = context.result_page.get_results()
    context.first_title_a = context.result_page.get_first_title(context.results_a)

    context.engine_page_b.access_page()
    context.result_page = context.engine_page_b.search(term)
    context.results_b = context.result_page.get_results()
    context.first_title_b = context.result_page.get_first_title(context.results_b)


@then('{engine_b} returns more results than {engine_a}')
def step_impl(context, engine_a, engine_b):
    assert (len(context.results_b) > len(context.results_a))


@then('the first result in {engine_a} is not the same as in {engine_b}')
def step_impl(context, engine_a, engine_b):
    assert (context.first_title_a != context.first_title_b)
