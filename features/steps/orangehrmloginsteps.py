from behave import *
from selenium.webdriver import Chrome

@given('I launch chrome browser')
def launch_browser(context):
    context.driver = Chrome(r"C:\Users\DELL\PycharmProjects\Selenium_Training\chromedriver.exe")


@when('I open orange HRM Homepage')
def go_to_the_url(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter username "{user}" and password "{ped}"')
def enter_parameter(context, user, pwd):
    context.driver.find_elemnet_by_id("txtUsername").send_keys(user)
    context.driver.find_elemnet_by_id("txtPassword").send_keys(pwd)

@when('click on login button')
def click_on_login(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('user must successfully login to the Dashboard page')
def step_impl(context):
    context.driver.close()
