import pytest
from pageObject.pages.instagram_singUp_page import ContactPage
from pageObject.test.test_base_page import BaseTest
from pageObject.config.config_xlsx import ConfigXlsxData
from pageObject.config.config_file import ConfigData


class TestContactPage(BaseTest):

    def go_to_SINGUP_PAGE(self):
        self.SingUp_button=ContactPage(self.driver)
        self.SingUp_button.do_click_SING_UP_buttton()
        assert self.SingUp_button.get_current_page_url()==ConfigData.INSTAGRAM_SINGUP_URL 
        