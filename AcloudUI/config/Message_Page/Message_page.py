from AcloudUI.common.utils import UIHelper
from AcloudUI.config.Message_Page.Message_locator import Message_Locators as Loc

class Message_Page:
    def __init__(self, driver):
        self.ui = UIHelper(driver)


    """进入消息列表"""
    def goto_message_list(self):
        self.ui.click(Loc.messagelist01)
        self.ui.click(Loc.messagelist02)

    """搜索消息"""
    def search_message(self):
        self.ui.click(Loc.messagelist03)

    """重置搜索条件"""
    def reset_search_condition(self):
        self.ui.click(Loc.messagelist04)
