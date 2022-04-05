from requests import request
import json
from selenium.webdriver import Chrome
from time import sleep




# s = "haihelloworld123"
# d = "amountbalance123"
# print(d[8:])
# print(d[-8:])

# driver = Chrome(r"C:\Users\DELL\PycharmProjects\Selenium_Training\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.flipkart.com/")
# sleep(5)
#
#
# driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("shashi")
# sleep(2)
# driver.find_element_by_xpath("//input[@type='password']").send_keys("shashi123")
# sleep(2)
# driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()


def test_title():
    payload = {
        "capabalities": {
            "browserName": "chrome"
        }
    }

    response = request(method="POST", url="https://127.0.01:9515/session", json=payload)
    _response = json.loads(response.text)
    session_id = _response['value']['sessionId']
    print(session_id)




