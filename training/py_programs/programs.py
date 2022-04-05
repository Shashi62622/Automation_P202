from collections import Counter
from itertools import islice
import re
from collections import defaultdict
from math import sqrt
import calendar
from itertools import islice
from collections import defaultdict
from selenium.webdriver import Chrome
from time import sleep
from collections import defaultdict
from selenium.webdriver.support.select import Select
import random
import xlrd
import attr
import xlrd
import csv
import os
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
path = r"C:\Users\DELL\PycharmProjects\Selenium_Training\training\sample file"
path1 = r"C:\Users\DELL\PycharmProjects\Selenium_Training\training\sample.txt"
c_path = r"C:\Users\DELL\PycharmProjects\Selenium_Training\new\new.csv"
driver = Chrome(r"C:\Users\DELL\PycharmProjects\Selenium_Training\training\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.amazon.in/")
sleep(5)

driver.find_element_by_id("twotabsearchtextbox").send_keys("books")
sleep(1)
driver.find_element_by_id("nav-search-submit-button").click()
sleep(2)

books = driver.find_elements_by_xpath("//div[@class='a-section']")
for book in books:
    print(book.text)














# sleep(5)
# # sleep(5)
# ele_size = driver.find_element_by_xpath("(//button[@type='submit'])[2]")
# print(ele_size.rect)

# def recusive_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return recusive_fibonacci(n-1) + recusive_fibonacci(n-2)
#
# n_terms = 10
#
# if n_terms < 0:
#     print("invalid input, please input a positive value")
# else:
#     print("fibonacci series")
#     for i in range(n_terms):
#         print(recusive_fibonacci(i))


# def recursive_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))
#
#
# n_terms = 10
#
# # check if the number of terms is valid
# if n_terms <= 0:
#     print("Invalid input ! Please input a positive value")
# else:
#     print("Fibonacci series:")
#     for i in range(n_terms):
#         print(recursive_fibonacci(i))

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
#
# result = fact(5)
# print(result)

# sleep(5)
# ele_size = driver.find_element_by_xpath("(//button[@type='submit'])[2]")
# location = ele_size.location
# print(location)


# driver.switch_to.alert.dismiss()
# driver.find_element_by_name("searchVal").send_keys("shoes")
# sleep(1)
# driver.find_element_by_xpath("//button[@type='submit']").click()
# sleep(2)
# products_name = driver.find_elements_by_id("products")
# item_name = []
# for index, product in enumerate(products_name):
#     if index < 6:
#         item_name.append(product.text)
#
# org_prices = driver.find_elements_by_xpath("//span[@class='orginal-price']")
# original_price = []
# for index, price in enumerate(org_prices):
#     if index < 6:
#         original_price.append(price.text)
#
# dis_price = driver.find_elements_by_xpath("//span[@class='price  ']")
# discount_price = []
# for index, price in enumerate(dis_price):
#     if index < 6:
#         discount_price.append(price.text)
#
# discounts = driver.find_elements_by_xpath("//span[@class='discount']")
# discount_percent = []
# for index, discount in enumerate(discounts):
#     if index < 6:
#         discount_percent.append(discount)
#
# list_all_products = zip(original_price, discount_price, discount_percent)
# # print(list_all_products)
# s = list(list_all_products)
# def Sort_Tuple(s):
#     # reverse = None (Sorts in Ascending order)
#     # key is set to sort using second element of
#     # sublist lambda has been used
#     s.sort(key=lambda x: x[0])
#     return s
#
#
# # Driver Code
#
#
# # printing the sorted list of tuples
# max_price = Sort_Tuple(s)
# print(max_price[-1])

# def read_locator(sheetname):
#     workbook = xlrd.open_workbook("path")
#     worksheet = workbook.sheet_by_name(sheetname)
#     rows = worksheet.get_rows()
#     next(rows)
#
#     return {row[0].value: (row[1].value, row[2].value) for row in rows}

# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         displayed = super().__call__(driver)
#         if isinstance(displayed, WebElement):
#             return displayed.is_enabled()
#         else:
#             return False
#

# l = [[1,2,3],[4,5,6],[7,8,9]]
# for item in l:
#     print(sum(item))

# with open(path1)as file:
#     for index, line in enumerate(file, start=1):
#         print(index, line)

# with open(path1)as file:
#     count_ = 0
#     for line in file:
#         count_ += 1
#     print(count_)

# a = [1, 2, 3, 4, 5]
# print(list(map(lambda item: item ** 2, a)))

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d = {}
# for name in names:
#     if len(name) % 2 == 0:
#         d[name] = len(name)
# print(d)

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# new_list = []
# for name in names:
#     if len(name) % 2 == 0:
#         new_list.append(name)
# print(new_list)

# def anagram(a, b):
#     if sorted(a) == sorted(b):
#         print(True)
#     else:
#         print(False)
# anagram("ate", 'eart')

# l = [1, 2, 3, 4]
# b = lambda a: a ** 2
# s = [b(item) for item in l]
# print(s)


# s = "programmingisfunfortimepass"
# print(list(s[::2]))

# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
#
# for key, value in d.items():
#     if value > 1:
#         print(key, value, end=" , ")

# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# a = ['abc', '123', 'hello', '23']
# for i in a:
#     if i.isnumeric():
#         print(i)

# s = "Sony12India567Pvt2ltd"
# s = re.findall('\d+', s)
#
# toatal = 0
# for i in s:
#     toatal += int(i)
# print(toatal)


# def func(string, flag):
#     if flag:
#         return string[0::2]
#     return string[1::2]
#
#
# print(func("TRACXN", 0))  # Should print RCN
# print(func("TRACXN", 1))  # Should print TAX

# l = [1, 2, 3, 4, 5, 6, 7]
# rev = []
# for i in range(len(l)-1, -1, -1):
#     rev.append(i)
# print(rev)

# def sum(*args):
#     if len(args) > 5:
#         print("greater than 5")
#     else:
#         print("less than 5")
# sum(1, 2, 3, 4, 5, 6)

