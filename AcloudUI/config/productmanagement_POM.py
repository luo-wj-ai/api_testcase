import os
from time import sleep
import pyautogui
from selenium.webdriver import ActionChains
from AcloudUI.common.Avalue import product1, product2, product3, product4, product5, product6, product7, product8, \
    product9, product10, product11, product12, product13, product14, product15, product16, product17, product18, \
    product19, product20, product21, product22, product23, product24, product25, product26, privilege1, privilege2, \
    privilege3, privilege4, privilege5, privilege6, privilege7, privilege8, privilege9, privilege10, privilege11, \
    privilege12, privilege13, privilege14, productitem1, productitem2, productitem3, productitem4, productitem5, \
    productitem6, productitem7, productitem8, productitem9, productitem10, productitem11, productitem12, productitem13, \
    productitem14, productitem15, productitem16, productitem17, productitem18, productitem19, product27, productitem20, \
    redeemcode2, redeemcode1, redeemcode3, redeemcode4, redeemcode5, redeemcode6, redeemcode7, redeemcode8, redeemcode9, \
    redeemcode10, redeemcode11, redeemcode12, redeemcode13, redeemcode14, redeemcode15, redeemcode16, redeemcode17, \
    redeemcode18, redeemcode19, redeemcode20, redeemcode21, redeemcode22, redeemcode23, redeemcode24, membermenu1, \
    membermenu2, membermenu3, membermenu4, membermenu5, membermenu6, membermenu7, membermenu8, membermenu9, \
    membermenu10, membermenu11, membermenu12, membermenu13, membermenu14, membermenu15, membermenu16, membermenu17, \
    membermenu18, membermenu19, membermenu20, membermenu21, membermenu22, membermenu23


#进入产品管理
def productmessage(driver):
    driver.find_element(*product1).click()
    sleep(2)
    return driver

#新增产品
def productadd(driver,addtitle,addinternal,addproductcode,addcontent,addsort):

    driver.find_element(*product2).click()
    sleep(2)
    driver.find_element(*product3).click()
    sleep(2)
    driver.find_element(*product4).send_keys(addtitle)
    driver.find_element(*product5).send_keys(addinternal)
    driver.find_element(*product6).send_keys(addproductcode)
    driver.implicitly_wait(30)
    driver.find_element(*product7).click()
    driver.implicitly_wait(30)
    driver.find_element(*product8).click()
    driver.implicitly_wait(30)
    driver.find_element(*product9).click()
    driver.implicitly_wait(30)
    driver.find_element(*product10).click()
    driver.implicitly_wait(30)
    ActionChains(driver).move_to_element(driver.find_element(*product11)).click().perform()
    driver.implicitly_wait(30)
    driver.find_element(*product12).send_keys(addsort)
    driver.implicitly_wait(30)
    driver.find_element(*product13).click()
    sleep(2)
    driver.find_element(*product14).click()
    driver.implicitly_wait(30)
    driver.find_element(*product15).send_keys(addcontent)
    driver.implicitly_wait(30)
    driver.find_element(*product16).click()
    sleep(2)
    return driver

#查询产品
def productselect(driver,addtitle):
    driver.find_element(*product17).send_keys(addtitle)
    driver.find_element(*product18).click()
    sleep(2)
    driver.find_element(*product19).click()
    driver.implicitly_wait(30)
    driver.find_element(*product20).click()
    sleep(2)
    return driver

#编辑产品
def productupdate(driver,updatetitle,updateaddinternal):
    driver.find_element(*product21).click()
    sleep(2)
    driver.find_element(*product22).send_keys(updatetitle)
    driver.find_element(*product23).send_keys(updateaddinternal)
    driver.implicitly_wait(30)
    driver.find_element(*product24).click()
    sleep(2)
    return driver

#删除产品
def productdelete(driver):
    driver.find_element(*product25).click()
    sleep(2)
    driver.find_element(*product26).click()
    driver.implicitly_wait(30)
    driver.find_element(*product27).click()
    sleep(2)
    return driver

