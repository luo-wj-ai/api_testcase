from random import randint

import requests
import json
from cloudsystem_test.common.Aheaders import Token
from cloudsystem_test.common.Aurl import baseurl
from cloudsystem_test.config.存储token值 import read_yamlm#clear_yamlm

'''验证token是否失效'''
class test_CP:
    def test_username(self):
        url = baseurl + "/cloudphone/member/getDetail"
        data = {}
        headers = {
            'token': read_yamlm('token1')
        }
        res = requests.post(url=url, json=data, headers=headers)
        result = res.text
        result = json.loads(result)
        if result["header"]["errMsg"] == "成功":
            print(read_yamlm("token1"))
        else:
            clear_yamlm()
            # Token()
#     '''获取OS临时票据'''
#     def tmktoken(self):
#         test_CP().test_username()
#         url = baseurl+"/cloudphone/user/login/sso/getOsTmpToken"
#
#         payload = json.dumps({
#           "instanceId": '4j4i20f7'
#         })
#         headers = {
#           'token': read_yamlm("token"),
#           'Content-Type': 'application/json'
#         }
#
#         response = requests.request("POST", url, headers=headers, data=payload)
#         rs=json.loads(response.text)
#         tmpToken=rs["data"]["tmpToken"]
#
#
#         url = baseurl+"/osbo/openApi/auth/v1/getAccessToken"
#
#         payload = json.dumps({
#           "tmpToken": tmpToken
#         })
#         headers = {
#           'Content-Type': 'application/json'
#         }
#
#         response = requests.request("POST", url, headers=headers, data=payload)
#         # print(response.text)
#         ass=json.loads(response.text)
#         accesstoken=ass["data"]["accessToken"]
#         return accesstoken
#
# '''设备锁RSA加密'''
# def devicersa():
#     url = "http://127.0.0.1:8899/mock/rsa/encrypt"
#
#     payload = json.dumps({
#       "et": "1",
#       "encryptText": randint(1000,9999),
#       "publicKey": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCfgZTjlrVJIsRRc4aBVlfahT3xWh48nnB/vN1XMjGWI8qG51yiFbtknZPUczA37GFvU898Y4ZVsbYNP8hxbSYP64j/uPzonswgJRqb5+0Fo5MLjLqy3VzU6ypsALxhQMngP3LfW77WUlmCUkxCa+4AJrnvapE4ZGYoyJSe2xRPwwIDAQAB"
#     })
#     headers = {
#       'Content-Type': 'application/json'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     # print(response.text)
#     result = response.text
#     result = json.loads(result)
#     password=result["encrypt"]
#     return password
#
# '''登录RSA加密'''
# def loginrsa():
#     url = "http://127.0.0.1:8899/mock/rsa/encrypt"
#
#     payload = json.dumps({
#         "et": "1",
#         "encryptText": randint(100000,999999),
#         "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvtQpvb5Z5qihpeEugZWe8zggWhM4n9w4miKWkYQXN1V69O3OPWo9IegaQf7rtK8PeI9jItQQU/o8Tb7wgPCX0hWHnDIsTr3mndshmgqL907i4LkLiYzB33NWUG46LAFe/yfxexLtDk1r3M+TnuynZmqXfloTovqR1IW5YZghmTjdpAkDp4094U5TRBy+Iuvw3x4la9cLEYc1ysKhzJAjCj7xWHXNS8rngiy727UtopyUXR8PZjBX/hiwgKZWD3hNnAvxMuRpF8LP9dugvSKsFE3vV7mdd6wVcgMgyiOFX3NFXpJRbKCVl6EDfQmT1YbddowV6MzN0bKSASDpnFvZdwIDAQAB"
#     })
#     headers = {
#         'Content-Type': 'application/json'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     # print(response.text)
#     result = response.text
#     result = json.loads(result)
#     code=result["encrypt"]
#     return code

'''验证现网token是否失效'''
# class test_CP2:
#     def test_username2(self):
#         url = baseurl + "/cloudphone/member/getDetail"
#         data = {}
#         headers = {
#             'token': read_yamlm2("token")
#         }
#         res = requests.post(url=url, json=data, headers=headers)
#         result = res.text
#         result = json.loads(result)
#         if result["header"]["errMsg"] == "成功":
#             read_yamlm2("token")
#         else:
#             clear_yamlm2()
#             Token21()
