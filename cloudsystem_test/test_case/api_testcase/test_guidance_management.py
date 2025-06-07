import json
import allure
import requests

from cloudsystem_test.common.Aheaders import Get_Authorization_new
from cloudsystem_test.common.Aurl import baseurl02,baseurl
from cloudsystem_test.config.Ahandle import Device_Rsa
from cloudsystem_test.utils.RequestHandler import RequestHandler
from cloudsystem_test.utils.ResponseValidator import ResponseValidator

"""
上架引导/portal/guidance/batchUpdateStatus
下架引导/portal/guidance/batchUpdateStatus
获取引导能力产商品关联关系/portal/guidance/queryGuidanceProductItem
上架开屏动画/portal/splashScreen/batchUpdateStatus
下架开屏动画/portal/splashScreen/batchUpdateStatus
获取开屏动画与产商品关联关系/portal/splashScreen/querySplashScreenProductItem
"""

@allure.title("用例编号：CJHA1 用例名称：上架引导")
def test_case01():
    url = baseurl+"/portal/guidance/batchUpdateStatus"

    payload = {
        "guidanceIdList": ["16"],
        "state": 1
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'Content-Type': 'application/json'
    }

    response = RequestHandler.send_request(method="POST",url=url,data=json.dumps(payload),headers=headers)

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")

@allure.title("用例编号：CJHA2 用例名称：下架引导")
def test_case02():
    url = baseurl+"/portal/guidance/batchUpdateStatus"

    payload = {
        "guidanceIdList": ["16"],
        "state": 0
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'Content-Type': 'application/json'
    }

    response = RequestHandler.send_request(method="POST",url=url,data=json.dumps(payload),headers=headers)

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")

@allure.title("用例编号：CJHA3 用例名称：获取引导能力产商品关联关系")
def test_case03():
    url = baseurl + "/portal/guidance/queryGuidanceProductItem"

    payload = {
        "pageNumber": 1,
        "pageSize": 1,
        "guidanceProductItemId": "1770989691685064706",
        "guidanceId": "1770989691576012802",
        "productId": "1",
        "productItemId": "3"
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'Content-Type': 'application/json'
    }

    response = RequestHandler.send_request(method="POST", url=url, data=json.dumps(payload), headers=headers)

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")

@allure.title("用例编号：CJHA4 用例名称：上架开屏动画")
def test_case04():
    url = baseurl + "/portal/splashScreen/batchUpdateStatus"

    payload = {
        "status": "ENABLE",
        "splashScreenIdList": ["7"]
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'Content-Type': 'application/json'
    }

    response = RequestHandler.send_request(method="POST", url=url, data=json.dumps(payload), headers=headers)

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")

@allure.title("用例编号：CJHA5 用例名称：下架开屏动画")
def test_case05():
    url = baseurl + "/portal/splashScreen/batchUpdateStatus"

    payload = {
        "status": "DISABLE",
        "splashScreenIdList": ["7"]
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'Content-Type': 'application/json'
    }

    response = RequestHandler.send_request(method="POST", url=url, data=json.dumps(payload), headers=headers)

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")

@allure.title("用例编号：CJHA6 用例名称：获取开屏动画与产商品关联关系")
def test_case06():
    url = baseurl + "/portal/splashScreen/querySplashScreenProductItem"

    payload = {
        "splashScreenIdList": None,
        "productItemIdList": [
            "1911687667155079170",
            "1912041889402851329",
            "1909781829385588737",
            "1913056618460090370",
            "1912775029104709633"
        ],
        "pageNumber": 1,
        "pageSize": 100
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'Content-Type': 'application/json'
    }

    response = RequestHandler.send_request(method="POST", url=url, data=json.dumps(payload), headers=headers)

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")

