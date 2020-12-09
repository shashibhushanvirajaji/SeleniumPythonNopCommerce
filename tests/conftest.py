import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.ReadConfig import ReadConfig


#
# @pytest.fixture(scope='class')
# def init_driver(request):
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get(baseURL)
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.quit()


@pytest.fixture()
def init_driver(browser):
    global driver
    if browser== 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser== 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # else:
    #     driver = webdriver.Ie()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(ReadConfig.getApplicationURL())
    return driver


def pytest_html_report_title(report):
    report.title = "Nop Commerce Report"


def pytest_addoption(parser):  # this will get the values from cli - this is a hook
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
