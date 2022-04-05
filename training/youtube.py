from selenium.webdriver import Chrome
from time import sleep

# driver = Chrome("./chromedriver.exe")
driver.maximize_window()
driver.get("https://www.youtube.com/shorts/467Fou_OX6k")
sleep(3)

driver.find_element_by_link_text("Explore").click()
sleep(2)

driver.find_element_by_id("destination-content-root").click()
sleep(2)

driver.find_element_by_xpath("(//yt-formatted-string[@class='style-scope ytd-video-renderer'])[1]").click()

a = 1,230.00
if a == 1230.00:
    print(a)
else:
    print("f")











