import unittest
from HTMLTestRunner import HTMLTestRunner
from AcloudUI.config.Afilename import filenamechange
from AcloudUI.test_case.test_OSadvertise import test_D
from AcloudUI.test_case.test_SmartDesktopIntegration import test_E
from AcloudUI.test_case.test_advertise import test_C
from AcloudUI.test_case.test_productmanagement import test_B
from AcloudUI.test_case.test_usermanagement import test_A

if __name__ == '__main__':
    # 创建一个测试用例池
    suite = unittest.TestSuite()
    # 创建一个加载测试用例的对象
    loader = unittest.TestLoader()
    # 加载要测试的测试用例
    suite.addTest(loader.loadTestsFromTestCase(test_A))
    # suite.addTest(loader.loadTestsFromTestCase(test_B))
    # suite.addTest(loader.loadTestsFromTestCase(test_C))
    # suite.addTest(loader.loadTestsFromTestCase(test_D))
    # suite.addTest(loader.loadTestsFromTestCase(test_E))
    # 生成新的文件目录
    newfilepath = '../AcloudUI/report/' + filenamechange('.html')
    # 运行并生成报告
    with open(newfilepath, 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=1, title="云手机能力中心平台自动化测试")
        runner.run(suite)


