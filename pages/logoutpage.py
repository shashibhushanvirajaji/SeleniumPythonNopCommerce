class Logout:

    logout_link_test = 'Logout'

    def __init__(self,driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.logout_link_test).click()