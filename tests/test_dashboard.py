from pages.dashboardpage import DashBoard
from pages.loginpage import LoginPage
from utilities.ReadConfig import ReadConfig
import pytest

class Test_Dashboard:

    @pytest.mark.sanity
    def test_cataloglink(self, init_driver):
        self.driver = init_driver
        # logging to application
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(ReadConfig.getUsername())
        self.lp.setPassword(ReadConfig.getPassword())
        self.lp.clickLogin()
        self.lp = DashBoard(self.driver)
        assert True, self.lp.checkCatalogLinkAvailable()
        self.driver.close()

    @pytest.mark.sanity
    def test_Sales_link(self, init_driver):
        self.driver = init_driver
        # logging to application
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(ReadConfig.getUsername())
        self.lp.setPassword(ReadConfig.getPassword())
        self.lp.clickLogin()
        self.lp = DashBoard(self.driver)
        assert True, self.lp.checkSalesLinkAvailable()
        self.driver.close()

    def test_customer_link(self, init_driver):
        self.driver = init_driver
        # logging to application
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(ReadConfig.getUsername())
        self.lp.setPassword(ReadConfig.getPassword())
        self.lp.clickLogin()
        self.lp = DashBoard(self.driver)
        assert True, self.lp.checkcustomerLinkAvailable()
        self.driver.close()

    def test_promotions_link(self, init_driver):
        self.driver = init_driver
        # logging to application
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(ReadConfig.getUsername())
        self.lp.setPassword(ReadConfig.getPassword())
        self.lp.clickLogin()
        self.lp = DashBoard(self.driver)
        assert True, self.lp.checkPromotionsLinkAvailable()
        self.driver.close()
