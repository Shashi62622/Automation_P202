from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
sleep(3)

driver.find_element_by_css_selector('a[class="ico-register"]').click()
sleep(2)

driver.find_element_by_css_selector('input[value="M"]').click()
sleep(2)

driver.find_element_by_css_selector('input[name="FirstName"]').send_keys("shashi")
sleep(2)

driver.find_element_by_css_selector('input[id="LastName"]').send_keys("kumar")
sleep(2)

driver.find_element_by_css_selector('input[name="Email"]').send_keys("abcd@gmail.com")
sleep(2)

driver.find_element_by_css_selector('input[name="Password"]').send_keys("abc@123")
sleep(2)

driver.find_element_by_css_selector('input[id="ConfirmPassword"]').send_keys("abc@123")
sleep(2)

driver.find_element_by_css_selector('input[id="register-button"]').click()
sleep(2)








