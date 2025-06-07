from AcloudUI.common.utils import UIHelper
from AcloudUI.config.SmartDesktopIntegration_Page.SmartDesktopIntegration_locator import SmartDesktopIntegration_Locators as Loc

class SmartDesktopIntegration_Page:
    def __init__(self, driver):
        self.ui = UIHelper(driver)
    """白名单账号"""
    #进入白名单页面
    def enter_white_list_tab(self):
        self.ui.click(Loc.whitelist01)
        self.ui.click(Loc.whitelist02)
        self.ui.click(Loc.whitelist03)
        
    #抖索白名单账号
    def search_account(self, info):
        self.ui.send_keys(Loc.whitelist04, info)
        self.ui.click(Loc.whitelist05)

    """布局文件管理"""
    #进入桌面布局页面
    def enter_layoutfile(self):
        self.ui.click(Loc.layoutfile01)

    #搜索布局文件
    def search_layoutfile(self, info):
        self.ui.send_keys(Loc.layoutfile02, info)
        self.ui.click(Loc.layoutfile03)

    """桌面布局管理"""
    #进入桌面布局页面
    def enter_desktoplayout(self):
        self.ui.click(Loc.desktoplayout01)

    #搜索布局文件
    def search_desktoplayout(self, info):
        self.ui.send_keys(Loc.desktoplayout02, info)
        self.ui.click(Loc.desktoplayout03)
    """桌面引导管理"""
    #进入桌面引导页面
    def enter_desktopguide(self):
        self.ui.click(Loc.desktopguide01)

    #搜索布局文件
    def search_desktopguide(self, info):
        self.ui.send_keys(Loc.desktopguide02, info)
        self.ui.click(Loc.desktopguide03)
    """娱乐文件管理"""
    #进入娱乐页面
    def enter_entertainment(self):
        self.ui.click(Loc.entertainment01)

    #搜索娱乐文件
    def search_entertainment(self, info):
        self.ui.send_keys(Loc.entertainment02, info)
        self.ui.click(Loc.entertainment03)
    """配置信息管理"""
    #进入配置信息页面
    def enter_configinfo(self):
        self.ui.click(Loc.configinfo01)

    #搜索配置信息
    def search_configinfo(self, info):
        self.ui.send_keys(Loc.configinfo02, info)
        self.ui.click(Loc.configinfo03)

