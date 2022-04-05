from pytest import mark
from logpage import LogPage
from S_wrapper import SeleniumWrapper

headers = "mail, password"

data = [("reddy@gmail.com", "reddy123")]

@mark.parametrize(headers, data)
def test_login(setup, mail, password):
    login = LogPage(setup)
    login.home_click_register()
    login.log_enter_mail(mail)
    login.log_enter_passwrd(password)
    login.log_click_login()









