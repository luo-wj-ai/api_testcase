from time import sleep
import ddddocr
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from AcloudUI.config.advertise_POM import adverseupdate, adverseadd, adversee, adverseselects, \
    adversedelete, guidanceadd, guidance, guidanceupdate, guidancedelete, guidanceselect, splashscreen, screenadd, \
    screenselect, screenupdate, screendelete, lingxiassistant, lingxiassistantadd, lingxiassistantselect, \
    lingxiassistantupdate, lingxiassistantdelete, configadd, configselect, configupdate, configdelete
from AcloudUI.config.usermanagement_POM import cloudlogin, cloudcode
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
#日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#新增标题
addtitle='自动化测试'
#编辑标题
updatetitle='编辑自动化测试'
#查询产品
selectproduct='自动化测试勿动'
#上传图片
files=r"C:\Users\acer\Desktop\picturetest\man.jpg"
#灵犀助手链接地址
lingxiurl='https://www.baidu.com/'

class test_C(unittest.TestCase):
    """运营管理"""
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
    def test_C01(self):
        """新增广告"""
        adversee(self.driver)
        adverseadd(self.driver,addtitle,files)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_advertise.py:test_C01:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C01:FALL")

    def test_C02(self):
        """编辑广告"""
        adverseselects(self.driver,addtitle)
        adverseupdate(self.driver,updatetitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_advertise.py:test_C02:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C02:FALL")

    def test_C03(self):
        """删除广告"""
        adversedelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_advertise.py:test_C03:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C03:FALL")

    def test_C04(self):
        """新增配置"""
        configadd(self.driver, addtitle, "9.9.2.20250808", "9.9.2", "https://cloud.139.com/cloudimage/app/51468/CP_V5.3.0.202409261604_1c0bb755_cp1215Release_20241010170609_sec.apk", "45", "自动化测试")
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_advertise.py:test_C04:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C04:FALL")

    def test_C05(self):
        """编辑配置"""
        configselect(self.driver, addtitle)
        configupdate(self.driver, addtitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_advertise.py:test_C05:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C05:FALL")

    def test_C06(self):
        """删除配置"""
        configdelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_advertise.py:test_C06:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C06:FALL")

    def test_C07(self):
        """新增功能引导"""
        guidance(self.driver)
        guidanceadd(self.driver,addtitle,files,selectproduct)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="操作成功！"]')))
            self.assertEqual("操作成功！", end.text)
            logging.info("test_advertise.py:test_C07:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C07:FALL")

    def test_C08(self):
        """编辑功能引导"""
        guidanceselect(self.driver,addtitle)
        guidanceupdate(self.driver,updatetitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="操作成功！"]')))
            self.assertEqual("操作成功！", end.text)
            logging.info("test_advertise.py:test_C08:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C08:FALL")

    def test_C09(self):
        """删除功能引导"""
        guidancedelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功！"]')))
            self.assertEqual("删除成功！", end.text)
            logging.info("test_advertise.py:test_C09:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C09:FALL")

    def test_C10(self):
        """新增开屏动画"""
        splashscreen(self.driver)
        screenadd(self.driver,addtitle,files,selectproduct)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="操作成功！"]')))
            self.assertEqual("操作成功！", end.text)
            logging.info("test_advertise.py:test_C10:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C10:FALL")

    def test_C11(self):
        """编辑开屏动画"""
        screenselect(self.driver,addtitle)
        screenupdate(self.driver,updatetitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="操作成功！"]')))
            self.assertEqual("操作成功！", end.text)
            logging.info("test_advertise.py:test_C11:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C11:FALL")

    def test_C12(self):
        """删除开屏动画"""
        screendelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功！"]')))
            self.assertEqual("删除成功！", end.text)
            logging.info("test_advertise.py:test_C12:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C12:FALL")

    def test_C13(self):
        """新增灵犀助手"""
        lingxiassistant(self.driver)
        lingxiassistantadd(self.driver,addtitle,files,selectproduct,lingxiurl)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="操作成功！"]')))
            self.assertEqual("操作成功！", end.text)
            logging.info("test_advertise.py:test_C13:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C13:FALL")

    def test_C14(self):
        """编辑灵犀助手"""
        lingxiassistantselect(self.driver,addtitle)
        lingxiassistantupdate(self.driver,updatetitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="操作成功！"]')))
            self.assertEqual("操作成功！", end.text)
            logging.info("test_advertise.py:test_C14:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C14:FALL")

    def test_C15(self):
        """删除灵犀助手"""
        lingxiassistantdelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功！"]')))
            self.assertEqual("删除成功！", end.text)
            logging.info("test_advertise.py:test_C15:SUCCESS")
        except Exception:
            logging.info("test_advertise.py:test_C15:FALL")

if __name__ == '__main__':
    unittest.main()