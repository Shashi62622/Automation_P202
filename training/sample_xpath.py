from selenium.webdriver import Chrome
from time import sleep
import csv

# driver = Chrome("./chromedriver")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com/")
# sleep(3)

path = r"C:\Users\DELL\PycharmProjects\Selenium_Training\training\sample file"
def read_csv():
    with open("path") as f:
        reference = {}
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            reference[row[0]] = float([1])
        return reference

driver = Chrome("./chromedriver")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
sleep(3)


reference_price = read_csv()
for product, expected
