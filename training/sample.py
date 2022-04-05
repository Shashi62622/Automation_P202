# a = 4
# pat = []
# for _ in range(1):
    # print("[")
#     for i in range(1, a+1):
#
#         pat.append(i)
#         print(pat)
# print("]")
l = [1, 2, 3, 4]
for i in l:
    if len(l) % 2 == 0:
        l.remove(l[len(l) // 2 + 1])
    else:
        l.remove(l[len(l) // 2 + 0.5])
print(l)
# a = 4
# b = 1
# if a + 2 == b:
#     print(a)
#     print("we can make a and b equal by adding 2 to a in one step")
# elif b + 2 == a:
#     print(b)
#     print("we can make a and b equal by adding 2 to b in one step")
# else:
#     print(1)
#     print("we can not make a and b equal by adding 2 to a or b in one step")




































# driver = webdriver.Chrome("./chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.ajio.com/")
# sleep(5)
#
# driver.find_element_by_xpath("//input[@type='text']").send_keys("shoes")
# sleep(1)
#
# driver.find_element_by_xpath("//span[@class='ic-search']").click()
# sleep(2)

# brand_names = driver.find_elements_by_xpath("//div[@class='nameCls']")
# list_of_brand_name = []
# for index, brand_name in enumerate(brand_names):
#     if index < 6:
#         list_of_brand_name.append(brand_name.text)
# print(list_of_brand_name)
#
# origial_prices = driver.find_elements_by_xpath("//span[@class='orginal-price']")
# list_original_price = []
# for index, origial_price in enumerate(origial_prices):
#     if index < 6:
#         list_original_price.append(origial_price.text)
#
# print(list_original_price)
#
# dis_prices = driver.find_elements_by_xpath("//span[@class='price  ']")
# list_dis_price = []
# for index, dis_price in enumerate(dis_prices):
#     if index < 6:
#         list_dis_price.append(dis_price.text)
#
# print(list_dis_price)
#
# per_dis = driver.find_elements_by_xpath("//span[@class='discount']")
# list_per_dis = []
#
# for index, per_discount in enumerate(per_dis):
#     if index < 6:
#         list_per_dis.append(per_discount.text)
#
# print(list_per_dis)
#
#
# all_product_details = zip(list_of_brand_name, list_original_price, list_dis_price, list_per_dis)
#
# l = list(all_product_details)
#
# l.sort(key=lambda item: item[1])
# print(l[-1])



















# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
#     else:
#         d[key] = value
# print(d)


# s = "hai welcome to python programming in real world"
# l = sorted(s.split(), key=len)
# print(l[-1])

# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# for item in items:
#     if items.count(item) == 1:
#         print(item)

# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])
# print((a, b))

# res = lambda a, b: a + b
# print(res(2, 2))

# s = "Hi How Are You"
# print(s[::-1])

# for i in s.split():
#     print(i[::-1], end=" ")

# def rev(n):
#     for item in n:
#         if isinstance(item, str):
#             print(item)
#         else:
#             res = str(item)
#             print(res[::-1])
#
# rev(["shashi", 123, "hai", 654.25])

# class Login:
#
#     count = 0
#     def __init__(self):
#         Login.count += 1
#
# l = Login()
# s = Login()
# print(Login.count)

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(abs(res))
#
#     return wrapper
#
# @outer
# def sub(a, b):
#     return a - b
#
# sub(5, 10)

# s = "hellohai"
# for i in s:
#     if s.count(i) > 1:
#         print("-", end="")
#     else:
#         print(i, end="")

# s = "shashi"
# ch = input("enter chr :")
# for index, chr in enumerate(s):
#     if chr == ch:
#         print(index)

# s = "som"
# if s[::-1] == s:
#     print("palindrom")

# start = 5
# end = 10
#
# with open(path1)as file:
#     for index, line in enumerate(file):
#         if index in range(start, end):
#             print(line)

# ch = int(input("enter num :"))
# with open(path1)as file:
#     for index, line in enumerate(file):
#         if index == ch:
#             print(line)

# l = [1, 2]
# l1 = [2, 3]
# print(l + l1)

# s = "hEllo WelCome To pYthoN"
# for i in s:
#     if "A" <= i <= "Z":
#         print(chr(ord(i)+32), end="")
#     elif "a" <= i <= "z":
#         print(chr(ord(i)-32), end="")

# if 'A'<= s <= 'Z':
#     print(chr(ord(s)+32))
# elif 'a'<= s <= 'z':
#     print(chr(ord(s)-32))

# for i in s:
#     print(ord(i))

# print(s[::2])

# print(",".join(s))

# s = "shashi"
# l = list(s)
# print("".join(l))

# s = "hello world"
# print(s.split())
# for i in s.split():
#     if i == "world":
#         print("universe")
#     else:
#         print(i, end=" ")

# s = "shai"
# print(s[::-1])
# c = ""
# for i in s:
#     c = i + c
# print(c)
#
# l = list(s)
# print("".join(l[::-1]))

# s = "shashi"
# print(len(s))
# print(s.count("s"))
# c = 0
# for i in s:
#     c += 1
# print(c)

# class Ntime:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for _ in range(self.n):
#                 res = func(*args, **kwargs)
#                 print(res)
#         return wrapper
#
# @Ntime(5)
# def add(a, b):
#     return a + b
#
# add(2, 2)

# class Log:
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res
#         return wrapper
#
# @Log()
# def add(a, b):
#     return a + b
#
# print(add(2, 2))


# def log(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 res = func(*args, **kwargs)
#                 print(abs(res))
#         return wrapper
#     return outer
#
# @log(5)
# def sub(a, b):
#     return a - b
#
# sub(5, 10)

# def n_times(n):
#     def repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 res = func(*args, **kwargs)
#                 print(res)
#         return wrapper
#     return repeat
#
# @n_times(3)
# def add(a, b):
#     return a + b
#
# @n_times(2)
# def sub(a, b):
#     return a - b
#
# add(2, 3)
# sub(5, 3)

# def outer(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @outer
# def add(a, b):
#     return a + b
#
# print(add(2, 2))

# names = {"shashi":25 , "vidya": 65, "ravi": 45, "prudvi": 55}
# print(sorted(names.items(), key=lambda item: item[-1]))

# print(sorted(names, key=lambda item: item[-1]))

# print(sorted(names, key=None, reverse=True))

# l = [2, 5, 6, 8, 9, 6, 4]
# print(list(filter(lambda a: a % 2 == 0, l)))
# print(list(map(lambda a: a * 2, l)))
# print(reduce(lambda a, b: a + b, l))

# s = "shashi"
# print(s[::-1])
# l = list(s)

# s = "ahashi"
# if s[0] in "aeiou":
#     print(True)
# else:
#     print(False)



# d = {'a': 25, 'b': 30}
# print(dict((v, k) for k, v in d.items()))


# for key, value in d.items():
#     d[value] = key
# print(d)

# print(d.popitem())

# d['a'] = 45
# print(d)
# print(d.items())
# print(d.keys())
# print(d.values())

# s = "hai shashi how are you"
# print(s.split())

# l = ['amazon', 'flipkart', 'myntra']
# l.append(['ajio', 'shashi'])
# print(l)

# l1 = [1, 2]
# l2 = [2, 4]
# l3 = [*l1, *l2]
# print(l3)


# driver = webdriver.Chrome()
# driver.find_element_by_link_text()

# n = 5
# for i in range(2, n):
#     if n % i == 0:
#         break
# else:
#     print(n)

# n = 5
# for i in range(2, n):
#     if n % i == 0:
#         print('it is not a prime')
#         break
# else:
#     print("prime")

# for n in range(2, 50):
#     for i in range(2, n):
#         if n % 2 == 0:
#             break
#     else:
#         print(n)

# for n in range(2, 50):
#     for i in range(2, n):
#         if n % 2 == 0:
#             break
#     else:
#         print(n)

# variable = imamge("path")
# copy = clone(variable)

# s = "nikhilii shashi kumar"

# l = s.split()
# print(", ".join(l))

# print(s.startswith("n"))

# print(s.replace("i", "a"))

# print(s.find("i"))

# print(s.count("i"))

# c = 0
# for i in s:
#     if i == "i":
#         c += 1
# print(c)

# l = [('sga', 25, 15, '10%'), ("ggh", 15, 10, '8%')]
# l.sort(key = lambda item: item[1])
# print(l)

# s = "sghhgkj15gf155"
# ss = ''
# for i in s:
#     if i.isalpha():
#         ss += i
# print(len(ss))

# s = "PYTHON HON"
# print(s.strip("PYTHON"))


# for i in range(len(s)):

# l = s.replace("PYTHON", "")
# print(l)

# def remove(s):
#     for i in s:
#         if i in "PYTHON":
#             print(i)
# print(remove(s))
# print(s)

# res = re.findall('[PYTHON]', s)
#
# print(res)

# l = [1, 2, 3, 4, 6, 7, 8]
# for i in range(1, len(l)):
#     if i not in l:
#         print(i)
#
# driver = webdriver.Chrome("./chromedriver.exe")
# driver.maximize_window()
# # driver.get("https://www.ajio.com/")
# # sleep(5)
#
# ele1 = driver.find_element_by_xpath("path")
# co_ordinates = ele1.rect

# ele2 =
# driver.find_element_by_name("register-button").click()
# sleep(1)
# error_text = driver.find_element_by_xpath("//span[@for='FirstName']")
#
# if error_text.text == "First name is required.":
#     print("error message is displaying")



# action = ActionChains(driver)
#
# ele = driver.find_element_by_link_text("Register")
#
# target_ele = driver.find_element_by_xpath("abc")
# print(target_ele.rect)
# #('x': 250, 'y': 500)
#
# action.click_and_hold(ele).move_by_offset(100, 200).release()



# driver.find_element_by_xpath("//input[@type='text']").send_keys("shoes")
# sleep(1)
# driver.find_element_by_xpath("//button[@type='submit']").click()
# sleep(2)
# product_name = driver.find_elements_by_xpath("//div[@class='nameCls']")
# #
# name_of_shoes = []
# for index, name in enumerate(product_name):
#     if index < 6:
#         name_of_shoes.append(name.text)
#
# actual_price = driver.find_elements_by_xpath("//span[@class='orginal-price']")
# original_price = []
# for index, org_price in enumerate(actual_price):
#     if index < 6:
#         original_price.append(org_price.text)
#
# actual_discount = driver.find_elements_by_xpath("//span[@class='price ']")
# discount_price = []
# for index, dis_price in enumerate(actual_price):
#     if index < 6:
#         discount_price.append(dis_price.text)
#
# discount_percemts = driver.find_elements_by_xpath("//span[@class='discount']")
#
# discounts = []
# for index, actual_percent in enumerate(discount_percemts):
#     if index < 6:
#         discounts.append(actual_percent.text)
#
# all_product_details = zip(name_of_shoes, original_price, discount_price, discounts)
# s = list(all_product_details)
# print(s)
# s.sort(key=lambda item: item[1])
# print(s[-1])



# a, b, *c, d = 1, 2, 3, 4, 5
# print(a, b, c, d)

# class Ntimes:

#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for i in range(self.n):
#                 print(func(*args, **kwargs))
#         return wrapper
#
# @Ntimes(5)
# def add(a, b):
#     return a + b
#
# add(2, 2)

# class Ntimes:
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for _ in range(3):
#                 print(func(*args, **kwargs))
#         return wrapper
# @Ntimes()
# def add(a, b):
#     return a +b
# add(2, 2)


# class Message:
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(func(*args, **kwargs))
#
#             print("hello everyone")
#
#         return wrapper
#
# @Message()
# def add(a, b):
#     return a + b
#
# add(1, 2)

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @outer
# def reverse(a):
#     return a[::-1]
#
# print(reverse("shashi"))

# def n_times(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 print(func(*args, **kwargs))
#         return wrapper
#     return outer
#
# @n_times(10)
# def add(a, b):
#     return a + b
#
# add(2, 2)

# def positive(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
# @positive
# def sub(a, b):
#     return a - b
#
# print(sub(5, 10))
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @log
# def add(a, b):
#     return a + b
#
# print(add(2, 2))



# def reverse(n):
#     print(n[::-1])
#
# reverse("shashi")

# s = "shashikumar"
# print(s[-2:-4:-2])

# def product(a, b):
#     p = a * b
#     print(p)
#
# def product(a, b, c):
#     p = a * b * c
#     print(p)
#
# product(1, 2)

# class Parent:
#
#     def __init__(self):
#         self.name = "In parent"
#     def spam(self):
#         print(self.name)
#
# class Child(Parent):
#
#     def spam(self):
#         print("In child")
#
# obj = Child()
# obj.spam()
# print(Child.spam(obj))
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in l:
#     if i % 2 == 0:
#         print(i)

# print([i for i in l if i % 2 == 0])


# driver = webdriver.Chrome(r"C:\Users\DELL\PycharmProjects\Selenium_Training\training\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com/")
# sleep(2)

# driver.find_element_by_xpath("//a[@class='ico-register']").click()
# sleep(1)
# driver.find_element_by_id("gender-female").click()
# sleep(1)
# driver.find_element_by_name("FirstName").send_keys("nishitha")
# sleep(1)
# driver.find_element_by_id("LastName").send_keys("chawla")
# sleep(1)
# driver.find_element_by_id("Email").send_keys("nishikc123@gmail.com")
# sleep(1)
# driver.find_element_by_name("Password").send_keys("nishi123")
# sleep(1)
# driver.find_element_by_id("ConfirmPassword").send_keys("nishi123")
# sleep(1)
# driver.find_element_by_id("register-button").click()


# def send_keys(n):
#     print("sending name into text filed", n)


# driver.quit()
# driver.close()
# expected_title = 'Dmo Web Shop'
#
# actual_title = driver.title
#
# if actual_title == expected_title:
#     print(actual_title)
# else:
#     print("title is mismatching")
# s = [1, 3, 5, 9]
# for i in range(1, 10):
    # if i not in s:
        # if i % 2 == 0:
            # s.insert(i)
# print()

# s = "hello"
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)
# path = r'C:\Users\DELL\PycharmProjects\Selenium_Training\files\hello'
# with open(path) as f:
#     for line in f:
#         for i in line.strip():
#             if "@gmail.com" in i:
#                 print(i)
# l = [1, 2, 3]
# l1 = [4, 5, 6]
# d = {}
# for i in l:
#     for j in l1:
#         d[i] = j
# print(d)


















