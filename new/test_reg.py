from homepage import HomePage


hearders = "gender, fname, lname, mail, password"
data = [("Male", "reddy", "pilla", "reddy@gamil.com", "reddy123")]

def test_reg(setup, gender, fname, lname, mail, password):
    reg = HomePage(setup)
    reg.home_click_register()
    reg.reg_click_male(gender)
    reg.reg_enter_fanme(fname)
    reg.reg_enter_lname(lname)
    reg.reg_enter_mail(mail)
    reg.reg_enter_password(password)
    reg.reg_enter_con_password(password)
    reg.reg_click_register()