# def outer(func):
#     def wrapper(*args):
#         res = func(*args)
#         if len(args) > 5:
#             print("more than 5")
#         else:
#             print("less than 5")
#     return wrapper
#
# @outer
# def add(a, b, c, d, e, f):
#     return a + b + c + d + e + f

# print(add(1, 2, 3, 4, 5, 6))

# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# c = set(a)
# d = set(b)
# print(d.difference(c))

# t = ('1', '2', '3', '4')
# print("".join(t))

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# for i, j in d.items():
#     if isinstance(j, str):
#         d[i] = j[::-1]
# print(d)

# s = "python is programming language"
# li_ = s.split()
#
# d = {word: len(word) for word in li_}
# print(max(d.items(), key = lambda item: item[-1]))

# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# for item in items:
#     if items.count(item) > 1:
#         pass
#     else:
#         print(item)

# l = lambda a, b: a + b
# print(l(2, 2))

# sentence = "Hi How are you"
# print(sentence[::-1])
# s = ""
# for i in sentence.split():
#     s = i[::-1] + " " + s
# print(s)


# sentence = "Hi How are you"
# for i in sentence.split():
#     print(i[::-1], end=" ")

# l = ["shashi", 123, "12.6", "vidya"]
# for item in l:
#     if isinstance(item, str):
#         print(item)
#     else:
#         res = str(item)
#         print(res[::-1])

# class Login:
#
#     obj_count = 0
#     def __init__(self):
#         Login.obj_count += 1
#
# l1 = Login()
# Login.obj_count
#
# l2 = Login()
# Login.obj_count

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
# @outer
# def sub(a, b):
#     return a - b
#
# print(sub(5, 10))

# my_string = 'hellohai'
# for i in my_string:
#     if my_string.count(i) > 1:
#         print("-", end="")
#     else:
#         print(i, end="")

# char = input("enter char")
# s = "shashi"
# for i, j in enumerate(s):
#     if char in j:
#         print(i)


# def pal_str(ele):
#     if isinstance(ele, str):
#         print(ele)
#     else:
#         rev = str(ele)
#         print(rev[::-1])
#
# pal_str(123)

# driver = Chrome(r"C:\Users\DELL\PycharmProjects\Selenium_Training\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.google.com/")
# sleep(3)
#
# driver.find_element_by_xpath("//input[@type='text']").send_keys("shashi")

# def last_line(n):
#     with open(path1)as file:
#         line_count =
# with open('sample.txt') as f:
#     line_count = 0
#     for line in f:
#         line_count += 1
#     f.seek(0)
#     lines = islice(f, line_count - n, None)


# n = 5
# m = 10
# with open(path1)as file:
#     for index, line in enumerate(file):
#         if index in range(n, m):
#             print(line)

# n = 3
# with open(path1)as file:
#     for index, line in enumerate(file):
#         if index == n:
#             print(line)

# l = [1, 2, 3]
# l1 = [4, 5, 6]
# print(l+l1)

# s = "Hello welcome to Python"
# for i in s:
#     print(i.swapcase(), end="")


# a = 10
# b = 20
# c = a
# d = b
# print(c, d)


# s = "Hello welcome to Python"
# for i in s:
#     print(ord(i))
# print(s[::2])
# print(",".join(s))

# s = "Hello World"
#
# l = list(s)
# print(l)
# print("".join(l))

# for i in s.split():
#     if i == "World":
#         print("universe")
#     else:
#         print(i)

# s = "haihello"
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)

# c = 0
# for i in s:
#     c += 1
# print(c)
# print(len(s))


# class log:
#     __a = 10
#
#     def display(self):
#         print("private variable", self.__a)
#
# l = log()
# l.display()

# f_path = os.path.join(path, "python.txt")
# print(f_path)
# with open(f_path)as f:
#     for line in f:
#         print(line)
#
# re_path =os.path.relpath(f_path)
# print(re_path)


# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print("this function does squaring of given number")
#         return res
#     return wrapper
#
# @outer
# def sqares(iterable):
#     for i in iterable:
#         print(i**2)
# l = [1, 2, 3]
# sqares(l)



# with open(r'C:\Users\DELL\PycharmProjects\Selenium_Training\new\new.csv', 'r+')as file:
#     r_obj = csv.DictReader(file)
#     w_obj = csv.DictWriter(file, ["a", "b", "result"])
#
#     for row in r_obj:
#         if row["a"] == "shashi":
#             res = row["a"] * 2
#             if res == "shashishashi":
#                 w_obj.writerow({"a": row["a"], "b": row["b"], "result": res})


# st = 'ASD1GD4J5L37K9'
# num = ''
# alpha_= ''
# for i in st:
#     if 'A'<= i <= 'Z' or 'a'<=i <= 'z':
#         alpha_ += i
#     if '0' <= i <= '9':
#         num += i
#
# print(num)
# print(alpha_)








# from selenium import webdriver
# from time import sleep
# driver= webdriver.Chrome(r'C:\Users\DELL\PycharmProjects\Selenium_Training\chromedriver.exe')
# driver.get('https://www.w3schools.com/html/html_tables.asp')
# driver.maximize_window()
# sleep(3)
#
# list_elements = driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr/td[1]")
# k = []
# for i in list_elements:
#     k.append(i.text)
# k.sort()
# print(k)


# with open(r'C:\Users\DELL\PycharmProjects\Selenium_Training\new\file.csv')as file:
#     data = csv.DictReader(file)
#     d = {}
#     for i in data:
#         dd = i
#
# driver = Chrome(r"C:\Users\DELL\PycharmProjects\Selenium_Training\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com/login")
# sleep(5)
#
# driver.find_element_by_id("Email").send_keys("shashi456@gmail.com")
# sleep(1)
# driver.find_element_by_id("Password").send_keys("shashi456")
# sleep(1)
# driver.find_element_by_xpath("(//input[@type='submit'])[2]").click()
# sleep(1)
# driver.find_element_by_link_text("My account").click()
# #
# a = driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/form/div[2]/div[2]//input')
#
# l = []
# for i in a:
#     l += [i.get_attribute("value")]
#
# for i, j in zip(dd, l):
#     if dd[i] == j:
#         print(True)