#新增单品
def productitemadd(driver,addtitle,addinternal,addproductitemcode,addcontent,times,price):

    driver.find_element(*productitem1).click()
    sleep(2)
    driver.find_element(*productitem2).click()
    sleep(2)
    driver.find_element(*productitem3).send_keys(addtitle)
    driver.find_element(*productitem4).send_keys(addinternal)
    driver.find_element(*productitem5).send_keys(addproductitemcode)
    driver.implicitly_wait(30)
    driver.find_element(*productitem6).click()
    sleep(2)
    driver.find_element(*productitem7).click()
    driver.implicitly_wait(30)
    driver.find_element(*productitem8).send_keys(addcontent)
    driver.implicitly_wait(30)
    driver.find_element(*productitem9).send_keys(times)
    sleep(2)
    driver.find_element(*productitem10).click()
    sleep(2)
    driver.find_element(*productitem11).click()
    driver.implicitly_wait(30)
    driver.find_element(*productitem12).send_keys(price)
    driver.find_element(*productitem13).send_keys(addcontent)
    driver.implicitly_wait(30)
    driver.find_element(*productitem14).click()
    sleep(2)
    return driver

#编辑单品
def productitemupdate(driver,updatetitle,updateaddinternal):
    driver.find_element(*productitem15).click()
    sleep(2)
    driver.find_element(*productitem16).send_keys(updatetitle)
    driver.find_element(*productitem17).send_keys(updateaddinternal)
    driver.implicitly_wait(30)
    driver.find_element(*productitem18).click()
    sleep(2)
    return driver

#删除单品
def productitemdelete(driver):
    driver.find_element(*productitem19).click()
    driver.implicitly_wait(30)
    driver.find_element(*productitem20).click()
    sleep(2)
    return driver

#新增兑换码批次
def redeemcodeadd(driver,addtitle,codenumber,limitusernumber):
    driver.find_element(*redeemcode1).click()
    sleep(2)
    driver.find_element(*redeemcode2).click()
    sleep(2)
    driver.find_element(*redeemcode3).send_keys(addtitle)
    driver.find_element(*redeemcode4).click()
    sleep(2)
    scroll_element=driver.find_element(*redeemcode5)
    # 当前设置为 range(0)，循环不会执行
    for i in range(0):
        action=ActionChains(driver).click_and_hold(scroll_element)
        action.move_by_offset(0,180).release().perform()
        sleep(1)
    ActionChains(driver).move_to_element(driver.find_element(*redeemcode6)).click().perform()
    driver.implicitly_wait(30)
    driver.find_element(*redeemcode7).click()
    sleep(2)
    # 当前设置为 range(0)，循环不会执行
    # scroll_element2=driver.find_element(*redeemcode8)
    # action=ActionChains(driver).click_and_hold(scroll_element2)
    # action.move_by_offset(0,200).release().perform()
    driver.implicitly_wait(30)
    ActionChains(driver).move_to_element(driver.find_element(*redeemcode9)).click().perform()
    driver.implicitly_wait(30)
    driver.find_element(*redeemcode10).click()
    sleep(2)
    driver.find_element(*redeemcode11).click()
    sleep(2)
    driver.find_element(*redeemcode12).send_keys(codenumber)
    driver.find_element(*redeemcode13).click()
    sleep(2)
    driver.find_element(*redeemcode14).click()
    sleep(2)
    driver.find_element(*redeemcode15).click()
    sleep(2)
    driver.find_element(*redeemcode16).click()
    sleep(2)
    driver.find_element(*redeemcode17).click()
    sleep(2)
    driver.find_element(*redeemcode18).click()
    sleep(2)
    driver.find_element(*redeemcode19).send_keys(limitusernumber)
    driver.implicitly_wait(30)
    driver.find_element(*redeemcode20).click()
    sleep(2)
    return driver

#生成兑换码批次
def redeemcodegenerate(driver,addtitle):
    driver.find_element(*redeemcode21).send_keys(addtitle)
    driver.find_element(*redeemcode22).click()
    sleep(2)
    driver.find_element(*redeemcode23).click()
    driver.implicitly_wait(30)
    driver.find_element(*redeemcode24).click()
    sleep(2)
    return driver

#进入会员中心
def membercenter(driver):
    driver.find_element(*privilege1).click()
    sleep(2)
    return driver

