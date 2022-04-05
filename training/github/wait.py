from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver import Chrome
from time import sleep


driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("https://github.com/")
sleep(2)


_xpath = "//a[@class='HeaderMenu-link flex-shrink-0 d-inline-block no-underline border color-border-default rounded px-2 py-1']"
driver.find_element_by_xpath(_xpath).click()
sleep(5)

driver.find_element_by_id("email").send_keys("shashikumar626622@gmail.com")
sleep(4)

driver.find_element_by_xpath("(//button[@type='button'])[1]").click()
sleep(2)

driver.find_element_by_id("password").send_keys("shashi62662")
sleep(2)

driver.find_element_by_xpath("(//button[@type='button'])[4]").click()

driver.find_element_by_xpath("//input[@id='login']").send_keys("shashi62662")
sleep(2)

driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
sleep(2)

driver.find_element_by_id("opt_in").send_keys("y")
sleep(2)

driver.find_element_by_xpath("(//button[@type='button''])[6]").click()