#################################################################

# with open(r'C:\Users\DELL\PycharmProjects\Selenium_Training\new\file.csv') as f:
#     data = csv.reader(f)
#     d = {}
#     l = next(data)
#     l1 = next(data)
#     for i,j in zip(l,l1):
#         d[i] = j
# print(d)

# driver = Chrome(r"C:\Users\DELL\PycharmProjects\Selenium_Training\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com/login")
# sleep(5)


# driver.find_element_by_id("Email").send_keys("shashi456@gmail.com")
# sleep(1)
# driver.find_element_by_id("Password").send_keys("shashi456")
# sleep(1)
# driver.find_element_by_xpath("(//input[@type='submit'])[2]").click()
# sleep(1)
# driver.find_element_by_link_text("My account").click()
# #
# a = driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/form/div[2]/div[2]//input')
#
# m = []
# for i in a:
#     m += [i.get_attribute('value')]
#
# for i,j in zip(d,m):
#     print(i,j)
#     if d[i] == j:
#         print(True)


###############################################################################
# driver.find_element_by_id("gender-male").click()
# sleep(2)
#
# driver.find_element_by_id("FirstName").send_keys("shashi")
# sleep(2)
#
# driver.find_element_by_id("LastName").send_keys("sam2")
# sleep(2)
#
# driver.find_element_by_id("Email").send_keys("shashi456@gmail.com")
# sleep(2)
#
# driver.find_element_by_id("Password").send_keys("shashi456")
# sleep(2)
#
# driver.find_element_by_id("ConfirmPassword").send_keys("shashi456")
# sleep(1)
# driver.find_element_by_id("register-button").click()
#
# driver.find_element_by_xpath("//input[@type='email']").send_keys("8310604202")
# sleep(5)

# driver.find_element_by_id("Email").send_keys("shashi456@gmail.com")
# sleep(1)
# driver.find_element_by_id("Password").send_keys("shashi456")
# sleep(1)
# driver.find_element_by_xpath("(//input[@type='submit'])[2]").click()
# sleep(1)
# driver.find_element_by_link_text("My account").click()
#
# fname = driver.find_elements_by_id("FirstName")
# if fname.get_attribute("value") == l[0]:
#     print(True)


# import csv
# file = open(r"C:\Users\DELL\PycharmProjects\Selenium_Training\new\file.csv")
# csvreader = csv.reader(file)
# next(csvreader)
# # print(header)
# rows = []
# for row in csvreader:
#     rows.append(row)
# print(rows)
# file.close()

# dd = {i.replace("city", "location"): j for i, j in {"name": "kelly", "city": "bangalore"}.items()}
# print(dd)
# print(d)

# a = list(range(20))
#
# def search(iterable, key):
#     return any(item == key for item in iterable)
#
# print(search(a, 19))


# all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows',
#                 'iOS', 'Google Drive', 'One Drive']

# # Pre-defined products for different companies
# apple_products = {'iPhone', 'Mac', 'iWatch'}
# google_products = {'Gmail', 'Maps', 'Google Drive'}
# msft_products = {'Windows', 'One Drive'}
#
# d = defaultdict(list)
#
# for product in all_products:
#     if product in apple_products:
#         d["apple"].append(product)
#     elif product in google_products:
#         d["google"].append(product)
#     elif product in msft_products:
#         d["msft"].append(product)
# print(d)


# with open(path1)as file:
#     d = defaultdict(int)
#     for line in file:
#         for word in line.split():
#             if word == "world":
#                 d[word] += 1
#     print(d)


# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# for i in items:
#     if isinstance(i, (int, float)):
#         print(i)

# with open(path)as file:
#     d = defaultdict(int)
#     for line in file:
#         for word in line:
#             if word in "aeiou":
#                 d[word] += 1
#             else:
#                 d[word] = 1
#     print(d)


# with open(path1)as file:
#     d = defaultdict(list)
#     for line in file:
#
#         for word in line.split():
#             if word in d:
#                 d[word] += 1
#         print(d)


# driver.find_element_by_xpath("(//div[text()='Primary']/../../../../../../../../../..//span[text()='Praxis Business Sch.'])[2]").click()
# sleep(2)
# driver.save_screenshot(r"G:\New folder\home1")

# driver.find_element_by_id("fname").send_keys("shashi")
# list_box = driver.find_element_by_name("continents")
# select = Select(list_box)
# sleep(3)


# all_options = select.options
#
# for item in all_options:
#     select.select_by_visible_text(item.text)
#
# for i in range(6, 0, -1):
#     print(f'{"* " * i:^12}')


# for i in range(1, 6):
#     for j in range(i, i+i):
#         print(j, end="")
#     print()

# select.select_by_index(random.randint(1, 6))


# def read_lcator(sheetname):
#     workbook = xlrd.open_workbook(path1)
#     worksheet = workbook.sheet_by_name(sheetname)
#     rows = worksheet.get_rows()
#     next(rows)
#     return {row[0].value: (row[1].value, row[2].value) for row in rows}

# read_lcator("loginpage")
# for i in range(1, 10):
#     for j in range(i, i + i):
#         print(j, end="")
#     print()

# for i in range(1, 6):
#     for j in range(i, i+i):
#         print(j, end="")
#     print()

# l = [1, 25, 3, 5, 98]
# a = 0
# for item in l:
#     if item > a:
#         a = item
# print(a)

# print(tuple(range(10)))

# for i in range(2, 50):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)


# n = 4
# for i in range(2, n):
#     if n % i == 0:
#         break
# else:
#     print(n)

# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# un_names = set(names)
# for item in un_names:
    # count = 0
    # for name in names:
        # count += 1
    # if count > 1:
        # print(item)


