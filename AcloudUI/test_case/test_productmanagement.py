import time
from random import randint
from time import sleep
import ddddocr
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from AcloudUI.config.productmanagement_POM import productadd, productselect, productupdate, productdelete, privilegeadd, \
    privilegeselect, privilegeupdate, privilegedelete, productmessage, productitemadd, productitemupdate, \
    productitemdelete, redeemcodeadd, redeemcodegenerate, membercenter, membermenuadd, membermenuselect, \
    membermenuupdate, membermenudelete
from AcloudUI.config.usermanagement_POM import cloudlogin, cloudcode
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
#日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#新增产品名称
addtitle='自动化测试'
#新增产品内部名称
addinternal='自动化测试'
#编辑产品名称
updatetitle='编辑自动化测试'
#编辑产品内部名称
updateaddinternal='编辑自动化测试'
#新增产品编码
addproductcode=randint(100000,999999)
#新增单品编码
addproductitemcode=randint(100000,999999)
#新增产品描述
addcontent='自动化测试'
#新增排序
addsort=9999
#编辑标题
updatetitle='编辑自动化测试'
#查询产品
selectproduct='自动化测试勿动'
#上传图片，这里是相对路径，需要改成绝对路径，我已在里面的代码片段更改，这个就不管了
files=r"C:\Users\acer\Desktop\picturetest\man.jpg"

class test_B(unittest.TestCase):
    """产品管理"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://koophone-cc.cmtest.xyz:8080/cloud-phone-admin/#/login')
        # cloudlogin(cls.driver, "15013957559", "ab123456+")
        cloudlogin(cls.driver, "luoweijie", "Luoweijie:123")
        # img = cls.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div[3]/div/div[2]/img')
        # img.screenshot("2.png")
        # ocr = ddddocr.DdddOcr(old=True)
        # with open("2.png", 'rb') as f:
        #     image = f.read()
        # res = ocr.classification(image)
        # cloudcode(cls.driver, res)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(10)
        cls.driver.quit()

    def test_B01(self):
        """新增产品"""
        productmessage(self.driver)
        productadd(self.driver,addtitle,addinternal,addproductcode,addcontent,addsort)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_productmanagement.py:test_B01:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B01:FALL")

    def test_B02(self):
        """编辑产品"""
        productselect(self.driver, addtitle)
        productupdate(self.driver,updatetitle, updateaddinternal)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_productmanagement.py:test_B02:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B02:FALL")
    def test_B03(self):
        """新增单品"""
        productitemadd(self.driver,addtitle, addinternal, addproductitemcode, addcontent, 1, 0.01)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_productmanagement.py:test_B03:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B03:FALL")
    def test_B04(self):
        """编辑单品"""
        productitemupdate(self.driver, updatetitle, updateaddinternal)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_productmanagement.py:test_B04:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B04:FALL")
    def test_B05(self):
        """删除单品"""
        productitemdelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_productmanagement.py:test_B05:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B05:FALL")
    def test_B06(self):
        """删除产品"""
        productdelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_productmanagement.py:test_B06:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B06:FALL")
    def test_B07(self):
        """新增兑换码批次"""
        redeemcodeadd(self.driver, addtitle, "1", "1")
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_productmanagement.py:test_B07:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B07:FALL")
    def test_B08(self):
        """生成兑换码批次"""
        redeemcodegenerate(self.driver, addtitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="生效成功"]')))
            self.assertEqual("生效成功", end.text)
            logging.info("test_productmanagement.py:test_B08:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B08:FALL")
    def test_B09(self):
        """新增特权"""
        membercenter(self.driver)
        privilegeadd(self.driver, addtitle, addcontent, files)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_productmanagement.py:test_B09:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B09:FALL")
    def test_B10(self):
        """编辑特权"""
        privilegeselect(self.driver, addtitle)
        privilegeupdate(self.driver, updatetitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_productmanagement.py:test_B10:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B10:FALL")
    def test_B11(self):
        """删除特权"""
        privilegedelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_productmanagement.py:test_B11:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B11:FALL")
    def test_B12(self):
        """新增会员套餐管理"""
        membermenuadd(self.driver, addtitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_productmanagement.py:test_B12:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B12:FALL")
    def test_B13(self):
        """编辑会员套餐管理"""
        membermenuselect(self.driver, addtitle)
        membermenuupdate(self.driver, updatetitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_productmanagement.py:test_B13:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B13:FALL")
    def test_B14(self):
        """删除会员套餐管理"""
        membermenudelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_productmanagement.py:test_B14:SUCCESS")
        except Exception:
            logging.info("test_productmanagement.py:test_B14:FALL")
if __name__ == '__main__':
    unittest.main()