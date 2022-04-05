from homepage import HomePage
from xceldata import read_locator

class LoginPage(HomePage):

    loginpage_objects = read_locator("login")

    def login_enter_email(self, email):
        self.enter_text(self.loginpage_objects['txt_email'], value=email)

    def login_enter_password(self, password):
        self.enter_text(self.loginpage_objects['txt_password'], value=password)

    def login_click_login(self):
        self.click_me(self.loginpage_objects['btn_login'])