# s = "This is a Programming language and Programming is fun"
# d = {item: len(item) for item in s.split() if s.count(item) == 1}
# print(d)
#
# res = sorted(d.items(), key=lambda item: item[-1])[-1]
# print(res)
# l = [i for i in range(1, 50) if i % 2 == 0]
# print(l)

# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# for key, value in d.items():
#     if isinstance(value, dict):
#         d[key]["n"] = "net"
# print(d)

# words = ["hi", "hello", "python"]
# print(words[::-1])

# l = [[1,2,3],[4,5,6],[7,8,9]]
# for item in l:
#     print(sum(item))

# with open(path1)as file:
#     for line_num, line in enumerate(file, start=1):
#         print(line_num, line)

# with open(path1)as file:
#     cunt = 0
#     for line in file:
#         cunt += 1
#     print(cunt)

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#
# d = {name: len(name) for name in names if len(name) % 2 == 0}
# print(d)

# d = {}
# for name in names:
#     if len(name) %2 == 0:
#         d[name] = len(name)
# print(d)

# l =[]
# for name in names:
    # if len(name) % 2 == 0:
        # l.append(name)
# print(l)

# a = "eat"
# b = "ase"
# if sorted(a) == sorted(b):
#     print("anagrams")

# l = [1, 2, 3, 4, 5]
# res = list(map(lambda item: item ** 2, l))
# print(res)

# s = "hai hello worls"
# l = []
# for item in s[::2]:
#     l.append(item)
# print(l)

# l = [c for c in s[::2]]
# print(l)

# s  = "hai hello world"
# d = defaultdict(int)
# for c in s:
#     d[c] += 1
# for key, value in d.items():
#     if value > 1:
#         print(key, value)

# d = {}
# for item in s:
#     if s.count(item) > 1:
#         d[item] = 1
#     else:
#         d[item] += 1
# print(d)

# s  = "hai hello world"
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# a = ['abc', '123', 'hello', '23']
# for item in a:
#     if item.isnumeric():
#         print(item)

# s = "Sony12India567Pvt2ltd"
# total = 0
# res = re.findall(r'[\d]+', s)
# for item in res:
#     total += int(item)
# print(total)


# total = 0
# res = re.findall(r'\d', s)
# for item in res:
#     total += int(item)
# print(total)


# def rev(a):
#     l = ""
#     for item in a:
#         l = item + " " + l
#     print(l)
#
# rev(["avbc", "sjg"])

# def log(func):
#     def wrapper(*args, **kwargs):
#         if len(args) > 5:
#             print("num of pos args is geter tan 5")
#         else:
#             print("num of pos agr is less tha 5")
#         func(*args, **kwargs)
#     return wrapper
# @log
# def add(a, b, c, d, e, f):
#     return a + b + c + d + e + f

# add(1, 2, 3, 4, 5, 6)

# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# c = set(a)
# d = set(b)
#
# print(d.difference(c))

# t= ('1', '2', '3', '4')
# print("".join(t))

# d = {"a": "hello", "b": 25}
# dd = {}
# for key, value in d.items():
    # if isinstance(value, str):
        # dd[key] = value[::-1]
    # else:
        # dd[key] = value
# print(dd)

# s = "hai welcme to programming"
# l = s.split()
# res = sorted(l, key=len)
# print(res[-1])

# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# for item in items:
#     if items.count(item)== 1:
#         print(item)

# res = lambda a, b: a+ b
# print(res(2, 2))


# s = "hi hello how are you"
# l = ""
# for item in s.split():
#      l = item[::-1]+ " " + l
#
# print(l)
# for item in s.split():
    # print(item[::-1], end=" ")

# class Sample:
#
#     def __init__(self, item):
#         self.item = item
#
#     def __iter__(self):
#         return iter(self.item)
#
# s = Sample([1, 2, 3, 5, 5])
# for i in s:
#     print(i)

# def rev_int(list_):
#     for item in list_:
#         if isinstance(item, str):
#             print(item)
#         else:
#             res = str(item)
#             print(res[::-1])
# rev_int(["hai", "hello", 25, 658])

# class Login:
#     count = 0
#     def __init__(self):
#         Login.count += 1

# l = Login()
# l1 = Login()
# print(Login.count)

# def log(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
# @log
# def sub(a, b):
#     return a - b
# print(sub(5, 10))

# s = "haihello"
# for i in s:
#     if s.count(i) > 1:
#         print("-", end="")
#     else:
#         print(i, end="")


# sentence = "hello world welcome to python programming hi there"

# d = defaultdict(list)
# words = sentence.split()
# for word in words:
#    d[word[0]].append(word)

# d = defaultdict(list)
# words = sentence.split()
# for word in words:
#     d[word[0]].append(word)
# print(d)

# s = "hai hello"
# ch = "i"
# for i, j in enumerate(s):
#     if j == ch:
#         print(i)


# n = "mon"
# if n[::-1] == n:
#     print("pal")

# def ran(n, m):
#     with open(path1)as file:
#         for index, line in enumerate(file):
#             if index in range(n, m):
#                 print(line)
#
# ran(5, 10)

# n = 3
# with open(path1) as file:
#     for index, line in enumerate(file):
#         if index == n:
#             print(line)


# l = [1, 2, 3, 4]
# l1 = [2, 5, 6, 6]
# l3 = l + l1
# print(l3)

# s = "hai hello"
#
# print(s[::2])

# l = list(s)
# print(l)
# print("".join(l))

# s = "hello world"
# for i in s.split():
#     if i  == "world":
#         print("universe", end="")
#     else:
#         print(i, end=" ")


# s = "hai hello"
# l = list(s)
# # print(l)
# reversed(l)
# print(l)
# print("".join(l))

# rev = ""

# s = "hai"
# l = 0
# for i in s:
#     l += 1
# print(l)

