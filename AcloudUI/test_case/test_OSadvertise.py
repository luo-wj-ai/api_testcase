from time import sleep
import ddddocr
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from AcloudUI.config.OSadvertise_POM import osadvertise, osadvertiseadd, osadvertiseselect, osadvertiseupdate, \
    osadvertisedelete, themeadd, themeselect, themeupdate, themedelete, wallpaperadd, wallpaperselect, wallpaperupdate, \
    wallpaperdelete, widgetadd, widgetselect, widgetupdate, widgetdelete, applicationadd, applicationselect, \
    applicationdelete, messageadd

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
#上传图片,已在代码里面修改了相对路径
files=r"C:\Users\acer\Desktop\picturetest\man.jpg"
#上传主题包,已在代码里面修改了相对路径
filesgnz=r"C:\Users\acer\Desktop\picturetest\test.gnz"
#上传应用,需要针对这个绝对路径，实时更改apk
fileapp=r"C:\Users\luo\Downloads\test.apk"
#链接地址
osurl='https://www.baidu.com/'
#消息内容
addcontent='自动化测试'
#用户号码
addaccount='15013957569'

class test_D(unittest.TestCase):
    """OS运营管理"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://koophone-cc.cmtest.xyz:8080/cloud-phone-admin/#/login')
        cloudlogin(cls.driver, "luoweijie", "Password:123")
        # img = cls.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div[3]/div/div[2]/img')
        # img.screenshot("2.png")
        # ocr = ddddocr.DdddOcr(old=True)
        # with open("2.png", 'rb') as f:
        #     image = f.read()
        # res = ocr.classification(image)
        # cloudcode(cls.driver, res)
        cls.driver.implicitly_wait(10)

    # #调试模式
    # @classmethod
    # def setUpClass(cls) -> None:
    #     options = Options()
    #     options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    #     cls.driver = webdriver.Chrome(options=options)


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(2)
        cls.driver.quit()

    def test_D01(self):
        """新增OS广告"""
        osadvertise(self.driver)
        osadvertiseadd(self.driver,addtitle,osurl)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_OSadvertise.py:test_D01:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D01:FALL")
    def test_D02(self):
        """编辑OS广告"""
        osadvertiseselect(self.driver)
        osadvertiseupdate(self.driver,updatetitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_OSadvertise.py:test_D02:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D02:FALL")
    def test_D03(self):
        """删除OS广告"""
        osadvertisedelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_OSadvertise.py:test_D03:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D03:FALL")
    def test_D04(self):
        """新增主题"""
        themeadd(self.driver,addtitle,files,filesgnz)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_OSadvertise.py:test_D04:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D04:FALL")
    def test_D05(self):
        """编辑主题"""
        themeselect(self.driver,addtitle)
        themeupdate(self.driver,updatetitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_OSadvertise.py:test_D05:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D05:FALL")
    def test_D06(self):
        """删除主题"""
        themedelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_OSadvertise.py:test_D06:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D06:FALL")
    def test_D07(self):
        """新增壁纸"""
        wallpaperadd(self.driver,addtitle,files)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_OSadvertise.py:test_D07:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D07:FALL")
    def test_D08(self):
        """编辑壁纸"""
        wallpaperselect(self.driver,addtitle)
        wallpaperupdate(self.driver,updatetitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_OSadvertise.py:test_D08:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D08:FALL")
    def test_D09(self):
        """删除壁纸"""
        wallpaperdelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_OSadvertise.py:test_D09:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D09:FALL")
    def test_D10(self):
        """新增小组件"""
        widgetadd(self.driver,addtitle,files)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_OSadvertise.py:test_D10:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D10:FALL")
    def test_D11(self):
        """编辑小组件"""
        widgetselect(self.driver,addtitle)
        widgetupdate(self.driver,updatetitle)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="修改成功"]')))
            self.assertEqual("修改成功", end.text)
            logging.info("test_OSadvertise.py:test_D11:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D11:FALL")
    def test_D12(self):
        """删除小组件"""
        widgetdelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_OSadvertise.py:test_D12:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D12:FALL")
    def test_D13(self):
        """新增应用"""
        applicationadd(self.driver,fileapp,addtitle,files)
        try:
            end = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_OSadvertise.py:test_D13:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D13:FALL")
    def test_D14(self):
        """删除应用"""
        applicationselect(self.driver,addtitle)
        applicationdelete(self.driver)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="删除成功"]')))
            self.assertEqual("删除成功", end.text)
            logging.info("test_OSadvertise.py:test_D14:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D14:FALL")
    def test_D15(self):
        """消息管理-消息列表"""
        messageadd(self.driver, addtitle, addcontent, addaccount)
        try:
            end = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//p[text()="新增成功"]')))
            self.assertEqual("新增成功", end.text)
            logging.info("test_OSadvertise.py:test_D15:SUCCESS")
        except Exception:
            logging.info("test_OSadvertise.py:test_D15:FALL")

if __name__ == '__main__':
    unittest.main()