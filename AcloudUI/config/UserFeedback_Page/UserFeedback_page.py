from AcloudUI.common.utils import UIHelper
from AcloudUI.config.UserFeedback_Page.UserFeedback_locator import UserFeedback_Locators as Loc

class UserFeedbackPage():
    def __init__(self, driver):
        self.ui = UIHelper(driver)

    """进入反馈列表"""
    def goto_feedback_list(self):
        self.ui.click(Loc.feedbacklist01)
        self.ui.click(Loc.feedbacklist02)

    """搜索反馈"""
    def search_feedback(self):
        self.ui.click(Loc.feedbacklist03)
        self.ui.click(Loc.feedbacklist04)
        self.ui.click(Loc.feedbacklist05)

    """重置搜索反馈"""
    def reset_search_feedback(self):
        self.ui.click(Loc.feedbacklist06)


    """进入日志上报"""
    def goto_log_report(self):
        self.ui.click(Loc.logreporting01)

    """搜索日志"""
    def search_log(self, info):
        self.ui.send_keys(Loc.logreporting02, info)
        self.ui.click(Loc.logreporting03)

    """重置搜索日志"""
    def reset_search_log(self):
        self.ui.click(Loc.logreporting04)