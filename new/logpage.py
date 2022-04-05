from S_wrapper import SeleniumWrapper

class LogPage(SeleniumWrapper):

    def log_enter_mail(self, mail):
        self.enter_text(("id", "Mail"))

    def log_enter_password(self, password):
        self.enter_text(("id", "Password"), password)

    def log_click_login(self):
        self.click_me(("link text", "Log in"))