from homepage import HomePage

class LogIn(HomePage):

    def login_enter_email(self, email):
        self.enter_text(("id", "Email"), email)

    def login_enter_password(self, passwrod):
        self.enter_text(("id", "Password"), passwrod)

    def login_click_login(self):
        self.click_me(("id", "Log in"))


