from homepage import HomePage

class RegistrationPage(HomePage):

    def registration_select_male(self):
        self.click_me(("id", "gender-male"))

    def registration_select_female(self):
        self.click_me(("id", "gender-female"))


    def registration_enter_first_name(self, fname):
        self.enter_text(("id", "FirstName"), value=fname)

    def registration_enter_last_name(self, lname):
        self.enter_text(("id", "LastName"), value=lname)

    def registration_enter_email(self, email):
        self.enter_text(("id", "Email"), value=email)

    def registration_enter_password(self, password):
        self.enter_text(("id", "Password"), value=password)

    def registation_enter_confirm_password(self, password):
        self.enter_text(("id", "ConfirmPassword"), value=password)

    def registration_click_register(self):
        self.click_me(("id", "register-button"))

