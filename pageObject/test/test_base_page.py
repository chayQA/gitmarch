import pytest
from pageObject.config.config_file import ConfigData
from selenium import webdriver

@pytest.mark.usefixtures('init_driver')

#fixture is created inside the class, then we pass this Decorator / @pytest.mark.usefixtures('init_driver')

#init_driver is a Test_function name, we pass it as a arrgument to @Decorator)
#init _driver test function will execute -- for every function

class BaseTest:

    @pytest.fixture(scope='function')
    def init_driver(self, request):

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Chrome(executable_path=ConfigData.CHROME_DRIVER_PATH, options =options) 
        request.cls.driver = web_driver
        yield   #yield ia generator function 
        web_driver.quit()
