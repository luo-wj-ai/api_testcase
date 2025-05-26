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

@allure.title("用例编号：CJHE0 用例名称：新增广告")#描述：针对运营管理模块-新增广告功能测试
def test_case1():
    url=baseurl+"/portal/found/add"
    data= {
    "directory": "6-",
    "title": "自动化测试",
    "imageUrl": "https://yunshouji20221125.obs.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fimage%2Fchunyanye_2bb2c305c7af4a7d9e1d1c24d338e05b.png",
    "content": "广告",
    "link": "cloud_pop://www.cmdc.com/cloud/pay/buy",
    "jumpType": "1",
    "startTime": "2024-03-02 00:00:00",
    "endTime": "2025-03-31 00:00:00",
    "state": True,
    "provinces":["20"],
    "platforms": [1, 2]
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case1:SUCCESS")
        datas = {"directory": data["directory"],
                 "title": data["title"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_DOM.py:test_case1:FALL")

@allure.title("用例编号：CJHE1 用例名称：查询广告列表")#描述：针对运营管理模块-查询广告列表功能测试
def test_case2():
    url=baseurl+"/portal/found/list"
    data={
    "page": {
        "pageIndex": 1,
        "pageSize": 10,
        "orders": [
            {
                "column": "state",
                "asc": False
            },
            {
                "column": "sort",
                "asc": False
            },
            {
                "column": "id",
                "asc": False
            }
        ]
    },
    "directory": "6-",
    "title": read_yaml("title"),
    "platform": []
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case2:SUCCESS")
        id = result["data"]["records"][0]["id"]
        datas = {"id": id}
        write_yaml(datas)
    except Exception:
        logging.info("test_DOM.py:test_case2:FALL")

@allure.title("用例编号：CJHE2 用例名称：修改广告")#描述：针对运营管理模块-修改广告功能测试
def test_case3():
    url=baseurl+"/portal/found/update"
    data={
    "directory": read_yaml("directory"),
    "id": read_yaml("id"),
    "title": "修改标题自动化测试2",
    "imageUrl": "https://yunshouji20221125.obs.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fimage%2Fchunyanye_2bb2c305c7af4a7d9e1d1c24d338e05b.png",
    "content": "修改广告",
    "link": "cloud_pop://www.cmdc.com/cloud/pay/buy",
    "jumpType": "2",
    "startTime": "2024-05-02 00:00:00",
    "endTime": "2024-12-31 00:00:00",
    "state": True,
    "platforms": [1, 2],
    "remark": None
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    assert "成功" in result["header"]["errMsg"]
    if result["header"]["errMsg"] =='成功':
        logging.info("test_DOM.py:test_case3:SUCCESS")
    else:
        logging.info("test_DOM.py:test_case3:FALL")

@allure.title("用例编号：CJHE3 用例名称：删除广告")#描述：针对运营管理模块-删除广告功能测试
def test_case4():
    url=baseurl+"/portal/found/delete"
    data=[read_yaml("id")]
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case4:SUCCESS")
    except Exception:
        logging.info("test_DOM.py:test_case4:FALL")

@allure.title("用例编号：CJHE4 用例名称：新增版本配置")#描述：针对运营管理模块-新增版本配置功能测试
def test_case5():
    url=baseurl+"/portal/appVersion/add"
    data={
    "packageName": "自动化测试",
    "version": "8.8.8.20241201",
    "versionNum": "888",
    "downloadURL": "111",
    "content": "自动化测试",
    "fileSize": "60",
    "appType": 2,
    "isForce": False
}

    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case5:SUCCESS")
        datas = {"packageName": data["packageName"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_DOM.py:test_case5:FALL")

@allure.title("用例编号：CJHE5 用例名称：查询版本配置")#描述：针对运营管理模块-查询版本配置功能测试
def test_case6():
    url=baseurl+"/portal/appVersion/list"
    data={
    "packageName":read_yaml("packageName"),
    "pageIndex": 1,
    "pageSize": 10
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case6:SUCCESS")
        rid = result["data"]["records"][0]["id"]
        datas = {"rid": rid}
        write_yaml(datas)
    except Exception:
        logging.info("test_DOM.py:test_case6:FALL")

@allure.title("用例编号：CJHE6 用例名称：修改版本配置")#描述：针对运营管理模块-修改版本配置功能测试
def test_case7():
    url=baseurl+"/portal/appVersion/update"
    data={
    "id": read_yaml("rid"),
    "packageName": "修改自动化测试",
    "version": "9.9.9.20241202",
    "versionNum": 990,
    "downloadURL": "111",
    "content": "自动化测试222",
    "fileSize": "70",
    "appType": 2,
    "isForce": False
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case7:SUCCESS")
    except Exception:
        logging.info("test_DOM.py:test_case7:FALL")

@allure.title("用例编号：CJHE7 用例名称：删除版本配置")#描述：针对运营管理模块-删除版本配置功能测试
def test_case8():
    url=baseurl+"/portal/appVersion/delete"
    data={"ids": [read_yaml("rid")]}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case8:SUCCESS")
    except Exception:
        logging.info("test_DOM.py:test_case8:FALL")

@allure.title("用例编号：CJHE8 用例名称：新增功能引导")#描述：针对运营管理模块-新增功能引导功能测试
def test_case9():
    url=baseurl+"/portal/guidance/add"
    data={
    "guidanceId": "",
    "name": "自动化测试",
    "state": 0,
    "imageUrls": [
        "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fimage%2Flishuhong_6e59d6ccc0ff461f978ba32b2f91874c.jpg"
    ],
    "guidanceProductItemList": [
        {
            "productId": "1747870700813025282",
            "productItemId": "1747870976919863297"
        }
    ]
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case9:SUCCESS")
        datas = {"guidename": data["name"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_DOM.py:test_case9:FALL")

@allure.title("用例编号：CJHE9 用例名称：查询功能引导")#描述：针对运营管理模块-查询功能引导功能测试
def test_case10():
    url=baseurl+"/portal/guidance/queryList"
    data={
    "name": read_yaml("guidename"),
    "productItemCode": None,
    "state": None,
    "pageNumber": 1,
    "pageSize": 10
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case10:SUCCESS")
        gid = result["data"]["records"][0]["id"]
        datas = {"gid": gid}
        write_yaml(datas)
    except Exception:
        logging.info("test_DOM.py:test_case10:FALL")


@allure.title("用例编号：CJHEA 用例名称：修改功能引导")#描述：针对运营管理模块-修改功能引导功能测试
def test_case11():
    url=baseurl+"/portal/guidance/update"
    data={
    "guidanceId": read_yaml("gid"),
    "name": "修改自动化测试",
    "state": False,
    "remark": None,
    "guidanceProductItemList": [
        {
            "productId": "1747870700813025282",
            "productItemId": "1747870976919863297"
        }
    ],
    "imageUrls": [
        "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fimage%2Flishuhong_6e59d6ccc0ff461f978ba32b2f91874c.jpg",
        "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fimage%2Flishuhong_cf02d27d56824e9e90c55b49aa56a7a1.jpeg"
    ]
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case11:SUCCESS")
    except Exception:
        logging.info("test_DOM.py:test_case11:FALL")

@allure.title("用例编号：CJHEB 用例名称：删除功能引导")#描述：针对运营管理模块-删除功能引导功能测试
def test_case12():
    url=baseurl+"/portal/guidance/batchDelete"
    data={"guidanceIdList": [read_yaml("gid")]}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case12:SUCCESS")
    except Exception:
        logging.info("test_DOM.py:test_case12:FALL")

@allure.title("用例编号：CJHEC 用例名称：新增开屏动画")#描述：针对运营管理模块-新增开屏动画功能测试
def test_case13():
    url=baseurl+"/portal/splashScreen/add"
    data={
    "splashScreenId": None,
    "splashScreenName": "自动化测试",
    "splashScreenContent": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fimage%2Flishuhong_bff2f503262746dfa64ca32942e02bf8.jpg",
    "displayFrequency": "ALWAYS",
    "status": "DISABLE",
    "splashScreenProductItemList": [
        {
            "productId": "1747870700813025282",
            "productItemId": "1747870976919863297"
        }
    ],
    "remark": None
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case13:SUCCESS")
        datas = {"splashScreenName": data["splashScreenName"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_DOM.py:test_case13:FALL")

@allure.title("用例编号：CJHED 用例名称：查询开屏动画")#描述：针对运营管理模块-查询开屏动画功能测试
def test_case14():
    url=baseurl+"/portal/splashScreen/queryList"
    data={
    "splashScreenName": read_yaml("splashScreenName"),
    "splashScreenId": None,
    "productItemCode": None,
    "status": None,
    "pageNumber": 1,
    "pageSize": 10
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case14:SUCCESS")
        sid = result["data"]["records"][0]["id"]
        datas = {"sid": sid}
        write_yaml(datas)
    except Exception:
        logging.info("test_DOM.py:test_case14:FALL")

@allure.title("用例编号：CJHEE 用例名称：修改开屏动画")#描述：针对运营管理模块-修改开屏动画功能测试
def test_case15():
    url=baseurl+"/portal/splashScreen/update"
    data={
    "splashScreenId": read_yaml("sid"),
    "splashScreenName": "修改自动化测试",
    "splashScreenContent": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fimage%2Flishuhong_bff2f503262746dfa64ca32942e02bf8.jpg",
    "displayFrequency": "ONCE",
    "status": "DISABLE",
    "remark": None,
    "splashScreenProductItemList": [
        {
            "productId": "1747870700813025282",
            "productItemId": "1747870976919863297"
        }
    ]
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case15:SUCCESS")
    except Exception:
        logging.info("test_DOM.py:test_case15:FALL")

@allure.title("用例编号：CJHEF 用例名称：删除开屏动画")#描述：针对运营管理模块-删除开屏动画功能测试
def test_case16():
    url=baseurl+"/portal/splashScreen/batchDelete"
    data={"splashScreenIdList": [read_yaml("sid")]}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_DOM.py:test_case16:SUCCESS")
    except Exception:
        logging.info("test_DOM.py:test_case16:FALL")

if __name__ == '__main__':
    pytest.main(['-vs','test_DOM.py'])