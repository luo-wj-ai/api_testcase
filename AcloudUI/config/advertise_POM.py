from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from AcloudUI.common.Avalue import adverse1, adverse2, adverse3, adverse4, adverse5, adverse6, adverse7, adverse8, \
    adverse9, adverse10, adverse11, adverse12, adverse13, adverse14, adverse15, adverse101, adverse102, adverse16, \
    adverse17, guide1, guide4, guide2, guide3, guide5, guide6, guide7, guide8, guide9, \
    guide10, guide11, guide12, guide13, guide14, guide15, guide16, screen1, screen2, screen3, screen4, screen6, \
    screen7, screen8, screen9, screen5, screen10, screen11, screen12, screen13, screen14, screen15, screen16, lingxi1, \
    lingxi2, lingxi3, lingxi4, lingxi5, lingxi6, lingxi7, lingxi8, lingxi9, lingxi10, \
    lingxi11, lingxi12, lingxi13, lingxi14, lingxi15, lingxi16, lingxi17, lingxi18, config1, config2, config3, config4, \
    config5, config6, config7, config8, config9, config10, config11, config12, config13, config14, config15, config16, \
    config17, config18, config19, config20, config21
import pyautogui

from AcloudUI.means.Upload_files import handle_screenshot


#进入运营管理
def adversee(driver):
    driver.find_element(*adverse1).click()
    sleep(2)
    return driver

#广告管理-新增广告
def adverseadd(driver,addtitle,files):
    driver.find_element(*adverse2).click()
    sleep(2)
    driver.find_element(*adverse3).click()
    sleep(2)
    driver.find_element(*adverse4).click()
    sleep(2)
    driver.find_element(*adverse5).send_keys(addtitle)
    driver.implicitly_wait(30)
    driver.find_element(*adverse6).click()
    driver.implicitly_wait(30)
    driver.find_element(*adverse7).click()
    driver.implicitly_wait(30)
    driver.find_element(*adverse8).click()
    sleep(2)
        #旧版截图
        # driver.find_element(*adverse9).click()
        # sleep(2)
        # pyautogui.write(files)
        # sleep(2)
        # pyautogui.press('enter',2)
        #sleep(2)
    #新版截图
    files=handle_screenshot(driver)
    driver.find_element(*adverse9).send_keys(files)
    sleep(2)
    driver.find_element(*adverse10).click()
    sleep(2)
    driver.implicitly_wait(30)
    driver.find_element(*adverse11).click()
    driver.implicitly_wait(30)
    driver.find_element(*adverse12).click()
    sleep(2)
    return driver

#广告管理-搜索广告
def adverseselects(driver,addtitle):
    driver.find_element(*adverse101).send_keys(addtitle)
    driver.find_element(*adverse102).click()
    sleep(2)
    return driver

#广告管理-编辑广告
def adverseupdate(driver,updatetitle):
    driver.find_element(*adverse13).click()
    sleep(2)
    driver.find_element(*adverse14).send_keys(updatetitle)
    driver.implicitly_wait(30)
    driver.find_element(*adverse15).click()
    sleep(2)
    return driver

#广告管理-删除广告
def adversedelete(driver):
    driver.find_element(*adverse16).click()
    driver.implicitly_wait(30)
    driver.find_element(*adverse17).click()
    sleep(2)
    return driver

#配置管理-新增配置
def configadd(driver,addtitle,showversion,internalversion,download,filesize,content):
    driver.find_element(*config1).click()
    sleep(2)
    driver.find_element(*config2).click()
    sleep(2)
    driver.find_element(*config3).click()
    sleep(2)
    driver.find_element(*config4).send_keys(addtitle)
    driver.find_element(*config5).send_keys(showversion)
    driver.find_element(*config6).send_keys(internalversion)
    driver.find_element(*config7).send_keys(download)
    driver.find_element(*config8).send_keys(filesize)
    sleep(2)
    driver.find_element(*config9).click()
    sleep(2)
    driver.implicitly_wait(30)
    driver.find_element(*config10).click()
    driver.implicitly_wait(30)
    driver.find_element(*config11).click()
    sleep(2)
    driver.find_element(*config12).click()
    driver.implicitly_wait(30)
    driver.find_element(*config13).send_keys(content)
    driver.find_element(*config14).click()
    sleep(2)
    return driver

#查询配置
def configselect(driver, addtitle):
    driver.find_element(*config15).send_keys(addtitle)
    driver.find_element(*config16).click()
    sleep(2)
    return driver
#编辑配置
def configupdate(driver,addtitle):
    driver.find_element(*config17).click()
    sleep(2)
    driver.find_element(*config18).clear()
    driver.find_element(*config18).send_keys(addtitle)
    driver.implicitly_wait(30)
    driver.find_element(*config19).click()
    sleep(2)
    return driver

#删除配置
def configdelete(driver):
    driver.find_element(*config20).click()
    driver.implicitly_wait(30)
    driver.find_element(*config21).click()
    sleep(2)
    return driver

#进入功能引导管理
def guidance(driver):
    # driver.find_element(*adverse1).click()
    # sleep(2)
    driver.find_element(*guide1).click()
    sleep(2)
    return driver

