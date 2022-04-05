from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
sleep(3)

driver.find_element_by_link_text("Register").click()
sleep(2)

driver.find_element_by_id("gender-male").click()
sleep(2)

driver.find_element_by_id("FirstName").send_keys("hello")
sleep(2)

driver.find_element_by_id("LastName").send_keys("world")
sleep(2)

driver.find_element_by_id("Email").send_keys("hello12@gmail.com")
sleep(2)

driver.find_element_by_id("Password").send_keys("pass12345")
sleep(2)

driver.find_element_by_name("ConfirmPassword").send_keys("pass12345")
sleep(2)

driver.find_element_by_id("register-button").click()

































