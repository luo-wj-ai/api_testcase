from time import sleep
from AcloudUI.common.Avalue import usename, pw, code, logins, usermessage, usermessagelist, add, usertype, phonetype, \
    account, y, ordermessage, orderlists, orderaccount, ordersele, update, update2, choice, y2, repassword, newpassword, \
    newpassword2, y3, off, y4, on, y5, delete, y6, logger, loggeraccount, loggersele, cm1, cm2, cm3, cm4, \
    cm5, cm6, cm7, cm8, userselectaccount, userselecta, cm9, cm11, cm10,cm12, cm13, cm14, cm15, cm16, cm17, cm18, cm19, cm20, cm21, cm22, cm23, cm24, cm25,cm26, cm27, cm28, cm29, cm30, cm31, cm32,cm33

from selenium.webdriver.common.action_chains import ActionChains
#登录页面
def adminname(driver,name):
    return driver.find_element(*usename).send_keys(name)

def adminpassword(driver,password):
    return driver.find_element(*pw).send_keys(password)

def lcode(driver,codes):
    return driver.find_element(*code).send_keys(codes)

def abtn(driver):
    driver.find_element(*logins).click()

def cloudlogin(driver,name,password):
    adminname(driver, name)
    adminpassword(driver, password)
    abtn(driver)
    return driver

def cloudcode(driver,codes):
    lcode(driver,codes)
    abtn(driver)
    return driver

#进入用户管理
def userlist(driver):
    driver.find_element(*usermessage).click()
    driver.implicitly_wait(10)
    return driver

#创建用户
def usemessagelist(driver,useraccount):
    driver.find_element(*usermessagelist).click()
    sleep(2)
    driver.find_element(*add).click()
    driver.implicitly_wait(10)
    driver.find_element(*usertype).click()
    driver.implicitly_wait(10)
    driver.find_element(*phonetype).click()
    driver.implicitly_wait(10)
    driver.find_element(*account).send_keys(useraccount)
    driver.find_element(*y).click()
    sleep(2)
    return driver

#查询用户
def userselects(driver,useraccount):
    driver.find_element(*userselectaccount).send_keys(useraccount)
    driver.find_element(*userselecta).click()
    sleep(2)
    return driver

#编辑用户
def updatee(driver):
    driver.find_element(*update).click()
    sleep(2)
    driver.find_element(*update2).click()
    driver.implicitly_wait(10)
    driver.find_element(*choice).click()
    driver.implicitly_wait(10)
    driver.find_element(*y2).click()
    sleep(2)
    return driver

#重置密码
def repw(driver,rerpassword):
    driver.find_element(*repassword).click()
    sleep(2)
    driver.find_element(*newpassword).send_keys(rerpassword)
    driver.find_element(*newpassword2).send_keys(rerpassword)
    driver.implicitly_wait(10)
    driver.find_element(*y3).click()
    sleep(2)
    return driver

#锁定用户
def lock(driver):
    driver.find_element(*off).click()
    driver.implicitly_wait(10)
    driver.find_element(*y4).click()
    sleep(2)
    return driver

#解锁用户
def unlock(driver):
    driver.find_element(*on).click()
    driver.implicitly_wait(10)
    driver.find_element(*y5).click()
    sleep(2)
    return driver

#删除用户
def deletes(driver):
    driver.find_element(*delete).click()
    driver.implicitly_wait(10)
    driver.find_element(*y6).click()
    sleep(2)
    return driver

#用户登录日志
def loggers(driver,useraccount2):
    # sleep(2)
    # driver.find_element(*usermessage).click()
    driver.find_element(*logger).click()
    sleep(2)
    driver.find_element(*loggeraccount).send_keys(useraccount2)
    driver.find_element(*loggersele).click()
    sleep(3)
    return driver

#分配云机
def cmsadd(driver,useraccount2):
    driver.find_element(*cm1).click()
    sleep(2)
    driver.find_element(*cm2).click()
    sleep(2)
    driver.find_element(*cm3).send_keys(useraccount2)
    driver.find_element(*cm4).click()
    sleep(2)
    #我尝试不再滑动
            # scroll_element = driver.find_element(*cm5)
            # for i in range(16):
            #     actions = ActionChains(driver).click_and_hold(scroll_element)
            #     actions.move_by_offset(0, 200).release().perform()
            #     sleep(1)
    ActionChains(driver).move_to_element(driver.find_element(*cm6)).click().perform()
    driver.implicitly_wait(10)
    driver.find_element(*cm7).click()
    sleep(2)
        # scroll_element2=driver.find_element(*cm8)
        # actions = ActionChains(driver).click_and_hold(scroll_element2)
        # actions.move_by_offset(0, 200).release().perform()
        # driver.implicitly_wait(10)
        # ActionChains(driver).move_to_element(driver.find_element(*cm9)).click().perform()
    driver.find_element(*cm9).click()
    driver.implicitly_wait(10)
    driver.find_element(*cm10).click()
    driver.implicitly_wait(10)
    driver.find_element(*cm11).click()
    sleep(2)
    return driver

#查询云机列表
def cmsselect(driver,useraccount):
    driver.find_element(*cm12).send_keys(useraccount)
    # driver.find_element(*cm13).send_keys(cloudmobilename)
    driver.find_element(*cm14).click()
    sleep(2)
    return driver

#续期云机
def cmsrenew(driver):
    driver.find_element(*cm15).click()
    sleep(2)
    driver.find_element(*cm16).click()
    sleep(2)
    scroll_element = driver.find_element(*cm17)
    for i in range(16):
        actions = ActionChains(driver).click_and_hold(scroll_element)
        actions.move_by_offset(0, 120).release().perform()
        sleep(1)
    ActionChains(driver).move_to_element(driver.find_element(*cm6)).click().perform()
    driver.implicitly_wait(10)
    driver.find_element(*cm19).click()
    sleep(2)
    scroll_element2=driver.find_element(*cm20)
    actions = ActionChains(driver).click_and_hold(scroll_element2)
    actions.move_by_offset(0, 200).release().perform()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(driver.find_element(*cm21)).click().perform()
    driver.implicitly_wait(10)
    driver.find_element(*cm22).click()
    driver.implicitly_wait(10)
    driver.find_element(*cm23).click()
    sleep(2)
    return driver

#变更有效期
def cwupdatetime(driver):
    driver.find_element(*cm24).click()
    sleep(2)
    driver.find_element(*cm25).click()
    sleep(2)
    driver.find_element(*cm26).click()
    sleep(2)
    driver.find_element(*cm27).click()
    sleep(2)
    driver.find_element(*cm28).click()
    sleep(2)
    driver.find_element(*cm29).click()
    sleep(2)
    return driver

# 查看云机详情
def cmselectdetails(driver):
    driver.find_element(*cm30).click()
    sleep(2)
    driver.find_element(*cm31).click()
    sleep(2)
    return driver

# 释放云机
def cmreverse(driver):
    driver.find_element(*cm32).click()
    driver.implicitly_wait(10)
    driver.find_element(*cm33).click()
    sleep(2)
    return driver

#订单列表
def orderlist(driver,useraccount):
    driver.find_element(*ordermessage).click()
    sleep(2)
    driver.find_element(*orderlists).click()
    sleep(2)
    driver.find_element(*orderaccount).send_keys(useraccount)
    driver.find_element(*ordersele).click()
    sleep(3)
    return driver
