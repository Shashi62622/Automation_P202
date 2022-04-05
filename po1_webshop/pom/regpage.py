from po1_webshop.pom.homepage import HomePage

class RegPage(HomePage):

    def reg_select_male(self):
        self.click_me(("id", "gender-male"))

    def reg_select_female(self):
        self.click_me(("id", "gender-female"))

    def reg_enter_first_name(self, fname):
        self.enter_text(("id", "FirstName"), fname)

    def reg_last_name(self, lname):
        self.enter_text(("id", "LastName"), lname)

    def reg_enter_email(self, email):
        self.enter_text(("id", "Email"), email)

    def reg_enter_password(self, password):
        self.enter_text(("id", "Password"), password)

    def reg_enter_confirm_password(self, password):
        self.enter_text(("id", "ConfirmPassword"), password)

    def reg_click_register(self):
        self.click_me(("id", "register-button"))
