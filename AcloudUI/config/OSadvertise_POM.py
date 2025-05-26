import pyautogui
from time import sleep
from selenium.webdriver.common.by import By
from AcloudUI.common.Avalue import OSadverse1, OSadverse2, OSadverse3, OSadverse4, OSadverse5, OSadverse6, OSadverse7, \
    OSadverse8, OSadverse9, OSadverse10, OSadverse11, OSadverse12, OSadverse13, OSadverse14, OSadverse15, OSadverse16, \
    OSadverse17, OSadverse18, OSadverse19, OSadverse20, OSadverse21, OSadverse22, theme1, theme2, theme3, theme4, \
    theme5, theme6, theme7, theme8, theme9, theme10, theme11, theme12, theme13, theme14, theme15, theme16, wallpaper1, \
    wallpaper2, wallpaper3, wallpaper4, wallpaper5, wallpaper6, wallpaper7, wallpaper8, wallpaper9, wallpaper10, \
    wallpaper11, wallpaper12, wallpaper13, wallpaper14, wallpaper15, widget1, widget2, widget3, widget4, widget5, \
    widget6, widget7, widget8, widget9, widget10, widget11, widget12, widget13, widget14, widget15, widget16, widget17, \
    application1, application2, application3, application4, application5, application6, application7, application8, \
    application9, application10, application11, message1, message2, message3, message4, message5, message6, message7, message8,message9, message10, message11, message12, message13
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#进入OS运营管理
def osadvertise(driver):
    driver.find_element(*OSadverse1).click()
    sleep(2)
    return driver

#新增OS广告
def osadvertiseadd(driver,addtitle,osurl):
    driver.find_element(*OSadverse2).click()
    sleep(2)
    driver.find_element(*OSadverse3).click()
    sleep(2)
    driver.find_element(*OSadverse4).click()
    sleep(2)
    driver.find_element(*OSadverse5).click()
    sleep(1)
    driver.find_element(*OSadverse6).click()
    driver.implicitly_wait(30)
    driver.find_element(*OSadverse7).click()
    sleep(1)
    driver.find_element(*OSadverse8).click()
    driver.implicitly_wait(30)
    driver.find_element(*OSadverse9).send_keys(addtitle)
    driver.find_element(*OSadverse10).click()
    driver.implicitly_wait(30)
    driver.find_element(*OSadverse11).send_keys(osurl)
    driver.find_element(*OSadverse12).click()
    driver.implicitly_wait(30)
    driver.find_element(*OSadverse13).click()
    sleep(2)
    return driver

#查询OS广告
def osadvertiseselect(driver):
    driver.find_element(*OSadverse14).click()
    sleep(2)
    driver.find_element(*OSadverse15).click()
    driver.implicitly_wait(30)
    driver.find_element(*OSadverse16).click()
    sleep(2)
    return driver

#编辑OS广告
def osadvertiseupdate(driver,updatetitle):
    driver.find_element(*OSadverse17).click()
    sleep(2)
    driver.find_element(*OSadverse18).send_keys(updatetitle)
    driver.implicitly_wait(30)
    driver.find_element(*OSadverse19).click()
    driver.implicitly_wait(30)
    driver.find_element(*OSadverse20).click()
    sleep(2)
    return driver

#删除OS广告
def osadvertisedelete(driver):
    driver.find_element(*OSadverse21).click()
    driver.implicitly_wait(30)
    driver.find_element(*OSadverse22).click()
    sleep(2)
    return driver

#新增主题
def themeadd(driver,addtitle,files,filesgnz):
    driver.find_element(*theme1).click()
    sleep(2)
    driver.find_element(*theme2).click()
    sleep(2)
    driver.find_element(*theme3).send_keys(addtitle)
    driver.implicitly_wait(30)
    driver.find_element(*theme4).click()
    sleep(2)
    pyautogui.write(files)
    sleep(2)
    pyautogui.press('enter',2)
    sleep(2)
    driver.find_element(*theme5).click()
    sleep(2)
    pyautogui.write(filesgnz)
    sleep(3)
    pyautogui.press('enter',2)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="复制链接"]'))
    )
    driver.find_element(*theme6).click()
    driver.implicitly_wait(30)
    driver.find_element(*theme7).click()
    sleep(2)
    return driver

#查询主题
def themeselect(driver,addtitle):
    driver.find_element(*theme8).send_keys(addtitle)
    driver.find_element(*theme9).click()
    sleep(2)
    return driver

#编辑主题
def themeupdate(driver,updatetitle):
    driver.find_element(*theme10).click()
    sleep(2)
    driver.find_element(*theme11).send_keys(updatetitle)
    driver.implicitly_wait(30)
    driver.find_element(*theme12).click()
    driver.implicitly_wait(30)
    driver.find_element(*theme13).click()
    sleep(2)
    return driver

#删除主题
def themedelete(driver):
    driver.find_element(*theme14).click()
    sleep(2)
    driver.find_element(*theme15).click()
    driver.implicitly_wait(30)
    driver.find_element(*theme16).click()
    sleep(2)
    return driver

