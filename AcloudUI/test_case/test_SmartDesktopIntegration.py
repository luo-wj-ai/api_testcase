import unittest
from time import sleep
from selenium import webdriver
from AcloudUI.config.SmartDesktopIntegration_Page.SmartDesktopIntegration_page import SmartDesktopIntegration_Page
from AcloudUI.config.usermanagement_POM import cloudlogin

whitelist_info = "15018066689"
layoutfile_info = "15018066689"
desktoplayout_info = "001"
desktopguide_info = "11"
entertainment_info = "11"
configinfo_info = "502"

class test_E(unittest.TestCase):
    """智能说面管理"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://koophone-cc.cmtest.xyz:8080/cloud-phone-admin/#/login')
        cloudlogin(cls.driver, "luoweijie", "Password:123")
        cls.driver.implicitly_wait(10)
        cls.page=SmartDesktopIntegration_Page(cls.driver)

    # #调试模式
    # @classmethod
    # def setUpClass(cls) -> None:
    #     options = Options()
    #     options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    #     cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(10)
        cls.driver.quit()

    def test_A01_whitelist(self):
        """白名单账号"""
        #进入白名单页面+搜索账号
        self.page.enter_white_list_tab()
        self.page.search_account(whitelist_info)
        pass

    def test_A02_layoutfile(self):
        """布局文件管理"""
        #进入布局文件管理页面+搜索账号
        self.page.enter_layoutfile()
        self.page.search_layoutfile(layoutfile_info)
        pass
    def test_A03_desktoplayout(self):
        """桌面布局管理"""
        #进入桌面布局管理页面+搜索账号
        self.page.enter_desktoplayout()
        self.page.search_desktoplayout(desktoplayout_info)
        pass
    def test_A04_desktopguide(self):
        """桌面引导管理"""
        #进入桌面引导管理页面+搜索账号
        self.page.enter_desktopguide()
        self.page.search_desktopguide(desktopguide_info)
        pass
    def test_A05_entertainment(self):
        """娱乐专区管理"""
        #进入娱乐专区管理页面+搜索账号
        self.page.enter_entertainment()
        self.page.search_entertainment(entertainment_info)
        pass
    def test_A06_configinfo(self):
        """配置信息管理"""
        #进入配置信息管理页面+搜索账号
        self.page.enter_configinfo()
        self.page.search_configinfo(configinfo_info)
        pass
