from behave import given, when, then
from selenium import webdriver
from pages.login_fb_page import LoginFBPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By

@given('the user is on the login intu page')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()  # o webdriver.Firefox()
    context.driver.get("https://www.icesi.edu.co/moodle/login/index.php")
    context.login_fb_page = LoginFBPage(context.driver)

@when('the user logs in intu with valid credentials')
def step_when_user_logs_in_valid(context):
    context.login_fb_page.login("user", "user")
    
@then('the user should be redirected to the dashboard page')
def step_then_error_message(context):
    dashboard_page = DashboardPage(context.driver)
    assert dashboard_page.is_top_bar_displayed()

def after_scenario(context, scenario):
    context.driver.quit()
