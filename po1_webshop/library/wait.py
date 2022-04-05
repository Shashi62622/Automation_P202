from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webdriver import WebElement


# driver = Chrome("./chromedriver")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com/")

class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, locator):
        result = super().__call__(locator)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False
def wait(func):
    def wrapper(*args, **kwargs):
        _locator = args[0]
        locator = args[1]
        web_wait = WebDriverWait(_locator.driver, 10)
        web_wait.until(_visibility_of_element_located(locator))
        return func(*args, **kwargs)
    return wrapper