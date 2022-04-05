import csv

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from pytest import fixture

# @fixture(scope="session")
# def fix_session():
#     print("\n running setup SESSIoN scope")
#     yield
#     print("\n running teardown Session scope")
#
# @fixture(scope="module")
# def fix_mod():
#     print("\n running setup module scope")
#     yield
#     print("\n running teardown module scope")



# driver = Chrome("./chromedriver")
# driver.maximize_window()
# driver.get("https://www.monsterindia.com/")
# sleep(3)





# driver.find_element_by_id("SE_home_autocomplete").send_keys("python")
# sleep(2)
#
# driver.find_element_by_css_selector("input[value='Search']").click()
# sleep(3)
#
# driver.find_element_by_xpath("(//a[text()='Python Developer'])[1]").click()
# sleep(2)
#
# handles = driver.window_handles
# sleep(1)
#
# driver.switch_to.window(handles[1])
# sleep(2)
#
# driver.find_element_by_xpath("(//button[text()='APPLY'])[1]").click()

# driver.find_element_by_link_text("Twitter").click()
# sleep(5)
#
# window_id = driver.window_handles
# print(window_id)
#
# sleep(3)
# driver.switch_to.window(window_id[1])
#
# driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("shashi")

# images = driver.find_element_by_xpath("//img")
# for image in images:
#     print(image.get_attribute("alt"))
#     sleep(1)

# list_box = driver.find_element_by_id("standard_cars")
#
# seletc = Select(list_box)
#
# seletc.select_by_visible_text("Land Rover")
# sleep(2)
#
# first_selected_item = seletc.first_selected_option.text
# print(first_selected_item)

# list_box = driver.find_element_by_id("multiple_cars")
# select = Select(list_box)
# select_all = select.options
#
# for item in select_all:
#     select.select_by_visible_text(item.text)
#     sleep(2)

# list_box = driver.find_element_by_id("standard_cars")
# select = Select(list_box)
#
# select.select_by_visible_text("Mercedes")
# sleep(2)
#
# select.select_by_visible_text("Honda")
# sleep(2)
#
# select.select_by_index(2)
# sleep(2)
#
# select.select_by_index(6)
# sleep(2)
#
# select.select_by_value("jgr")
# sleep(2)
#
# select.select_by_value("nin")
# sleep(2)


# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         display = super().__call__(driver)
#         if isinstance(display, WebElement):
#             return display.is_enabled()
#         else:
#             return False

# wait = WebDriverWait(driver, 10)
# wait.until(visibility_of_element_located(("name", "fname")))
#
# driver.find_element_by_name("fname").send_keys("hello")

# wait = WebDriverWait(driver, 10)
#
# wait.until(visibility_of_element_located(("name", "fname")))
#
# driver.find_element_by_name("fname").send_keys("hello")


# driver.get("https://www.flipkart.com/search?q=smartphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_15_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_15_na_na_ps&as-pos=2&as-type=HISTORY&suggestionId=smartphone%7CMobiles&requestId=80b6d186-7a1d-4750-9bd3-9d2765fac1b2")
# sleep(5)
#
# driver.find_element_by_xpath("//div[text()='POCO M3 (Yellow, 64 GB)']/../../..//div[@class='_24_Dny']").click()

#  //div[text()='POCO M3 (Yellow, 64 GB)']/../../..//div[@class='_24_Dny']

# links_ = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//a")
# for link in links_:
#     print(link.text)
#     sleep(2)

# driver.find_element_by_id("twotabsearchtextbox").send_keys("mi mobiles")
# sleep(2)
# driver.find_element_by_id("nav-search-submit-button").click()
# sleep(2)
# names_of_mobiles = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
# for names in names_of_mobiles:
#     print(names.text)
#     sleep(2)

# def read_csv():
#     with open("./files/prices.csv") as f:
#         references = {}
#         rows = csv.reader(f)
#         next(rows)
#         for row in rows:
#             references[row[0]] = float(row[1])
#         return references
#
# expected_prices = read_csv()
# print(expected_prices)
#
# for product, expected_price in expected_prices.items():
#     actual_price = driver.find_element_by_xpath(f"//a[text()='{product}']/../..//span[@class='price actual-price']").text
#     sleep(2)
#     if expected_price == float(actual_price):
#         print("pass")
#     else:
#         print("fail")




# expected_prices = {
#                     "$25 Virtual Gift Card": 25.00,
#                     "14.1-inch Laptop": 1590.00,
#                     "Build your own cheap computer": 800.00,
#                     "Build your own computer":1200.00,
#                     "Build your own expensive computer": 1800.00,
#                     "Simple Computer": 800
#                     }
# for gadget, expected_price in expected_prices.items():
#     actual_price = driver.find_element_by_xpath(f"//a[text()='{gadget}']/../..//span[@class='price actual-price']").text
#     if float(actual_price) == expected_price:
#         print("pass")
#     else:
#         print("fail")

# expected_prices = {"Computing and Internet": 10.00, "Science": 51.00, "Health Book": 10.00}
#
# for book, expected_price in expected_prices.items():
#     driver.find_element_by_link_text("Books").click()
#     actual_price = driver.find_element_by_xpath(f"//a[text()='{book}']/../..//span[@class='price actual-price']").text
#     if float(actual_price) == expected_price:
#         print("pass")
#     else:
#         print("fail")

# ratings = ["Excellent", "Good", "Poor", "Very bad"]
# for rating in ratings:
#     driver.find_element_by_xpath(f"//label[text()='{rating}']/..//input[@type='radio']").click()
#     sleep(2)


# books = ["Computing and Internet", "Fiction", "Health Book"]
# #
# for book in books:
#     driver.find_element_by_xpath(f'//a[text()="{book}"]/../..//input[@value="Add to cart"]').click()
#     sleep(2)
#
# for book in books:
#     driver.find_element_by_link_text("Shopping cart").click()
#     sleep(2)
#
#     driver.find_element_by_xpath(f"//a[text()='{book}']/../..//input[@type='checkbox']").click()
#     driver.find_element_by_name("updatecart").click()

























