from selenium import webdriver



driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()

driver.get("www.google.com")