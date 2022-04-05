import time
import re
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = Chrome("./chromedriver.exe")
driver.maximize_window()
driver.get("https://www.goibibo.com/bus/")
sleep(5)

actions = ActionChains(driver)
driver.find_element_by_xpath("//input[@data-testid='openCheckinCalendar']").click()
for _ in range(12):
    try:
        driver.find_element_by_xpath("//p[text()='February 2022']").click()
        break
    except NoSuchElementException:
        driver.find_element_by_xpath("(//div[@class='dcalendarstyles__SliderArrow-sc-r2jz2t-14 ilBEvY'])[2]").click()
        sleep(1)
        continue
try:
    date = driver.find_element_by_xpath("//p[text()='February 2022']/../../..//span[text()='10']").click()
    print(date.text)
except NoSuchElementException:
    print("invalid date")



# driver.find_element_by_xpath("//input[@value='Search']").click()
# sleep(2)
#
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.accept()


# for price in prices:
#     print(price.text)

# driver.find_element_by_link_text("Twitter").click()
# sleep(3)
#
# handels = driver.window_handles
#
# driver.switch_to.window(handels[1])
# sleep(2)
#
# driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("shashi")

# parent = driver.find_element_by_xpath("//img[@alt='The peaks of High Tatras']")
# sleep(2)
#
# dest = driver.find_element_by_id("trash")

# actions.drag_and_drop(parent, dest).perform()

# actions.send_keys(Keys.PAGE_DOWN).perform()
# sleep(5)
#
# actions.send_keys(Keys.PAGE_UP).perform()

# job_search = driver.find_element_by_xpath("//a[text()='Job search']")
# sleep(2)
#
# actions.move_to_element(job_search).perform()
# sleep(2)
#
# jobs_by_skill = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
# sleep(2)
#
# actions.move_to_element(jobs_by_skill).perform()
# sleep(2)




# mens = driver.find_element_by_link_text("Men")
# sleep(2)
# actions.move_to_element(mens).perform()
# sleep(1)
#
# suits = driver.find_element_by_xpath("//a[text()='Suits']")
# sleep(2)
# actions.move_to_element(suits).perform()
# sleep(1)
# driver.find_element_by_xpath("//a[text()='Suits']").click()
# sleep(2)



# driver.find_element_by_xpath("(//div[@class='common-checkboxIndicator'])[17]")
# sleep(2)
#
# prices = driver.find_elements_by_xpath("//span[@class='product-discountedPrice']")
# for price in prices:
#     temp = price.text
#     port = re.findall(r'\d+', temp)
#     actual_price = float(port[0])
#     if actual_price >= 219 and actual_price <= 1164:
#         print("pass")
#     else:
#         print("actual price not in the range of 219 and 1164")




# driver.find_element_by_name("firstname").send_keys("shashi")
# sleep(2)
# driver.find_element_by_name("lastname").send_keys("kumar")
# sleep(2)
# driver.find_element_by_xpath("//input[@value='Male']").click()
# sleep(2)
# driver.find_element_by_name("exp").click()
# sleep(2)
# driver.find_element_by_xpath("//strong[text()='Date:  ']/../..//input[@type='text']").send_keys("21/01/2022")
# sleep(2)
# driver.find_element_by_xpath("//input[@value='Automation Tester']").click()
# sleep(2)







# print(contacts)
    # for i in contacts:
    #             print(i)

# companies = ['TATACONSUM', 'POWERGRID', 'KOTAKBANK']
# # for company in companies:
# #     print(f"{company:>15}", end='')
#
# # while True:
# for company in companies:
#     share_price = driver.find_element("xpath", f"//a[text()='{company}']/../..//td[7]").text
#         # print(f"{share_price:>15}", end='')
#     print(share_price)
