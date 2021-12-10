class Loginpage:

    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    button_login_id = "btnLogin"
    link_forgetpwd_xpath = "//a[normalize-space()='Forgot your password?']"

    def __init__(self, driver):
        self.driver = driver

    def enterusername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def enterpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_id).click()

    def clickforgetpwd(self):
        self.driver.find_element_by_xpath(self.link_forgetpwd_xpath).click()
