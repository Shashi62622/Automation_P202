from selenium.webdriver import Chrome
from time import sleep
from pytest import fixture

@fixture
def setup():
    driver = Chrome(r"C:\Users\DELL\PycharmProjects\Selenium_Training\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://demowebshop.tricentis.com/")
    sleep(2)
    yield driver
    driver.get_screenshot_as_file("shashi.png")
    driver.close()

