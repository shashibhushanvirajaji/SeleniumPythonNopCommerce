from pages.loginpage import LoginPage
from utilities.ReadConfig import ReadConfig
from utilities.customlogger import GenerateLog
from utilities import XLUtils
import time


#
# @pytest.mark.usefixtures('init_driver')
# class Baseclass:
#     pass


class Test_LoginPage_Datadriven():
    logger = GenerateLog.logg()

    def test_loginFunctionality_dd(self, init_driver):
        self.driver = init_driver
        self.lp = LoginPage(self.driver)
        for r in range(1, XLUtils.getrows()):
            email = XLUtils.getdata(r, 0)
            password = XLUtils.getdata(r, 1)
            self.lp.setUsername(email)
            time.sleep(3)
            self.lp.setPassword(password)
            time.sleep(3)
            self.lp.clickLogin()
            time.sleep(5)
            self.lp.clickLogout()
        self.driver.close()
