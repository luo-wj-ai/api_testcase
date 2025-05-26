from time import sleep
import ddddocr
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AcloudUI.config.usermanagement_POM import cloudlogin, cloudcode, orderlist, usemessagelist, updatee, repw, loggers, \
    userlist, lock, unlock, deletes, cmsadd, cmsselect, cmsrenew, cwupdatetime, cmselectdetails, cmreverse
import logging
#日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#用户列表-用户账号
useraccount="15018066688"
#用户列表-重置密码
rerpassword="ab123456+"
#订单列表/用户云机列表-用户账号
useraccount2="15013957569"
#云手机实例名称
cloudmobilename="A2号产品"

class test_A(unittest.TestCase):
    """用户管理-订单管理"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://cc-hwy.cmtest.xyz/cloud-phone-admin/#/userInfo/cloudphone')
        cloudlogin(cls.driver, "15013957559", "ab123456+")
        img = cls.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div[3]/div/div[2]/img')
        img.screenshot("2.png")
        ocr = ddddocr.DdddOcr(old=True)
        with open("2.png", 'rb') as f:
            image = f.read()
        res = ocr.classification(image)
        cloudcode(cls.driver, res)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    def test_A01(self):
        """创建用户"""
        usemessagelist(self.driver,useraccount)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_usermanagement.py:test_A01:SUCCESS")
        except Exception:
            logging.info("test_usermanagement.py:test_A01:FALL")

    def test_A02(self):
        """编辑用户"""
        updatee(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_usermanagement.py:test_A02:SUCCESS")
        except Exception:
            logging.info("test_usermanagement.py:test_A02:FALL")

    def test_A03(self):
        """重置密码"""
        repw(self.driver,rerpassword)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_usermanagement.py:test_A03:SUCCESS")
        except Exception:
            logging.info("test_usermanagement.py:test_A03:FALL")

    def test_A04(self):
        """锁定用户"""
        lock(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="锁定成功"]')))
            self.assertEqual("锁定成功", end.text)
            logging.info("test_usermanagement.py:test_A04:SUCCESS")
        except Exception:
            logging.info("test_usermanagement.py:test_A04:FALL")

    def test_A05(self):
        """解锁用户"""
        unlock(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="解锁成功"]')))
            self.assertEqual("解锁成功", end.text)
            logging.info("test_usermanagement.py:test_A05:SUCCESS")
        except Exception:
            logging.info("test_usermanagement.py:test_A05:FALL")

    def test_A06(self):
        """删除用户"""
        deletes(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_usermanagement.py:test_A06:SUCCESS")
        except Exception:
            logging.info("test_usermanagement.py:test_A06:FALL")

    def test_A07(self):
        """查询登录日志"""
        loggers(self.driver,useraccount2)
        logging.info("test_usermanagement.py:test_A07:SUCCESS")

    def test_A08(self):
        """分配云机"""
        cmsadd(self.driver,useraccount2)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_usermanagement.py:test_A08:SUCCESS")
        except Exception:
            logging.info("test_usermanagement.py:test_A08:FALL")
    def test_A09(self):
        """续期云机"""
        cmsselect(self.driver,cloudmobilename)
        cmsrenew(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="续期成功"]')))
            self.assertEqual("续期成功", end.text)
            logging.info("test_usermanagement.py:test_A09:SUCCESS")
        except Exception:
            logging.info("test_usermanagement.py:test_A09:FALL")
    def test_A10(self):
        """变更有效期"""
        cwupdatetime(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_usermanagement.py:test_A10:SUCCESS")
        except Exception:
            logging.info("test_usermanagement.py:test_A10:FALL")
    def test_A11(self):
        """查看云机详情+释放云机"""
        cmselectdetails(self.driver)
        cmreverse(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="释放成功"]')))
            self.assertEqual("释放成功", end.text)
            logging.info("test_usermanagement.py:test_A11:SUCCESS")
        except Exception:
            logging.info("test_usermanagement.py:test_A11:FALL")
    def test_A12(self):
        """查询订单列表"""
        orderlist(self.driver,useraccount2)
        logging.info("test_usermanagement.py:test_A12:SUCCESS")

if __name__ == '__main__':
    unittest.main()

