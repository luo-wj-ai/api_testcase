import json
import allure
import requests

from cloudsystem_test.common.Aheaders import Get_Authorization_new
from cloudsystem_test.common.Aurl import baseurl02
from cloudsystem_test.config.Ahandle import Device_Rsa
from cloudsystem_test.utils.RequestHandler import RequestHandler
from cloudsystem_test.utils.ResponseValidator import ResponseValidator

phone_number=18124457029
"""用户注销"""

@allure.title("用例编号：CJHA1 用例名称：发起注销")
def test_case01():
    url = "https://koophone-cc.cmtest.xyz:8080/portal/user/sms/deactivate"
    payload = {
        "workId": "123456789551234567895522",
        "userId": "1927173769754050562",
        "subsAccount": phone_number
    }
    headers = {
        "Authorization": Get_Authorization_new(),
        "csrfToken": "null",
        "Content-Type": "application/json;charset=UTF-8"
    }
    response = RequestHandler.send_request("POST", url, data=json.dumps(payload), headers=headers)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")
    return None


@allure.title("用例编号：CJHA2 用例名称：用户注销记录")
def test_case02():
    url = baseurl02 + "/cloudphone/user/third/cancellation/record"
    payload = json.dumps({
        "phone": Device_Rsa(phone_number)
        # "phone": "AadLpcdgXuXRHfBh/ihYlNcR9r8R5E2NvOOGp7THLUdKV4lYWAQavDgVVbv2MvLuydhtLAsEVbnTLcKqe4TcX3e3Mv/0ZcSf/UHSJSqyqrIOb9unJeOFQQQIO3ZIIHvSdk82x6QMbYOe67hFpHcABuNtiE96r80szg4iDfyjvsc+rJd4Gdd083UnU0iVpSxpeYoWJXTakw9HpmRZX4HejxU+uwdZChaFJ+3fR+DWQH9FD3ZUpnP4KRtTW20J1dErRYBD5+5qydMNznPIlpMmAR3Mk28BKoWQMoBqstOC8sFaalUgVjL5BwXGE1QDrMXGq3KkqZx1dajzcavpJXrTKw=="
    })
    headers = {
        'appid': 'fF3iE0cA2cA5kC1cB3pB2bE2gL1cA1sd',
        'signature': 'third_sys ePVZsOrMgrKHlY9P2w6eq4uhMvTT3yw47KG6Hb7w3eY=',
        'timestamp': '1702607733',
        'Content-Type': 'application/json'
    }
    response = RequestHandler.send_request(method="POST", url=url, data=payload, headers=headers)
    ResponseValidator.assert_status_code(response, 200)  # 断言状态码为200
    ResponseValidator.assert_field_in_response(response, 'header.errMsg', "成功")
    return None

@allure.title("用例编号：CJHA3 用例名称：上行短信通知接口")
def test_case03():
    url = baseurl02 + "/cloudphone/callback/smsResponse"
    payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<root>\r\n    <BaseNumber>30</BaseNumber>\r\n    <responseDataList>\r\n        <responseData>\r\n            <SpNumber>20</SpNumber>\r\n            <UserNumber>13726265992</UserNumber>\r\n            <MoMsg>ZX</MoMsg>\r\n            <MoTime>2025-04-24 14:25:00</MoTime>\r\n            <timestamp>1744957500000</timestamp>\r\n        </responseData>\r\n    </responseDataList>\r\n</root>"
    headers = {
        'Content-Type': 'application/xml'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200, f"状态码异常，实际为 {response.status_code}"
    return None
