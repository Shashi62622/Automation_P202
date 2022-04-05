from selenium.webdriver.support.select import Select
from wait import wait

class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait
    def click_me(self, locator):
        self.driver.find_element(*locator).click()

    @wait
    def enter_text(self, locator, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def select_item(self, locator, value):
        list_box = self.driver.find_element(*locator)
        select = Select(list_box)
        if isinstance(value, str):
            select.select_by_visible_text(value)
        else:
            select.select_by_index(value)