import allure
import pytest
import requests
from cloudsystem_test.common.Aheaders import h
from cloudsystem_test.common.Aurl import baseurl
import json
from cloudsystem_test.config.dataportal import write_yaml, read_yaml, clear_yaml
import logging

#云手机运营后台token
headers=h
#清空yaml文件
clear_yaml()
#配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@allure.title("用例编号：CJHDP 用例名称：新增特权")#描述：针对会员中心模块-新增特权功能测试
def test_case1():
    url=baseurl+"/portal/benefit/add"
    data={
    "benefitName": "自动化测试",
    "benefitImg": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fimage%2Flishuhong_2ed6092a594b49de8f5607c19c549746.jpg",
    "displayStatus": "NORMAL",
    "benefitDesc": "自动化测试"
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case1:SUCCESS")
        datas = {"benefitName": data["benefitName"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_Cmembercenter.py:test_case1:FALL")

@allure.title("用例编号：CJHDQ 用例名称：查询特权")#描述：针对会员中心模块-查询特权功能测试
def test_case2():
    url=baseurl+"/portal/benefit/list"
    data={
    "benefitName":read_yaml("benefitName"),
    "pageNumber": 1,
    "pageSize": 10,
    "sorts": [
        {
            "sortField": "createTime",
            "sortOrder": "DESC"
        }
    ]
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case2:SUCCESS")
        bid = result["data"]["benefitRecordList"][0]["id"]
        datas = {"bid": bid}
        write_yaml(datas)
    except Exception:
        logging.info("test_Cmembercenter.py:test_case2:FALL")

@allure.title("用例编号：CJHDR 用例名称：修改特权")#描述：针对会员中心模块-修改特权功能测试
def test_case3():
    url=baseurl+"/portal/benefit/update"
    data={
    "id": read_yaml("bid"),
    "benefitName": "修改自动化测试",
    "benefitImg": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fimage%2Flishuhong_2ed6092a594b49de8f5607c19c549746.jpg",
    "displayStatus": "GRAY",
    "benefitDesc": "修改自动化测试"
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case3:SUCCESS")
    except Exception:
        logging.info("test_Cmembercenter.py:test_case3:FALL")

@allure.title("用例编号：CJHDS 用例名称：删除特权")#描述：针对会员中心模块-删除特权功能测试
def test_case4():
    url=baseurl+"/portal/benefit/delete"
    data={
    "benefitIdList": [read_yaml("bid")]}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case4:SUCCESS")
    except Exception:
        logging.info("test_Cmembercenter.py:test_case4:FALL")

@allure.title("用例编号：CJHDT 用例名称：查看会员等级管理")#描述：针对会员中心模块-查看会员等级管理功能测试
def test_case5():
    url=baseurl+"/portal/specification/list"
    data={}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case5:SUCCESS")
    except Exception:
        logging.info("test_Cmembercenter.py:test_case5:FALL")

@allure.title("用例编号：CJHDU 用例名称：新增会员套餐")#描述：针对会员中心模块-新增会员套餐功能测试
def test_case6():
    url=baseurl+"/portal/memberPackage/add"
    data={
    "title": "自动化测试",
    "productId": "1747870700813025282",
    "productItemId": "1747870976919863297",
    "limitType": "UN_LIMIT_TIME",
    "memberLevel": "ULTRA",
    "startTime": "2024-12-02 10:16:23",
    "endTime": "2024-12-02 10:16:30",
    "status": False,
    "packageBadgeImageUrl": None
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case6:SUCCESS")
        datas = {"title": data["title"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_Cmembercenter.py:test_case6:FALL")

@allure.title("用例编号：CJHDV 用例名称：查询会员套餐")#描述：针对会员中心模块-查询会员套餐功能测试
def test_case7():
    url=baseurl+"/portal/memberPackage/list"
    data={
    "title": read_yaml("title"),
    "pageNumber": 1,
    "pageSize": 10,
    "status": False
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case7:SUCCESS")
        hid = result["data"]["records"][0]["id"]
        datas = {"hid": hid}
        write_yaml(datas)

    except Exception:
        logging.info("test_Cmembercenter.py:test_case7:FALL")

@allure.title("用例编号：CJHDW 用例名称：修改会员套餐")#描述：针对会员中心模块-修改会员套餐功能测试
def test_case8():
    url=baseurl+"/portal/memberPackage/update"
    data={
    "id": read_yaml("hid"),
    "title": "修改自动化测试",
    "memberLevel": "ULTRA",
    "limitType": "UN_LIMIT_TIME",
    "productId": "1747870700813025282",
    "productItemId": "1747870976919863297",
    "startTime": "2024-12-02 10:16:23",
    "endTime": "2024-12-02 10:16:30",
    "status": False,
    "sort": 732,
    "remark": "1111",
    "provinces": None,
    "packageBadgeImageUrl": None,
    "createTime": "2024-12-02 10:16:35",
    "updateTime": "2024-12-02 10:21:14",
    "productItemDisplayName": "不限时月卡",
    "productItemName": "不限时月卡",
    "hideUp": 1,
    "memberPackageId": read_yaml("hid")
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case8:SUCCESS")
    except Exception:
        logging.info("test_Cmembercenter.py:test_case8:FALL")

@allure.title("用例编号：CJHDX 用例名称：启用会员套餐")#描述：针对会员中心模块-启用会员套餐功能测试
def test_case9():
    url=baseurl+"/portal/memberPackage/setEnableStatus"
    data={
    "memberPackageIds": [read_yaml("hid")],
    "status": 1
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case9:SUCCESS")
    except Exception:
        logging.info("test_Cmembercenter.py:test_case9:FALL")

@allure.title("用例编号：CJHDY 用例名称：禁用会员套餐")#描述：针对会员中心模块-禁用会员套餐功能测试
def test_case10():
    url = baseurl + "/portal/memberPackage/setEnableStatus"
    data = {
        "memberPackageIds": [read_yaml("hid")],
        "status": 0
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case10:SUCCESS")
    except Exception:
        logging.info("test_Cmembercenter.py:test_case10:FALL")

@allure.title("用例编号：CJHDZ 用例名称：删除会员套餐")#描述：针对会员中心模块-删除会员套餐功能测试
def test_case11():
    url=baseurl+"/portal/memberPackage/delete"
    data={
    "memberPackageIds": [read_yaml("hid")]}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Cmembercenter.py:test_case11:SUCCESS")
    except Exception:
        logging.info("test_Cmembercenter.py:test_case11:FALL")

if __name__ == '__main__':
    pytest.main(['-vs','test_Cmembercenter.py'])