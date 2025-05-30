import allure
import pytest
import requests
from cloudsystem_test.common.Aheaders import h, Get_Authorization
from cloudsystem_test.common.Assert import assert_response_time
from cloudsystem_test.common.Aurl import baseurl
import json
from cloudsystem_test.config.Amobile import generate_phone_number
from cloudsystem_test.config.dataportal import write_yaml, read_yaml, clear_yaml
import logging

#云手机运营后台token
headers02=h(update=True)
headers=h()
#清空yaml文件
clear_yaml()
#配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@allure.title("用例编号：CJHCZ 用例名称：创建用户")#描述：针对用户管理模块-创建用户功能测试
def test_case1():
    url=baseurl+"/portal/system/user/create"
    data={
    "account":generate_phone_number(),#一个方法
    "accountType": "MOBILE",
    "password":"ab123456+"
}
    res = requests.post(url=url, json=data, headers=headers02)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case1:SUCCESS")
        userid = result["data"]["respSubs"]["userId"]
        account = result["data"]["respSubs"]["account"]
        datas = {"userId": userid,
                 "username": account}
        write_yaml(datas)
        print("\nc测试完成：",datas)
    except Exception :
        logging.error("test_Ausermanagement.py:test_case1:FALL")

@allure.title("用例编号：CJHD0 用例名称：查询用户列表")#描述：针对用户管理模块-查询用户列表功能测试
def test_case2():
    url=baseurl+"/portal/system/user/query"
    data={"pageSize":10,
        "pageNumber":1,
        "account":read_yaml("username")}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case2:SUCCESS")
    except Exception:
        logging.info("test_Ausermanagement.py:test_case2:FALL")

@allure.title("用例编号：CJHD1 用例名称：修改用户")#描述：针对用户管理模块-修改用户功能测试
def test_case3():
    url=baseurl+"/portal/system/user/update"
    data={
    "userId": read_yaml("userId"),
    "level": "VIP",
    "mobile": read_yaml("username")
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case3:SUCCESS")
    except Exception:
        logging.info("test_Ausermanagement.py:test_case3:FALL")

@allure.title("用例编号：CJHD2 用例名称：修改用户密码")#描述：针对用户管理模块-修改用户密码功能测试
def test_case4():
    url=baseurl+"/portal/system/user/update/password"
    data={
    "userId": read_yaml("userId"),
    "account": read_yaml("username"),
    "tempPassword": "ab123456-"
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case4:SUCCESS")
    except Exception:
        logging.info("test_Ausermanagement.py:test_case4:FALL")

@allure.title("用例编号：CJHD3 用例名称：锁定用户")#描述：针对用户管理模块-锁定用户功能测试
def test_case5():
    url=baseurl+"/portal/system/user/lock"
    data = {
        "userId": read_yaml("userId")
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    assert "成功" in result["header"]["errMsg"]
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case5:SUCCESS")
    except Exception:
        logging.info("test_Ausermanagement.py:test_case5:FALL")

@allure.title("用例编号：CJHD4 用例名称：解锁用户")#描述：针对用户管理模块-解锁用户功能测试
def test_case6():
    url=baseurl+"/portal/system/user/unlock"
    data = {
        "userId": read_yaml("userId")
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case6:SUCCESS")
    except Exception:
        logging.info("test_Ausermanagement.py:test_case6:FALL")

@allure.title("用例编号：CJHD5 用例名称：删除用户")#描述：针对用户管理模块-删除用户功能测试
def test_case7():
    url=baseurl+"/portal/system/user/delete"
    data={
    "userId": read_yaml("userId")
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case7:SUCCESS")
    except Exception:
        logging.info("test_Ausermanagement.py:test_case7:FALL")

@allure.title("用例编号：CJHD6 用例名称：查询用户登录日志")#描述：针对用户管理模块-查询用户登录日志功能测试
def test_case8():
    url=baseurl+"/portal/system/user/loginLogs"
    data={
    "pageNumber": 1,
    "pageSize": 10,
    "account": "15013957569",
    "startTime": "2024-11-01 00:00:00",
    "endTime": "2024-11-29 23:59:59"
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case8:SUCCESS")
    except Exception:
        logging.info("test_Ausermanagement.py:test_case8:FALL")

@allure.title("用例编号：CJHD7 用例名称：云机列表分配云机")#描述：针对用户管理模块-云机列表分配云机功能测试
def test_case9():
    url=baseurl+"/portal/system/order/createVvipInstance"

    data={
        "account": 15107612187,
        "productId": 1921841985090879489,
        "productItemId": 1921844563719618561,
        "productItemName": "至尊版月卡"
    }

    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case9:SUCCESS")
        datas = {"account": data["account"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_Ausermanagement.py:test_case9:FALL")

@allure.title("用例编号：CJHD8 用例名称：查询云机列表")#描述：针对用户管理模块-查询云机列表功能测试
def test_case10():
    url=baseurl+"/portal/system/device/list"
    data={
    "pageNumber": 1,
    "pageSize": 10,
    "sorts": [
        {
            "sortField": "createTime",
            "sortOrder": "DESC"
        }
    ],
    "subsAccount": read_yaml("account"),
    "status":"ACTIVE"
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case10:SUCCESS")
        instanceId = result["data"]["data"][0]["cloudMachineId"]
        datas = {"instanceId": instanceId}
        write_yaml(datas)
    except Exception:
        logging.info("test_Ausermanagement.py:test_case10:FALL")

@allure.title("用例编号：CJHD9 用例名称：续期云机")#描述：针对用户管理模块-续期云机功能测试
def test_case11():
    url=baseurl+"/portal/system/order/renewInstance"
    data={"instanceId":read_yaml("instanceId"),
          "account":read_yaml("account"),
          "productId":"1747870700813025282",
          "productItemId":"1747870976919863297"}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case11:SUCCESS")
    except Exception:
        logging.info("test_Ausermanagement.py:test_case11:FALL")

@allure.title("用例编号：CJHDA 用例名称：云机变更有效期")#描述：针对用户管理模块-云机变更有效期功能测试
def test_case12():
    url=baseurl+"/portal/system/order/upadateVvipOrders"
    data={
    "account": read_yaml("account"),
    "resourceId": read_yaml("instanceId"),
    "endTime": "2025-01-29 23:59:59"
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case12:SUCCESS")
    except Exception:
        logging.info("test_Ausermanagement.py:test_case12:FALL")

@allure.title("用例编号：CJHDB 用例名称：释放云机")#描述：针对用户管理模块-释放云机功能测试
def test_case13():
    url=baseurl+"/portal/system/order/removeVvipOrders"
    data={
    "account": read_yaml("account"),
    "resourceId": read_yaml("instanceId")
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    #断言响应时间加的新需求
    assert_response_time(res, max_ms=400)  # 👈 调用封装的断言方法
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Ausermanagement.py:test_case13:SUCCESS")
    except Exception:
        logging.info("test_Ausermanagement.py:test_case13:FALL")

if __name__ == '__main__':
    pytest.main(['-vs',"test_Ausermanagement.py"])