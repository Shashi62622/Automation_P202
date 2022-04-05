
from selenium_wrapper import SeleniumWrapper
from pytest import mark
from loginpage import LoginPage

headers = "email, password"

data = [("prudviraj33@gmail.com", "prudvi123"),
        ("prudvraj1244@gmail.com", "prudvi123")
        ]
@mark.parametrize(headers, data)
def test_login(setup, email, password):
    login = LoginPage(setup)
    login.home_click_login()
    login.login_enter_email(email)
    login.login_enter_password(password)
    login.home_click_login()