# # driver.save_screenshot(r"G:\New folder\homepage1.png")
# driver.get_screenshot_as_file(r"G:\New folder\homepage2.png")
#
# numbers = [9945377190, 8310604202, 7406702660]
#
# def add_prefix(number):
#     if len(str(number)) == 12 and str(number).startswith("91"):
#         return "+" + str(number[:2]+ "-" + str(number)[2:])
#     elif len(str(number)) == 10:
#         return "91+" + str(number)
#     else:
#         return number

# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         numbers = args
#         prefix_numbers = ["+91"+str(numbers) for number in numbers]
#         return func(prefix_numbers)
#     return wrapper
# #
# @prefix_country_code
# def print_numbers(numbers):
#     for number in numbers:
#         print(number)
#
# print(print_numbers(numbers))


# def max_calls(func):
#     func.count = 0
#     def wrapper(*args, **kwargs):
#         func.count += 1
#         if func.count > 5:
#             raise ValueError(f"cannot call {func.__name__} more than 5 times")
#         return func(*args, **kwargs)
#     return wrapper
#
# @max_calls
# def greet():
#     return "hello world"
#
# @max_calls
# def grett():
#     return 10
#
# print(greet())
# print(greet())
# print(greet())
# print(greet())
# print(greet())
# print(greet())
# print(grett())


# a = 10
# def mul(b, a=a):
#     return a * b
# a = 20
#
# result = mul(10)
# print(result)

# count = 0
# for i in range(1, 10):
#     count += 1
#     print(i, end="")
#     if count == 3:
#         print()
#         count = 0


# links = driver.find_elements_by_xpath("//a")
#
# for link in links:
#     print(link.get_attribute("href"))
# def last(n):
#     print(n[::-1])
# last([123])

# l = [1, 7, 8, 6, 5, 9, 12]
# n = 0
# for i in l:
#     if i > n:
#         n = i
# print(n)

# print(tuple(str(10)))

# t = [i for i in range(0, 10)]
# print(tuple(t))

# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             print("not a prime")
#             break
#     else:
#         print("prime")
# prime(6)

# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# d = {}
# for name in names:
#     if name in d:
#         d[name] += 1
#     else:
#         d[name] = 1
# print(d)

# l = ["abc", 2, 5, "abc", 5]
# li = []
# for i in l:
#     if l.count(i) == 1:
#         li.append(i)
# print(li)


# s = "python is a programming language of my heart"

# l = {word: len(word) for word in s.split() if s.count(word) == 1}

# d = sorted(l.items(), key=lambda item: item[-1])[-1]
# print(d)
# d = sorted(l.items(), key=lambda item: item[-1])[-1]
# print(d)


# l = [i for i in range(1, 50) if i % 2 == 0]
# print(l)

# with open(path1)as file:
#     count = 0
#     for lines in file:
#         for line in lines:
#             if line == " ":
#                 count += 1
#     print(count)

# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# for key, item in d.items():
#     if isinstance(item, dict):
#         d[key]['n'] = "net"
# print(d)

# words = ["hi", "hello", "python"]
# print(words[::-1])

# res = reversed(words)
# print(list(res))

# l = [[1,2,3],[4,5,6],[7,8,9]]
# li = []
# for item in l:
#     li.append(sum(item))
#
# print(li)


# with open(path1) as file:
#     for index, line in enumerate(file, start=1):
#         print(index, line)


# lines = """CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical"""

# count = 0
# with open(path1)as file:
#     for line in file:
#         count += 1
# print(count)

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# l = [name for name in names if len(name) % 2 == 0]
# print(l)

# d = {name: len(name) for name in names if len(name) % 2 == 0}
# print(d)

# l =[]
# for item in names:
#     if len(item) % 2 == 0:
#         l.append(item)
# print(l)

# a = [5, 2, 3]
# a.sort()
# print(a)

# def anagram(a, b):
#     if sorted(a) == sorted(b):
#         print("anag")
#     else:
#         print("false")
# anagram("eat", "ae")

# def anagram(a, b):
#     if  == sorted(b):
#         print("anagrams")
#
# anagram("eat,", "ate")

# l = [1, 2, 3, 4, 5, 6]
# res = list(map(lambda a: a ** 2, l))
# print(res)

# s = "hai hello how are you"
# print(list(s[::2]))

# d = defaultdict(int)
# for i in s:
#     d[i] += 1
# for key, value in d.items():
#     if value > 1:
#         print(key, ":", value, end=",")

# s = "hai hello how are you"
#
# d = defaultdict(int)
# for i in s:
#     d[i] += 1
# print(d)

# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# a = ['abc', '123', 'hello', '23']
# for i in a:
#     if i.isnumeric():
#         print(i)

# s = "Sony12India567Pvt2ltd" # eg.12+567+2
#
# res = re.findall(r'[\d]+', s)
# total = 0
# for item in res:
#     total += int(item)
# print(total)

# s = "Sony12India567Pvt2ltd"
# res = re.findall(r'[\d]', s)
# totl = 0
# for item in res:
#     totl += int(item)
# print(totl)


# def rev(string, float):
#     if float:
#         return string[0::2]
#     return string[1::2]
#
# print(rev("TRACXN", 0))  # Should print RCN
# print(rev("TRACXN", 1))  # Should print TAX

# l = [1, 2, 3, 4, "abc"]
# li = []
# for i in range(len(l)-1, -1, -1):
#     li.append(l[i])
# print(li)

# dd = defaultdict(int)
# for line in lines.split():
#     word = line.strip().split(":")
#     dd[word[0]] += 1
# print(dd)

# def log(*args):
#     if len(args) > 5:
#         print("number of positional args are greater than 5")
#     else:
#         print("number of positional args are less than 5")
#
# log(1, 2, 3, 4, 5, 6)


# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# c = set(a)
# d = set(b)
#
# print(d.difference(c))

# s = ("1", "2", "3", "4")
# print("".join(s))

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
#
# dd = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(dd)

# dd = {}
# for key, value in d.items():
#     if isinstance(value, str):
#         dd[key] = value[::-1]
#     else:
#         dd[key] = value
# print(dd)


