from random import randint

import allure
import pytest
from cloudsystem_test.config.Border  import  test_CP
from cloudsystem_test.config.deskfile import clear_yaml, read_yaml,generate_random_string

'''
A1产品标准版：限时天卡：100012356854，不限时天卡：100089898989,不限时年卡的3年卡：100095634563，限时年卡的3年卡：100062659686
不限时连续包月：100078787878，限时连续包月：100021358862，限时连续包月*31天：lxby31
A2产品标准版：限时月卡：10008889998，不限时天卡：100088889997，不限时年卡的3年卡：100066262698,限时年卡的3年卡：100095628792
不限时连续包月退订 * 31天：100051616552,不限时连续包月退订直接到期：100099866656
A3产品至尊版：限时月卡：100012365489，不限时月卡:100016516546，不限时连续包月：100065165889，限时连续包月：100085639978
A4产品专业版：限时天卡：100099856639，不限时天卡：100061518899,不限时连续包月：100035158856，限时连续包月：100015366585
A5产品专业版：限时连续包月可用时长60秒：100068485168，限时5天可用时长1分钟：100058484993，限时周卡可用时长1分钟：100098426311
'''
#清空yaml文件
clear_yaml()

@allure.title("用例编号：CJHEX 用例名称：权益开通订购云机")#描述：针对订购云机模块-权益开通订购云机功能测试
def test_case1():
    phone = 18475952281
    channel = 456542123456#202208111713#456542123456
    privateKey ="JHGYUINBVCSDIYR13" #"KD60AB522B384AF7"#"JHGYUINBVCSDIYR13"
    skuCode ="KP01" #"7tian1"
    skuId = 202408149992  # 20240814999
    price = 101


    test_CP().test_ComputingPowerPackage(phone, channel, privateKey, skuCode, skuId, price)
    test_CP().test_ComputingPowerPackage2()

@allure.title("用例编号：CJHEY 用例名称：权益开通退订云机")#描述：针对订购云机模块-权益开通退订云机功能测试
def test_case2():
        phone = 18475952281
        channelCode = 456542123456
        privateKey = "JHGYUINBVCSDIYR13"

        test_CP().test_ComputingPowerPackage3(phone, channelCode, privateKey)
        test_CP().test_ComputingPowerPackage4()

@allure.title("用例编号：CJHEZ 用例名称：政企权益")#描述：针对订购云机模块-政企权益功能测试
def test_case3():
        phone = 18475952281
        channel = 456542123456
        privateKey = 'JHGYUINBVCSDIYR13'
        skuCode = "KP01"
        skuId = 202408149992
        price = 101

        test_CP().test_governmententerprises(phone, channel, privateKey, skuCode, skuId, price)
        test_CP().test_governmententerprises2()


@allure.title("用例编号：CJHF0 用例名称：正向订购")#描述：针对订购云机模块-正向订购功能测试
def test_case4():
        phone = 18475952281
        memberPackageId = "34"
        renewOrderNo = "1925382583770550274"
        channel = "APP"  # 小程序：WXMINIAPP


        test_CP().test_AForwardordering(memberPackageId)
        test_CP().test_AForwardordering2(phone)
        test_CP().test_AForwardordering3(renewOrderNo, channel)#这里的响应需要重点看，少了order
        # test_CP().test_AForwardordering4()#有问题,很难处理，和很多数据关联，需要慢慢研究解决


@allure.title("用例编号：CJHF1 用例名称：第三方正向订购")#描述：针对订购云机模块-第三方正向订购功能测试
def test_case5():
        account = 18475952281
        productItemCode = "S001"
        thirdOrderNo = generate_random_string()
        renewOrderNo = ''
        orderType = "ORDER_BUY"  # 订购：ORDER_BUY，续订：ORDER_RENEW
        channelCode = "345678998765"


        test_CP().test_Thirddirectordering(account, productItemCode, thirdOrderNo, renewOrderNo, orderType,
                                           channelCode)
        test_CP().test_Thirddirectordering2()#这里的响应需要重点看，少了order

        # test_CP().test_Thirddirectordering3()#有问题,很难处理，和很多数据关联，需要慢慢研究解决

@allure.title("用例编号：CJHF2 用例名称：营销订购")#描述：针对订购云机模块-营销订购功能测试
def test_case6():
        account = 18475952281
        productItemCode = "S001"
        # thirdOrderNo = randint(9, 99999999999999999999999999)
        thirdOrderNo = generate_random_string()
        renewOrderNo = ''
        orderType = "ORDER_BUY"  # 订购：ORDER_BUY，续订：ORDER_RENEW
        channelCode = "202208111713"

        test_CP().test_Marketing_platform(account, productItemCode, thirdOrderNo, renewOrderNo, orderType,
                                          channelCode)
        test_CP().test_Marketing_platform2()

@allure.title("用例编号：CJHF3 用例名称：反向订购")#描述：针对订购云机模块-反向订购功能测试
def test_case7():
        phone = 15176797652
        oprType = "01"
        if oprType == "01":
            clear_yaml()
            outOrder = generate_random_string()
            # print(outOrder)
        elif oprType == "03":
            outOrder = read_yaml("P")["reqParam"]["outOrderId"]
            print(outOrder)
        else:
            print("格式有误！")
        outOrderId = outOrder

        test_CP().test_Reverse_order(phone)
        test_CP().test_Reverse_order2(outOrderId, oprType)


@allure.title("用例编号：CJHF4 用例名称：统一认证单点登录和订购")#描述：针对订购云机模块-统一认证单点登录和订购功能测试
def test_case8():
        phone = 15013957569
        channelSrc = "lishuaige"
        skuId = "100099866656"
        key = "A9B8FBE3D048404"  # "KD60AB522B384AF7"#"A9B8FBE3D048404"
        test_CP().qtoken()
        test_CP().test_sign(channelSrc, skuId, key, phone)
        test_CP().test_loginorder(channelSrc,skuId)

if __name__ == '__main__':
    pytest.main(['-vs',"test_order.py"])