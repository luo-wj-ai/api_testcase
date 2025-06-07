import json
import allure
import requests

from cloudsystem_test.common.Aheaders import geting_token
from cloudsystem_test.common.Aurl import baseurl02
from cloudsystem_test.common.Bthirdheader02 import generate_api_auth_data
from cloudsystem_test.config.Ahandle import Device_Rsa
from cloudsystem_test.utils.RequestHandler import RequestHandler
from cloudsystem_test.utils.ResponseValidator import ResponseValidator
from cloudsystem_test.config.请求头签名 import app_id, timestamp, signature

phone_number=15107612187

"""用户云机"""
@allure.title("用例编号：CJHA1 用例名称：查询用户云机使用详情")
def test_case01():
    url = baseurl02 + "/cloudphone/device/third/queryUsageDetail"
    payload = json.dumps({
        "account": "Kjz/1tf64DbNYHOXOqYCHWHEG7jr70NAzoH7q4VprPZfeuQQZNfUOyLvjIkF1dj2DRBbpYp/R7iuUPDvH+9TnB2tn3cylOBySvs4JWVgaUx2I6dRGRHjSnvCNaNVA5QbeLUPpG2m23t0BsVD1cl7z0fELh1WZ94zRbRsVq0SNG6GwF0obad3bWg+jMBdvh7oESaFJPQ794/mi73cohkkK3JAKk1sV234LiqyeMBffE4nSzJn/VYn4g++nyma9igll3C+5G8SSh7TPWeFJwIlZFkDXqtAKTdkoqYUJhMK2lRKID4hKr8xaY97RpElkpase1hxodt+1FElJ6ir5CqzJA=="
    })
    headers = {
        'appId': app_id,
        'timestamp': timestamp,
        'signature': "third_sys " + signature,
        'Content-Type': 'application/json'
    }
    response = RequestHandler.send_request(method="POST", url=url, data=payload, headers=headers)
    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, 'header.errMsg', "成功")
    return None

@allure.title("用例编号：CJHA2 用例名称：批量查询用户云机实例列表")
def test_case02():
    url = baseurl02 + "/cloudphone/subscribe/third/queryUserInstanceList"
    payload = json.dumps({
        "userAccountList": [
            "18475952281",
            "15013242712",
            "13726265991"
        ]
    })
    headers = {
        'appId': app_id,
        'timestamp': timestamp,
        'signature': "third_sys " + signature,
        'Content-Type': 'application/json'
    }
    response = RequestHandler.send_request(method="POST", url=url, data=payload, headers=headers)
    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, 'header.errMsg', "成功")
    return None

@allure.title("用例编号：CJHA3 用例名称：查询默认云机设置")
def test_case03():
    url = baseurl02 + "/cloudphone/defaultDevice/queryDetail"
    client_id02, request_id02, timestamp02, signature02 = generate_api_auth_data()
    payload = {}
    headers = {
        'x-kpcc-clientId': client_id02,
        'x-kpcc-requestId': request_id02,
        'x-kpcc-timestamp': timestamp02,
        'x-kpcc-signature': signature02,
        'token': geting_token()
    }
    response = RequestHandler.send_request(method="POST", url=url, data=payload, headers=headers)
    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, 'header.errMsg', "成功")
    return None


@allure.title("用例编号：CJHA4 用例名称：查询订购关系")
def test_case04():
    url = baseurl02 + "/cloudphone/subscribe/third/queryUserRelationshipV2"

    payload = {
        "pageSize": 10,
        "pageNumber": 1,
        "phone": phone_number,
        "statusList": ["ACTIVE", "PENDING"]
    }

    headers = {
        'appId': app_id,
        'timestamp': timestamp,
        'signature': "third_sys " + signature,
        'Content-Type': 'application/json'
    }

    response = RequestHandler.send_request(
        method="POST",
        url=url,
        data=json.dumps(payload),
        headers=headers
    )

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")
