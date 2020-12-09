class DashBoard:
    link_catalog_xpath = "//span[normalize-space()='Catalog']"
    link_Sales_css = "ul.sidebar-menu > li:nth-of-type(3) > [href='#']"
    link_customer_css = "ul.sidebar-menu > li:nth-of-type(4) > [href='#']"
    link_promotions_css = "ul.sidebar-menu > li:nth-of-type(5) > [href='#'] > span"

    def __init__(self, driver):
        self.driver = driver

    def checkCatalogLinkAvailable(self):
        return self.driver.find_element_by_xpath(self.link_catalog_xpath).is_displayed()

    def checkSalesLinkAvailable(self):
        return self.driver.find_element_by_xpath(self.link_Sales_css).is_displayed()

    def checkcustomerLinkAvailable(self):
        return self.driver.find_element_by_xpath(self.link_customer_css).is_displayed()

    def checkPromotionsLinkAvailable(self):
        return self.driver.find_element_by_xpath(self.link_promotions_css).is_displayed()
