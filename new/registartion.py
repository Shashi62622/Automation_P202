from S_wrapper import SeleniumWrapper

class RegisterPage(SeleniumWrapper):

    def reg_click_male(self):
        self.click_me(("id", "gender-male")).click()

    def reg_click_female(self):
        self.click_me(("id", "gender-female")).click()

    def reg_enter_fname(self, fname):
        self.enter_text(("id", "FirstName"), fname)

    def reg_enter_lname(self, lname):
        self.enter_text(("id", "LastName"), lname)

    def reg_enter_mail(self, mail):
        self.enter_text(("id", "Email"), mail)

    def reg_enter_password(self, password):
        self.enter_text(("id", "Password"), password)

    def reg_enter_con_password(self, password):
        self.enter_text(("id", "ConfirmPassword"), password)

    def reg_click_register(self):
        self.click_me(("id", "register-button"))