from behave import *
from selenium.webdriver import Chrome

@given('launch chrome browser')
def launch_browser(context):
    context.driver = Chrome(r"C:\Users\DELL\PycharmProjects\Selenium_Training\chromedriver.exe")

@when('open orange hrm homepage')
def open_home_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the logo on page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath("//img[@src='/webres_61eea9f1357e52.82110479/themes/default/images/login/logo.png']").is_displayed()
    assert status is True

@then('close browser')
def close_browser(context):
    context.driver.close()
