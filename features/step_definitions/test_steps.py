from behave import given, when, then
from pages.page_objects import GooglePage
from utils.selenium_utils import initialize_webdriver

@given('I am on the Google homepage')
def step_impl(context):
    context.driver = initialize_webdriver()
    context.google_page = GooglePage(context.driver)
    context.google_page.load()

@when('I search for "{search_term}"')
def step_impl(context, search_term):
    context.google_page.search(search_term)

@then('I should see search results related to "{search_term}"')
def step_impl(context, search_term):
    assert search_term in context.driver.title
    context.driver.quit()