
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, locator):
        result = super().__call__(locator)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False

def wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        _locator = args[1]
        web_wait = WebDriverWait(instance.driver, 10)
        web_wait.until(_visibility_of_element_located(_locator))
        return func(*args, **kwargs)
    return wrapper
