import unittest
from time import sleep

from AcloudUI.config.UserFeedback_Page.UserFeedback_page import UserFeedbackPage
from AcloudUI.config.usermanagement_POM import cloudlogin
from selenium import webdriver


"""消息管理"""
class test_G(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://koophone-cc.cmtest.xyz:8080/cloud-phone-admin/#/login')
        cloudlogin(cls.driver, "luoweijie", "Password:123")
        cls.driver.implicitly_wait(10)
        cls.page=UserFeedbackPage(cls.driver)


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.quit()

    def test_01_feedbackList(self):
        self.page.goto_feedback_list()
        self.page.search_feedback()
        self.page.reset_search_feedback()
        pass

    def test_02_logreport(self):
        self.page.goto_log_report()
        self.page.search_log("15107612187")
        self.page.reset_search_log()
        pass