#新增特权
def privilegeadd(driver,addtitle,addcontent,files):
    driver.find_element(*privilege2).click()
    sleep(2)
    driver.find_element(*privilege3).click()
    sleep(2)
    driver.find_element(*privilege4).send_keys(addtitle)
    driver.find_element(*privilege5).send_keys(addcontent)
    driver.implicitly_wait(30)
    #上传文件 旧
        # driver.find_element(*privilege6).click()
        # sleep(2)
        # pyautogui.write(files)
        # sleep(3)
        # pyautogui.press("enter",2)
    # 上传文件 新
    screenshot_path = './temp_screenshot.png'
    driver.save_screenshot(screenshot_path)
    driver.find_element(*privilege6).send_keys(os.path.abspath(screenshot_path))
    # 3. 删除截图
    sleep(1)  # 等待上传完成，视情况加不加
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
    sleep(2)
    driver.find_element(*privilege7).click()
    sleep(2)
    return driver

#查询特权
def privilegeselect(driver, addtitle):
    driver.find_element(*privilege8).send_keys(addtitle)
    driver.find_element(*privilege9).click()
    sleep(2)
    return driver

#编辑特权
def privilegeupdate(driver, updatetitle):
    driver.find_element(*privilege10).click()
    sleep(2)
    driver.find_element(*privilege11).send_keys(updatetitle)
    driver.implicitly_wait(30)
    driver.find_element(*privilege12).click()
    sleep(2)
    return driver

#删除特权
def privilegedelete(driver):
    driver.find_element(*privilege13).click()
    driver.implicitly_wait(30)
    driver.find_element(*privilege14).click()
    sleep(2)
    return driver

#新增会员套餐管理
def membermenuadd(driver,addtitle):
    driver.find_element(*membermenu1).click()
    sleep(2)
    driver.find_element(*membermenu2).click()
    sleep(2)
    driver.find_element(*membermenu3).send_keys(addtitle)
    driver.find_element(*membermenu4).click()
    sleep(2)
    scroll_element=driver.find_element(*membermenu5)
    # 当前设置为 range(0)，循环不会执行
    for i in range(0):
        action=ActionChains(driver).click_and_hold(scroll_element)
        action.move_by_offset(0,200).release().perform()
        sleep(1)
    ActionChains(driver).move_to_element(driver.find_element(*membermenu6)).click().perform()
    driver.implicitly_wait(30)
    driver.find_element(*membermenu7).click()
    sleep(2)
    # 当前设置为 range(0)，循环不会执行
    # scroll_element2=driver.find_element(*membermenu8)
    # action=ActionChains(driver).click_and_hold(scroll_element2)
    # action.move_by_offset(0,200).release().perform()
    driver.implicitly_wait(30)
    ActionChains(driver).move_to_element(driver.find_element(*membermenu9)).click().perform()
    driver.implicitly_wait(30)
    driver.find_element(*membermenu10).click()
    sleep(2)
    driver.find_element(*membermenu11).click()
    sleep(2)
    driver.find_element(*membermenu12).click()
    sleep(2)
    driver.find_element(*membermenu13).click()
    sleep(2)
    driver.find_element(*membermenu14).click()
    sleep(2)
    driver.find_element(*membermenu15).click()
    sleep(2)
    driver.find_element(*membermenu16).click()
    sleep(2)
    return driver

#查询会员套餐管理
def membermenuselect(driver,addtitle):
    driver.find_element(*membermenu17).send_keys(addtitle)
    driver.find_element(*membermenu18).click()
    sleep(2)
    return driver

#编辑会员套餐管理
def membermenuupdate(driver,updatetitle):
    driver.find_element(*membermenu19).click()
    sleep(2)
    driver.find_element(*membermenu20).send_keys(updatetitle)
    driver.implicitly_wait(30)
    driver.find_element(*membermenu21).click()
    sleep(2)
    return driver

#删除会员套餐管理
def membermenudelete(driver):
    driver.find_element(*membermenu22).click()
    driver.implicitly_wait(30)
    driver.find_element(*membermenu23).click()
    sleep(2)