# s = "hai hello welocome to python programming"
# list = s.split()
# b = sorted(list, key=len)
# print(b[-1])

# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# unique = []
# for item in items:
#     if item not in unique:
#         unique.append(item)
# print(unique)

# s = lambda a, b: a + b
# print(s(1, 2))


# sentence = "Hi How are you"
# s = ""
# for item in sentence.split():
#     s = item[::-1] + " " + s
# print(s)


# for item in sentence.split():
#     print(item[::-1], end=" ")

# class Login:
#
#     count = 0
#     def __init__(self):
#         Login.count += 1
#
# c = Login()
# print(Login.count)
# b = Login()
# print(Login.count)
# d = Login()
# print(Login.count)


# def res(list_):
#     for item in list_:
#         if isinstance(item, str):
#             print(item)
#         else:
#             temp = str(item)
#             print(temp[::-1])
# res(["hai", 23, "12.5", 56])

# def log(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
# @log
# def sub(a, b):
#     return a - b
# print(sub(2, 5))


# my_string = 'hellohai'
# for i in my_string:
#     if my_string.count(i) > 1:
#         print("-", end="")
#     else:
#         print(i, end="")

# sentence = "hello world welcome to python programming hi there"
# d = defaultdict(list)
# for word in sentence.split():
#     d[word[0]].append(word)
# print(d)
# def nthline(n):
#     coutn = 0
#     with open(path1) as file:
#         for line in file:
#             coutn += 1
#             file.seek(0)
#             lines = islice(file, coutn-n, None)
#             print(list(lines))
# nthline(1)

# def rand(n, m):
#     with open(path1)as file:
#         for line, item in enumerate(file):
#             if line in range(n, m):
#                 print(item)
# rand(5, 10)

# def ran_read(n):
#     with open(path1) as file:
#         for line, item in enumerate(file):
#             if line == n:
#                 print(item)
#
# ran_read(5)
# n = 3
# with open(path)as file:
#     for line, item in enumerate(file):
#         if line == n:
#             print(item)

# l = [1, 2, 3]
# l2 = [4, 5, 2, "hai"]
# print(*l, *l2)

# a = 10
# b = 15
# b, a = a, b
# print(b, a)

# s = "hAi hElLo"
# print(s.swapcase())

# for i in s:
#     print(ord(i))

# print(s[::2])

# s = "hello welcome to python0"
# print(",".join(s))
# l = s.split()

# print(",".join(l))

# s = "hai heloo how are you"
# l = list(s)
# print(l)
# print("".join(l))

# s = "hello world"
# c = ""
# for i in s.split():
#     if i == "world":
#         print("universe")
#     else:
#         print(i, end=" ")

# s = "hai hello how are you"
# l = ""
# for i in s.split():
#     l = i + " " + l
# print(l)
# print(len(s))
# c = 0
# for i in s:
#     c += 1
# print(c)

# def read_locator(sheetname):
#     workbook = xlrd.open_workbook("path")
#     worksheet = workbook.sheet_by_name(sheetname)
#     rows = worksheet.get_rows()
#     next(rows)
#     locators = {row[0].value: (row[1].value, row[2].value) for row in rows}
#     return locators

# def read_locators(sheetname):
#     workbook = xlrd.open_workbook("path")
#     worksheet = workbook.sheet_by_name(sheetname)
#     rows = worksheet.get_rows()
#     next(rows)
#     locators = {row[0].value: (row[1].value, row[2].value) for row in rows}
#     return locators

# n = 10
# first = 0
# second = 1
# count = 1
# while count < n:
#     print(first)
#     third = first + second
#     first = second
#     second = third
#     count += 1

# n = 10
# first = 0
# second = 1
# count = 1
# while count <= n:
#     print(first)
#     third = first + second
#     first = second
#     second = third
#     count += 1

# l = [1, 3, 6, 8, 7.5, 10, 7]
#
# for i in range(3):
#     s = 0
#     for j in l:
#         if j>s:
#             s=j
#     l.remove(s)
# print(s)


# for i in range(3):
#     a = 0
#     for j in l:
#         if j>a:
#             a=j
#     l.remove(a)
# print(a)

# def prime(n, m):
#     for i in range(n, m):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
#
# prime(5, 50)

# n = 6
# for n in range(1, 50):
#     for i in range(2, n):
#         if n % i == 0:
#             # print("not a prime")
#             break
#     else:
#         print(n)


# word1 = 'hello 1 2 3 4 5'
# word2 = 'world 5 6 7 8 9'
#
# num1 = re.findall(r'\d', word1)
# num2 = re.findall(r'\d', word2)
# total = []
# for n1, n2 in zip(num1, num2):
#     total.append(int(n1) + int(n2))
# print(total)

# sentence = 'hello 123 world 567 welcome to 9724 python'
#
# numbers = re.findall(r'\d', sentence)
#
# digits = [int(number) for number in numbers]
# print(digits)
#
# evens = [digit for digit in digits if digit % 2 == 0]
# print(evens)

# s = 'hello world hi hello universe how are you happy birthday'
# print(re.findall(r'\bh\w+', s))

# print("bangaluru \n" * 10)

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
#
# d = defaultdict(list)
# for index, item in enumerate(names):
#     d[item].append(index)
# print(d)
# numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
# for number in numbers:
    # match = re.findall(r'5$', number)
    # if match:
        # print(number)

# s = "python@#$%pool"
# print(re.findall(r'\w+', s))

# numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]
# sum_sorted = sorted(numbers)
#
# max_sum = sum(sum_sorted[-3:])
# print(max_sum)
#
# min_sum = sum(sum_sorted[:3])
# print(min_sum)
# with open(path1) as file:
#     with open('pyhthon.text', 'a') as pf:
#         for lines in file:
#             new_line = re.sub("java", "python", lines)
#             pf.write(new_line)

# sentence = "hello world welcome to python"
#
# print(re.sub(r'[aeiou]', "*", sentence))

# sentence = "Hello world welcome to python"