#新增功能引导
def guidanceadd(driver,addtitle,files,selectproduct):
    driver.find_element(*guide2).click()
    sleep(2)
    driver.find_element(*guide3).send_keys(addtitle)
    driver.implicitly_wait(30)
    #旧版本截图
    # driver.find_element(*guide4).click()
    # sleep(2)
    # pyautogui.write(files)
    # sleep(2)
    # pyautogui.press('enter',2)
    #新版本截图
    files=handle_screenshot(driver)
    driver.find_element(*guide4).send_keys(files)
    sleep(2)
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//p[text()="上传成功！"]')))
    driver.find_element(*guide5).send_keys(selectproduct)
    sleep(2)
    driver.find_element(*guide6).click()
    sleep(2)
    driver.find_element(*guide7).click()
    driver.implicitly_wait(30)
    driver.find_element(*guide8).click()
    sleep(2)
    return driver

#查询功能引导
def guidanceselect(driver,addtitle):
    driver.find_element(*guide9).send_keys(addtitle)
    driver.find_element(*guide10).click()
    sleep(2)
    return driver

#编辑功能引导
def guidanceupdate(driver,updatetitle):
    driver.find_element(*guide11).click()
    sleep(2)
    driver.find_element(*guide12).send_keys(updatetitle)
    driver.implicitly_wait(30)
    driver.find_element(*guide13).click()
    sleep(2)
    return driver

#删除功能引导
def guidancedelete(driver):
    driver.find_element(*guide14).click()
    sleep(2)
    driver.find_element(*guide15).click()
    driver.implicitly_wait(30)
    driver.find_element(*guide16).click()
    sleep(2)
    return driver

#进入开屏动画管理
def splashscreen(driver):
    # driver.find_element(*adverse1).click()
    # sleep(2)
    driver.find_element(*screen1).click()
    sleep(2)
    return driver

#新增开屏动画
def screenadd(driver,addtitle,files,selectproduct):
    driver.find_element(*screen2).click()
    sleep(2)
    driver.find_element(*screen3).send_keys(addtitle)
    driver.implicitly_wait(30)
    #旧版本截图
    # driver.find_element(*screen4).click()
    # sleep(2)
    # pyautogui.write(files)
    # sleep(2)
    # pyautogui.press('enter',2)
    #新版本截图
    files=handle_screenshot(driver)
    driver.find_element(*screen4).send_keys(files)
    sleep(2)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//p[text()="上传成功！"]')))
    driver.find_element(*screen5).send_keys(selectproduct)
    sleep(2)
    driver.find_element(*screen6).click()
    sleep(2)
    driver.find_element(*screen7).click()
    driver.implicitly_wait(30)
    driver.find_element(*screen8).click()
    sleep(2)
    return driver

#查询开屏动画
def screenselect(driver,addtitle):
    driver.find_element(*screen9).send_keys(addtitle)
    driver.find_element(*screen10).click()
    sleep(2)
    return driver

#编辑开屏动画
def screenupdate(driver,updatetitle):
    driver.find_element(*screen11).click()
    sleep(2)
    driver.find_element(*screen12).send_keys(updatetitle)
    driver.implicitly_wait(30)
    driver.find_element(*screen13).click()
    sleep(2)
    return driver

#删除开屏动画
def screendelete(driver):
    driver.find_element(*screen14).click()
    sleep(2)
    driver.find_element(*screen15).click()
    driver.implicitly_wait(30)
    driver.find_element(*screen16).click()
    sleep(2)
    return driver

#进入灵犀助手管理
def lingxiassistant(driver):
    # driver.find_element(*adverse1).click()
    # sleep(2)
    driver.find_element(*lingxi1).click()
    sleep(2)
    return driver

#新增灵犀助手
def lingxiassistantadd(driver,addtitle,files,selectproduct,lingxiurl):
    driver.find_element(*lingxi2).click()
    sleep(2)
    driver.find_element(*lingxi3).send_keys(addtitle)
    driver.implicitly_wait(30)
    driver.find_element(*lingxi4).click()
    sleep(2)
    #旧版本截图
    # driver.find_element(*lingxi5).click()
    # sleep(2)
    # pyautogui.write(files)
    # sleep(2)
    # pyautogui.press('enter',2)
    #新版本截图
    files=handle_screenshot(driver)
    driver.find_element(*lingxi5).send_keys(files)
    sleep(2)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//p[text()="上传成功！"]')))
    driver.find_element(*lingxi6).send_keys(lingxiurl)
    sleep(2)
    driver.find_element(*lingxi7).send_keys(selectproduct)
    sleep(2)
    driver.find_element(*lingxi8).click()
    sleep(2)
    driver.find_element(*lingxi9).click()
    driver.implicitly_wait(30)
    driver.find_element(*lingxi10).click()
    sleep(2)
    return driver

#查询灵犀助手
def lingxiassistantselect(driver,addtitle):
    driver.find_element(*lingxi11).send_keys(addtitle)
    driver.find_element(*lingxi12).click()
    sleep(2)
    return driver

#编辑灵犀助手
def lingxiassistantupdate(driver,updatetitle):
    driver.find_element(*lingxi13).click()
    sleep(2)
    driver.find_element(*lingxi14).send_keys(updatetitle)
    driver.implicitly_wait(30)
    driver.find_element(*lingxi15).click()
    sleep(2)
    return driver

#删除灵犀助手
def lingxiassistantdelete(driver):
    driver.find_element(*lingxi16).click()
    sleep(2)
    driver.find_element(*lingxi17).click()
    driver.implicitly_wait(30)
    driver.find_element(*lingxi18).click()
    sleep(2)
    return driver