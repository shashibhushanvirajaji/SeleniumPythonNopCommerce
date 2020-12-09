
from pages.loginpage import LoginPage
from utilities.ReadConfig import ReadConfig
from utilities.customlogger import GenerateLog
from  utilities.misc import Misc
#
# @pytest.mark.usefixtures('init_driver')
# class Baseclass:
#     pass


class Test_LoginPage():

    logger = GenerateLog.logg()

    def test_check_title(self, init_driver):
        self.driver = init_driver
        #function.__name__
        self.logger.info('starting check title test')
        self.driver.get_screenshot_as_file('./screenshots/'+Misc.getrandomdate())
        assert self.driver.title == 'Your store. Logi'
        self.logger.info('ending check title test')
        self.driver.close()


    def test_check_url(self, init_driver):
        self.driver = init_driver
        self.logger.info('starting check url test')
        self.driver.get_screenshot_as_file('./screenshots/'+ Misc.getrandomdate())
        self.logger.info('ending check url test')
        assert self.driver.current_url == 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
        self.driver.close()

    def test_loginFunctionality(self,init_driver):
        self.driver = init_driver
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(ReadConfig.getUsername())
        self.lp.setPassword(ReadConfig.getPassword())
        self.lp.clickLogin()
        self.driver.close()