# print(re.sub(r'\s', '\n', sentence))

# def len_iter(*iterable):
#     total = 0
#     for item in iterable:
#         total += len(item)
#     return total
#
# print(len([1, 2, 30]))

# class Parent:
#
#     @staticmethod
#     def demo(self):
#         print("in parent")
#
# class Child(Parent):
#
#     @staticmethod
#     def demo(self):
#         print("in clild")
# c = Child()
# c.demo("hai")
# sentence = '0-0, 4-8, 20-20, 43-45'
# word = sentence.split(',')
# words = []
# for item in word:
#     start, end = item.split('-')
#     for i in range(int(start), int(end)):
#         words.append(i)
# print(words)

# sentence = "hello world hi apple you yahoo to you"
# max_word = max(sentence.split(), key=len)
#
# max_of_all_words = [word for word in sentence.split() if len(word) == len(max_word)]
# print(max_of_all_words)

# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# max_number = max(numbers)
# max_of_all_numbers = [number for number in numbers if number == max_number]
# print(max_of_all_numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# d = defaultdict(list)
# for item in numbers:
#     if item % 2 == 0:
#         d[0].append(item)
#     else:
#         d[1].append(item)
# print(d)

# sentence = "Hi there! How are you:) How are you doing today!"

# word = re.findall(r'\b\w+', sentence.lower())
# print(Counter(word))
# s = "hai hello how are you"
# print(Counter(s.split()))

# s = '@hello12world34welcome!123'
# for i in s:
#     if not i.isdigit():
#         print(i, end="")


# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
# d = defaultdict(list)
# for file in files:
#     file, product = file.split(".")
#     d[product].append(file)
#
# print(d)

# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
# d = defaultdict(list)
# for item in items:
#     item, group = item.split("-")
#     d[group].append(item)
# print(d)

# s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
# d = defaultdict(int)
# for item in s:
#     if item.isalpha():
#         d[item] += 1
# print(d)


# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# evenes = [item for item in a if item % 2 == 0]
# odds = [item for item in a if item % 2 != 0]
# evenes.sort()
# odds.sort()
#
# odds_evens = [*odds, *evenes]
# print(odds_evens)


# for n in range(1, 50):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n)

# for i in range(1, 50):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# sentence = "hello world welcome to python hello hi how are you hello there"
# def indext_nth_occur(sentence, pat, n):
#     matches = re.finditer(pat, sentence)
#     count = 0
#     for match in matches:
#         count += 1
#         if count == n:
#             return f"start index {match.start()}, end index {match.end()}"
#
# print(indext_nth_occur(sentence, "hello", 2))


# def index_nth_occurance(sentence, pat, n):
#     matches = re.finditer(pat, sentence)
#     # print(matches)
#     _count = 0
#     for match in matches:
#         _count +=1
#         if _count == n:
#             return f"Start Index: {match.start()}, End Index: {match.end()}"
#
# print(index_nth_occurance(sentence, "hello", 3))
# s = "welcome to python programming"
# for i in s:
#     if s.count(i) > 1:
#         print(i)
#         break

# a = [1, 2, 3]
# b = (4, 5, 6)
# a.extend(b)
# print(a)
#
# c = {7, 8, 9}
# a.extend(c)
# print(a)
#
# d = {'a': 1, 'b': 2, 'c': 3}
# a.extend(d)
# print(a)
# a = [10, 12, 14, 16, 18]
# b = [20, 22, 24, 26, 28]
#
# a = [0, 5, 10, 15]
# b = [20, 25, 30, 35, 40]
#
# x = [10, 20, 30, 40]
# y = [50, 40, 60, 70]
#
#
#
# def _series(iter1, iter2):
# # Get the difference of the series
#     diff = a[1]-a[0]
#     print(diff)
#     # Combine both the lists
#     c = iter1 + iter2
#     return all([True if c[i] + diff ==  c[i+1] else False for i in range(0, len(c)-1)])
# print(_series(a, b))

# s = "Hai hEllO hoW Are"
# for i in s:
#     if i == i.upper():
#         print(i, end=" ")

# s = list(range(21))
# print(s)
# def _search(iterable, key):
#     return any(item == key for item in iterable)
#
# print(_search(s, 21))
# print(calendar.isleap(2020))

# with open(path1)as file:
#     for line in file:
#         if line[0] == "#":
#             print(line)

# s = "hai hello world welcome to python"
# for i in s:
#     if i not in "aeiou":
#         print(i, end=" ")
#
# l = [i for i in s if i not in "aeiou"]
# print(l)

# for i in s:
#     if s.count(i) == 1:
#         print(i, end=" ")

# count = 0
# for i in s:
#     if i == " ":
#         count += 1
# print(count)

# s = "hai hello world"

# def rotate(s, n):
#     s = list(s)
#     for _ in range(n):
#         f = s.pop()
#         f.insert(2, f)
#         return "".join(s)
#
# print("hai hello world", 1)


# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# def rotate(iterable, n):
#     for _ in range(n):
#         f = iterable.pop()
#         iterable.insert(1, f)
#     return iterable
#
# print(rotate(names, 1))


# all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows',
#                 'iOS', 'Google Drive', 'One Drive']
# # Pre-defined products for different companies
# apple_products = {'iPhone', 'Mac', 'iWatch'}
# google_products = {'Gmail', 'Maps', 'Google Drive'}
# msft_products = {'Windows', 'One Drive'}
#
# d = defaultdict(list)
# for product in all_products:
#     if product in apple_products:
#         d["apple"].append(product)
#     elif product in google_products:
#         d["google"].append(product)
#     elif product in msft_products:
#         d["msft"].append(product)
#
# print(d)
# d = defaultdict(list)
# for product in all_products:
#     if product in apple_products:
#         d["apple p"].append(product)
#     elif product in google_products:
#         d["google p"].append(product)
#     elif product in msft_products:
#         d["msft"].append(product)
#
# print(d)
# with open(path1) as file:
#     words = 0
#     for line in file:
#         for word in line.split():
#             if word == "world":
#                 words += 1
#     print(words)

# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# for item in items:
#     if isinstance(item, (int, float)):
#         print(item)

# with open(path1) as file:
#     count = 0
#     for line in file:
#         for i in line:
#             if i in "aeiou":
#                 count += 1
#     print(count)

# with open(path1) as file:
#     d = {}
#     for line in file:
#         for word in line.split():
#             if word in d:
#                 d[word] += 1
#             else:
#                 d[word] = 1
#     print(d)

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# d = {}
#
# for name in names:
#     if name in d:
#         d[name] += 1
#     else:
#         d[name] = 1
# print(d)
# def if_perfect_sqr(num):
#     return num == sqrt(num) ** 2
#
# print(if_perfect_sqr(25))

# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
# ]
# d = {}
#
# for word in words:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1
# print(d)
#
# l = sorted(d.items(), key=lambda item: item[1])
# print(l[-1])

# def last_digit(num):
#     return int(num[-1])
#
# print(last_digit("1234"))


# l = [10, 20, 30, 50, 40]
# l.sort()
# print(l[-1])
# largest = 0
# for item in l:
#     if item > largest:
#         largest = item
# print(largest)
# largest = 0
# for item in l:
#     if item > largest:
#         largest = item
# print(largest)

# print(tuple(range(10)))

# def prime(num):
#
#     return not any([num % 2 == 0 for i in range(2, num)])
#     # return not any([num % 2 == 0 for i in range(2, num)])
#
# print(prime(5))
# def prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#         else:
#             return "prime"
# print(prime(5))

# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# d = {}
# for name in names:
#     if name in d:
#         d[name] += 1
#     else:
#         d[name] = 1
# print(d)

# l = ["sha", "shi", 1, 2, 1, "the", "sha"]
#
# for item in l:
#     if l.count(item) > 1:
#         print(item)

# s = "This is a Programming language and Programming is fun"

# d = {sub: len(sub) for sub in s.split() if s.count(sub) == 1}

# d = {sub: len(sub) for sub in s.split() if s.count(sub) == 1}
# print(d)

# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
#
# d = defaultdict(list)
# for word in words:
#     s = "".join(sorted(word))
#     d[s].append(word)
# print(d)
# d = defaultdict(list)
# for word in words:
# 	s = ''.join(sorted(word))
# 	d[s].append(word)
# print(d)

# l = [i for i in range(1, 50) if i % 2 == 0]
# print(l)
# white_space = 0
# with open(path) as file:
#     for line in file:
#         match = re.findall(r'\s', line)
#         if match:
#             white_space += 1
# print(white_space)

# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# print(d.get('b'))
# for key, value in d.items():
#     if isinstance(value, dict):
#         d[key]['n'] = 'net'
# print(d)


# a = (1, 2, 3, 4)
# b = (4, 5, 6)
# c = a + b
# print(c)

# l = [3, 5, -4, 8, 11, 1, -1, 6]
# l.sort()
# print(l)
# print(l[-2])

# 1. Write a program to find the length of the string without using inbuilt function
# string_ = "hello world"
#
# count = 0
# for item in string_:
#     count += 1
# print(count)
#
# print(len(string_))
#
# def length(a):
#     return len(a)
#
# print(length("hello world"))


# 2. Write a program to reverse a string without using any inbuilt functions.
# string_ = "hello world"
# s = ""
# for item in string_:
#     s = item + s
# print(s)
#
# def reverse(stringg):
#     temp = []
#     for i in range(len(stringg)-1, -1, -1):
#         temp.append(stringg[i])
#     return "".join(temp)
# #
# print(reversed("hai hello"))
#
# print(reverse("helloworld"))

# 3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".

# word = "hello world"
# print(word.replace("world", "universe"))

# 4. How to convert a string to a list and vice-versa
# string_ = "hello world"
# list_ = string_.split()
# print(list_)
#
# strr = "".join(list_)
# print(strr)

# s = "Hello welcome to Python"
# print(",".join(s))
#
# a = s.split()
#
# print(",".join(a))

# s = "Hello welcome to Python"
# print(s[::2])

# def alter(a):
#     print(a[::2])
# alter("shashi")
#
# s = "Hello welcome to Python"
# for ch in s:
#     print(ord(ch))

# s = "Hello welcome to Python"
#
# print(s.swapcase())
#
# a = 10
# b = 20
#
# a, b = b, a
#
# print(b, a)

# a = [1, 2, 3]
# b = [3, 4, 5]
#
# print(*a, *b)
# print(a + b)

path = r"C:\Users\DELL\PycharmProjects\Selenium_Training\training\files\smart_prices.csv"
# line_num = 7
# with open(path) as file:
#     for index, item in enumerate(file, start=1):
#         if index == line_num:
#             print(item)

# def random_line(num):
#     with open(path) as file:
#         for index, item in enumerate(file):
#             if index == num:
#                 print(item)
# random_line(5)
# def rand_line(start_line, end_line):
#     with open(path) as file:
#             a = islice(file, start_line, end_line)
#             for line in a:
#                 print(line)
#
# rand_line(5, 10)


# with open(path) as file:
#     n = 1
#     count_ = 0
#     for line in file:
#         count_ += 1
#         file.seek(0)
#         lines = islice(file, count_-n, None)
#         print(list(lines))

# s = "hai hello"
# ch = input("enter chr"
# for index, item in enumerate(s):
#     if item == ch:
#         print(ch, index)


sentence = "hello world welcome to python programming hi there"

# from collections import defaultdict
#
# dd = defaultdict(list)
#
# words = sentence.split()
# print(words)
# for word in words:
#     print(word)
#     dd[word[0]].append(word)
# print(dd)
#
# d = {}
#
# for word in sentence.split():
#     if word in d:
#         d[word[0]] += word
#     else:
#         d[word[0]] = word
#
# print(d)
# pat = ""
# for i in range(1,6):
#     pat += str(i)
#     print(f'{pat:6}')







