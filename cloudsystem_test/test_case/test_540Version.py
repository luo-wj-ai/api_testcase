import json
import logging
from random import randint
import allure
import pytest
import requests
from cloudsystem_test.common.Aurl import baseurl
from cloudsystem_test.common.Bthirdheader import app_id, request_id, signature, timestamp
from cloudsystem_test.config.Ahandle import test_CP

from cloudsystem_test.config.stockdata import write_cyaml, read_cyaml, clear_cyaml
from cloudsystem_test.config.存储token值 import read_yamlm

#清空yaml文件
clear_cyaml()
#配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@allure.title("用例编号：TF654 用例名称：营销计划任务物料信息同步")#描述：针对运营编排模块-营销计划任务物料信息同步接口测试
def test_case1():
    url = "http://cc-hwy.cmtest.xyz/cloudphone/third/iop/plan/syncActivityInfo"

    data ={
        "planInfo": {
            "planId": randint(10000,99999),
            "planName": "免流活动投放",
            "touchPointId": "123456",
            "touchPointName": "移动云盘app首页Banner位",
            "businessTouchPointId": "6-",
            "beginTime": "2024-10-10 12:01:02",
            "endTime": "2025-10-10 12:01:02",
            "status": 0,
            "personaSource": 0,
            "testPhoneList": [
                "13800000000",
                "13800000001"
            ],
            "materialConfig": "{\"title\":\"活动标题\",\"platforms\":[1,2],\"provinces\":\"\",\"imageUrl\":[\"/data/upload/resource/20241225/d72689e26c257701727e0d954758183e135425.png\"],\"adLink\":\"http://www.baidu.com\",\"startTime\":\"2024-10-10 12:01:02\",\"endTime\":\"2024-12-26 00:00:00\",\"jumpType\":1,\"link\":\"http://www.baidu.com\",\"content\":\"解放拉萨的金发路上的风景\"}"
        }
    }
    # #自己手动输入的
    # headers_test = {
    #     "x-app-id": 'Q0NylSZ7hj',
    #     "x-request-id": '7330436453882662912',
    #     "x-timestamp": '1747712243529',
    #     "x-signature": '2ecc47c63eb02d6bf5f501757d34058c',
    #     'Content-Type': 'application/json'
    # }
    headers = {
        "x-app-id": app_id,
        "x-request-id": request_id,
        "x-timestamp":str(timestamp),
        "x-signature": signature,
        'Content-Type': 'application/json'
    }
    res = requests.post(url=url,json=data,headers=headers)
    print(res.text)
    result=res.text
    result=json.loads(result)

    try:
        assert "成功" in result["msg"]
        logging.info("test_540Version.py:test_case1:SUCCESS")
        datas = {"planId": data["planInfo"]["planId"]}
        write_cyaml(datas)
    except Exception:
        logging.info("test_540Version.py:test_case1:FALL")

@allure.title("用例编号：TF655 用例名称：营销计划任务状态变更同步")#描述：针对运营编排模块-营销计划任务状态变更同步接口测试
def test_case2():
    url=baseurl+"/cloudphone/third/iop/plan/statusChange"
    data={
    "planId": read_cyaml("planId"),
    "businessTouchPointId": "6-",
    "status": 0
}
    headers={
        "x-app-id": app_id,
        "x-request-id": request_id,
        "x-timestamp":str(timestamp),
        "x-signature": signature,
        'Content-Type': 'application/json'
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    result=res.text
    result=json.loads(result)
    try:
        assert "成功" in result["msg"]
        logging.info("test_540Version.py:test_case2:SUCCESS")
    except Exception:
        logging.info("test_540Version.py:test_case2:FALL")

@allure.title("用例编号：TF656 用例名称：查询可用的优惠券列表")#描述：针对运营编排模块-查询可用的优惠券列表接口测试
def test_case3():
    test_CP().test_username()
    url=baseurl+"/cloudphone/coupon/queryAvailableList"
    data={
    "memberPackageId":"689",
    "channel":"APP",
    "ifQueryRemark":True
}
    headers={
        "token":read_yamlm("token"),
        'Content-Type': 'application/json'
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    result=res.text
    result=json.loads(result)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_540Version.py:test_case3:SUCCESS")
    except Exception:
        logging.info("test_540Version.py:test_case3:FALL")

@allure.title("用例编号：TF657 用例名称：查询当前用户下的优惠券列表")#描述：针对运营编排模块-查询当前用户下的优惠券列表接口测试
def test_case4():
    test_CP().test_username()
    url=baseurl+"/cloudphone/coupon/queryList"
    data={
    "pageSize":10,
    "pageNumber":1,
    "ifQueryRemark":True,
    "displayStatus":"UNUSED",
    "sorts": [
        {
            "sortField": "createTime",
            "sortOrder": "DESC"
        },
        {
            "sortField": "id",
            "sortOrder": "DESC"
        }
    ]
}
    headers={
        "token":read_yamlm("token"),
        'Content-Type': 'application/json'
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    result=res.text
    result=json.loads(result)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_540Version.py:test_case4:SUCCESS")
    except Exception:
        logging.info("test_540Version.py:test_case4:FALL")
if __name__ == '__main__':
    pytest.main(['-vs','test_540Version.py'])

