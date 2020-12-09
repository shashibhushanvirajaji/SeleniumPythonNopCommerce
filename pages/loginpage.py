
class LoginPage:

    username_textbox_id = 'Email'
    password_textbox_id = 'Password'
    login_button_css = 'input[value="Log in"]'
    logout_link_test = 'Logout'
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, email):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_css_selector(self.login_button_css).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.logout_link_test).click()


