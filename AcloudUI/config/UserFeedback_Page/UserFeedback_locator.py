
from selenium.webdriver.common.by import By

class UserFeedback_Locators:
    feedbacklist01= (By.XPATH, "(//span[contains(text(),'用户反馈')])[1]")
    feedbacklist02= (By.XPATH, "(//span[contains(text(),'反馈列表')])[1]")
    feedbacklist03= (By.XPATH, "(//input[@placeholder='请选择'])[1]")
    feedbacklist04= (By.XPATH, "(//span[contains(text(),'功能建议')])[1]")
    feedbacklist05= (By.XPATH, "(//span[contains(text(),'搜索')])[1]")
    feedbacklist06= (By.XPATH, "(//span[contains(text(),'重置')])[1]")

    logreporting01= (By.XPATH, "(//span[contains(text(),'日志上报')])[1]")
    logreporting02= (By.XPATH, "(//input[@placeholder='请输入用户账号'])[1]")
    logreporting03= (By.XPATH, "(//span[contains(text(),'搜索')])[1]")
    logreporting04= (By.XPATH, "(//span[contains(text(),'重置')])[1]")
