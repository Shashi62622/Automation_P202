from pytest import mark
from po1_webshop.pom.regpage import RegPage

# import sys
# sys.path.append(r"C:\Users\DELL\PycharmProjects\Selenium_Training\po1_webshop")
# from Selenium_Training

headers = "gender", "fname", "lname", "email", "password"

data = [("Male", "shashi", "sam1", "shashisam1@gmail.com", "shashi123"),
        ("Female", "shashi", "sam2", "shashisam2@gmail.com", "shashi123")]


@mark.parametrize(headers, data)
def test_regspage(setup, gender, fname, lname, email, password):

    reg = RegPage(setup)

    reg.home_click_me_register()

    if gender == "Male":
        reg.reg_select_male()
    elif gender == "Female":
        reg.reg_select_female()

    reg.reg_enter_first_name(fname)
    reg.reg_last_name(lname)
    reg.reg_enter_email(email)
    reg.reg_enter_password(email)
    reg.reg_enter_confirm_password(password)
    reg.reg_click_register()





















