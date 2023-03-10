from pageObject.config.config_xlsx import ConfigXlsxData
from pageObject.config.config_file import ConfigData
from pageObject.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactPage(BasePage):


    EMAIL_INPUT =(By.XPATH, '//input[@name="emailOrPhone"]')
    FULL_NAME_INPUT =(By.NAME, 'fullName')
    USERNAME_INPUT = (By.NAME, 'Username')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]') #xpath = //tagname[@attribut ='value']
    SING_UP_INPUT = (By.XPATH,'//button[@class="_acan _acap _acas _aj1-"]')

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(ConfigData.INSTAGRAM_SINGUP_URL)


    def fill_form_with_data(self):
        
        self.do_send_keys(self.EMAIL_INPUT, 'chaitanya')
        self.do_send_keys(self.FULL_NAME_INPUT, 'chay@mail.com')
        self.do_send_keys(self.USERNAME_INPUT, '0451677979')
        self.do_send_keys(self.PASSWORD_INPUT, 'powerball')

    def do_click_SING_UP_buttton(self):
        self.do_click(self.SING_UP_INPUT)    
        

    