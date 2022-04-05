from po1_webshop.library.selenium_wrapper1 import SeleniumWrapper1

class HomePage(SeleniumWrapper1):

    def home_click_me_register(self):
        self.click_me(("link text", "Register"))

    def home_click_me_login(self):
        self.click_me(("link text", "Log in"))




