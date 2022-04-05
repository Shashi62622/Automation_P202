from selenium_wrapper import SeleniumWrapper

class HomePage(SeleniumWrapper):

    def home_click_register(self):
        self.click_me(("link text", "Register"))

    def home_click_login(self):
        self.click_me(("link text", "Log in"))