#新增壁纸
def wallpaperadd(driver,addtitle,files):
    driver.find_element(*wallpaper1).click()
    sleep(2)
    driver.find_element(*wallpaper2).click()
    sleep(2)
    driver.find_element(*wallpaper3).send_keys(addtitle)
    driver.implicitly_wait(30)
    driver.find_element(*wallpaper4).click()
    sleep(2)
    pyautogui.write(files)
    sleep(2)
    pyautogui.press('enter',2)
    sleep(2)
    driver.find_element(*wallpaper5).click()
    driver.implicitly_wait(30)
    driver.find_element(*wallpaper6).click()
    sleep(2)
    return driver

#查询壁纸
def wallpaperselect(driver,addtitle):
    driver.find_element(*wallpaper7).send_keys(addtitle)
    driver.find_element(*wallpaper8).click()
    sleep(2)
    return driver

#编辑壁纸
def wallpaperupdate(driver,updatetitle):
    driver.find_element(*wallpaper9).click()
    sleep(2)
    driver.find_element(*wallpaper10).send_keys(updatetitle)
    driver.implicitly_wait(30)
    driver.find_element(*wallpaper11).click()
    driver.implicitly_wait(30)
    driver.find_element(*wallpaper12).click()
    sleep(2)
    return driver

#删除壁纸
def wallpaperdelete(driver):
    driver.find_element(*wallpaper13).click()
    sleep(2)
    driver.find_element(*wallpaper14).click()
    driver.implicitly_wait(30)
    driver.find_element(*wallpaper15).click()
    sleep(2)
    return driver

#新增小组件
def widgetadd(driver,addtitle,files):
    driver.find_element(*widget1).click()
    sleep(2)
    driver.find_element(*widget2).click()
    sleep(2)
    driver.find_element(*widget3).send_keys(addtitle)
    driver.implicitly_wait(30)
    driver.find_element(*widget4).click()
    sleep(1)
    driver.find_element(*widget5).click()
    driver.implicitly_wait(30)
    driver.find_element(*widget6).click()
    sleep(2)
    pyautogui.write(files)
    sleep(2)
    pyautogui.press('enter',2)
    sleep(2)
    driver.find_element(*widget7).click()
    driver.implicitly_wait(30)
    driver.find_element(*widget8).click()
    sleep(2)
    return driver

#查询小组件
def widgetselect(driver,addtitle):
    driver.find_element(*widget9).send_keys(addtitle)
    driver.find_element(*widget10).click()
    sleep(2)
    return driver

#编辑小组件
def widgetupdate(driver,updatetitle):
    driver.find_element(*widget11).click()
    sleep(2)
    driver.find_element(*widget12).send_keys(updatetitle)
    driver.implicitly_wait(30)
    driver.find_element(*widget13).click()
    driver.implicitly_wait(30)
    driver.find_element(*widget14).click()
    sleep(2)
    return driver

#删除小组件
def widgetdelete(driver):
    driver.find_element(*widget15).click()
    sleep(2)
    driver.find_element(*widget16).click()
    driver.implicitly_wait(30)
    driver.find_element(*widget17).click()
    sleep(2)
    return driver

#新增应用
def applicationadd(driver,fileapp,addtitle,files):
    driver.find_element(*application1).click()
    sleep(2)
    driver.find_element(*application2).click()
    sleep(2)
    driver.find_element(*application3).click()
    sleep(2)
    pyautogui.write(fileapp)
    sleep(2)
    pyautogui.press('enter',2)
    sleep(2)
    driver.find_element(*application4).send_keys(addtitle)
    driver.implicitly_wait(30)
    driver.find_element(*application5).click()
    sleep(2)
    pyautogui.write(files)
    sleep(2)
    pyautogui.press('enter',2)
    sleep(2)
    driver.find_element(*application6).click()
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]'))
    )
    return driver

#查询应用
def applicationselect(driver,addtitle):
    driver.find_element(*application7).send_keys(addtitle)
    driver.find_element(*application8).click()
    sleep(2)
    return driver

#删除应用
def applicationdelete(driver):
    driver.find_element(*application9).click()
    sleep(2)
    driver.find_element(*application10).click()
    driver.implicitly_wait(30)
    driver.find_element(*application11).click()
    sleep(2)
    return driver

#新增消息
def messageadd(driver,addtitle,addcontent,addaccount):
    driver.find_element(*message1).click()
    sleep(2)
    driver.find_element(*message2).click()
    sleep(2)
    driver.find_element(*message3).click()
    sleep(2)
    driver.find_element(*message4).send_keys(addtitle)
    driver.find_element(*message5).send_keys(addcontent)
    driver.implicitly_wait(30)
    driver.find_element(*message6).click()
    sleep(1)
    driver.find_element(*message7).click()
    sleep(1)
    driver.find_element(*message8).click()
    driver.implicitly_wait(30)
    driver.find_element(*message9).send_keys(addaccount)
    driver.implicitly_wait(30)
    driver.find_element(*message10).click()
    sleep(2)
    driver.find_element(*message11).click()
    sleep(2)
    driver.find_element(*message12).click()
    driver.implicitly_wait(30)
    driver.find_element(*message13).click()
    sleep(2)
    return driver