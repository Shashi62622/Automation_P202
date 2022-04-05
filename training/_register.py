from selenium_wrapper import SeleniumWrapper
from pytest import mark
from registration_page import RegistrationPage

headers = "gender, fname, lname, email, password"

data = [("Male", "prudvi", "raj", "prudviraj33@gmail.com", "prudvi123"),
        ("Female", "prudvi", "raj", "prudviraj44@gmail.com", "prudvi123")
        ]
@mark.parametrize(headers, data)
def test_registration(setup, gender, fname, lname, email, password):

    reg = RegistrationPage(setup)

    reg.home_click_register()

    if gender == "Male":
        reg.registration_select_male()
    elif gender == "Female":
        reg.registration_select_female()

    reg.registration_enter_first_name(fname)
    reg.registration_enter_last_name(lname)
    reg.registration_enter_email(email)
    reg.registration_enter_email(email)
    reg.registration_enter_password(password)
    reg.registation_enter_confirm_password(password)













































