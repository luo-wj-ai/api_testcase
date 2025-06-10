from selenium.webdriver.common.by import By

class Message_Locators:
    messagelist01= (By.XPATH, "(//span[contains(text(),'消息管理')])[1]")
    messagelist02= (By.XPATH, "(//span[contains(text(),'消息列表')])[1]")
    messagelist03= (By.XPATH, "(//span[contains(text(),'搜索')])[1]")
    messagelist04= (By.XPATH, "(//span[contains(text(),'重置')])[1]")