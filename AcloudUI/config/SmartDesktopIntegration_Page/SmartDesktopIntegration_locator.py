from selenium.webdriver.common.by import By

class SmartDesktopIntegration_Locators:
    whitelist01 = (By.XPATH, "//span[contains(text(),'智能桌面管理')]")
    whitelist02 = (By.XPATH, "(//span[contains(text(),'桌面布局')])[1]")
    whitelist03 = (By.XPATH, "//span[contains(text(),'白名单账号')]")
    whitelist04 = (By.XPATH, "(//input[@placeholder='请输入'])[1]")
    whitelist05 = (By.XPATH, "//span[contains(text(),'搜索')]")
    whitelist06= (By.XPATH, "(//span[contains(text(),'重置')])[1]")

    layoutfile01 = (By.XPATH, "(//span[contains(text(),'布局文件管理')])[1]")
    layoutfile02 = (By.XPATH, "(//input[contains(@placeholder,'请输入')])[1]")
    layoutfile03 = (By.XPATH, "(//span[contains(text(),'搜索')])[1]")
    layoutfile04 = (By.XPATH, "(//span[contains(text(),'重置')])[1]")

    desktoplayout01 = (By.XPATH, "//span[contains(text(),'桌面布局管理')]")
    desktoplayout02 = (By.XPATH, "(//input[contains(@placeholder,'请输入')])[1]")
    desktoplayout03 = (By.XPATH, "(//span[contains(text(),'搜索')])[1]")
    desktoplayout04 = (By.XPATH, "(//span[contains(text(),'重置')])[1]")

    desktopguide01 = (By.XPATH, "//span[contains(text(),'桌面引导管理')]")
    desktopguide02 = (By.XPATH, "(//input[contains(@placeholder,'请输入')])[1]")
    desktopguide03 = (By.XPATH, "(//span[contains(text(),'搜索')])[1]")
    desktopguide04 = (By.XPATH, "(//span[contains(text(),'重置')])[1]")

    entertainment01 = (By.XPATH, "//span[contains(text(),'娱乐专区管理')]")
    entertainment02 = (By.XPATH, "(//input[contains(@placeholder,'请输入')])[1]")
    entertainment03 = (By.XPATH, "(//span[contains(text(),'搜索')])[1]")
    entertainment04 = (By.XPATH, "(//span[contains(text(),'重置')])[1]")

    configinfo01 = (By.XPATH, "(//span[contains(text(),'配置信息管理')])[1]")
    configinfo02 = (By.XPATH, "(//input[contains(@placeholder,'请输入')])[1]")
    configinfo03 = (By.XPATH, "(//span[contains(text(),'搜索')])[1]")
    configinfo04 = (By.XPATH, "(//span[contains(text(),'重置')])[1]")

