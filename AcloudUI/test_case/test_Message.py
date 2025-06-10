import unittest
from time import sleep

from AcloudUI.config.Message_Page.Message_page import Message_Page
from AcloudUI.config.usermanagement_POM import cloudlogin
from selenium import webdriver


"""消息管理"""
class test_F(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://koophone-cc.cmtest.xyz:8080/cloud-phone-admin/#/login')
        cloudlogin(cls.driver, "luoweijie", "Password:123")
        cls.driver.implicitly_wait(10)
        cls.page=Message_Page(cls.driver)


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.quit()

    def test_01_message_list(self):
        self.page.goto_message_list()
        self.page.search_message()
        self.page.reset_search_condition()