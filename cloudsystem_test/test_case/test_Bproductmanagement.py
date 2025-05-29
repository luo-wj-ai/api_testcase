from random import randint
import allure
import pytest
import requests
from cloudsystem_test.common.Aheaders import h
from cloudsystem_test.common.Aurl import baseurl
import json
from cloudsystem_test.config.dataportal import write_yaml, read_yaml, clear_yaml
import logging

#云手机运营后台token
headers=h()
#清空yaml文件
clear_yaml()
#配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@allure.title("用例编号：CJHDC 用例名称：订单列表查询")#描述：针对订单管理模块-订单列表查询功能测试
def test_case1():
    url=baseurl+"/portal/system/order/list"
    data={
    "pageNumber": 1,
    "pageSize": 10,
    "subsAccount": "15013957569",
    "sorts": [
        {
            "sortField": "createTime",
            "sortOrder": "DESC"
        }
    ]
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case1:SUCCESS")
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case1:FALL")

@allure.title("用例编号：CJHDD 用例名称：创建产品")#描述：针对产品管理模块-创建产品功能测试
def test_case2():
    url=baseurl+"/portal/product/create"

    data={
        "displayName": "自动化测试",
        "name": "自动化测试",
        "code": randint(100000000,999999999),
        "effectMode": "IMMEDIATE",
        "renewMode": "AUTO",
        "cancelMode": "IMMEDIATE",
        "resourcePoolId": "1828313015688351745",
        "purpose": "FORMAL",
        "startTime": "2024-12-20 00:00:00",
        "displayOrder": 50,
        "type": "CPH",
        "description": "1",
        "specificationType": "STANDARD",
        "renewLimit": "ONLY_PRODUCT"
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case2:SUCCESS")
        productId = result["data"]["product"]["id"]
        code = result["data"]["product"]["code"]
        datas = {"productId": productId,
                 "code": code}
        write_yaml(datas)
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case2:FALL")

@allure.title("用例编号：CJHDE 用例名称：修改产品")#描述：针对产品管理模块-修改产品功能测试
def test_case3():
    url = baseurl + "/portal/product/update"
    data = {
        "productId":read_yaml("productId"),
        "displayName": "修改名称自动化测试",
        "name": "修改名称自动化测试",
        "code": read_yaml("code"),
        "effectMode": "IMMEDIATE",
        "renewMode": "AUTO",
        "cancelMode": "IMMEDIATE",
        "resourcePoolId": "1828313015688351745",
        "purpose": "FORMAL",
        "startTime": "2023-11-29 11:27:44",
        "displayOrder": 9999,
        "type": "CPH",
        "description": "自动化测试666",
        "specificationType": "ULTRA",
        "renewLimit": "ONLY_PRODUCT"
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case3:SUCCESS")
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case3:FALL")

@allure.title("用例编号：CJHDF 用例名称：新增单品")#描述：针对产品管理模块-新增单品功能测试
def test_case4():
    url=baseurl+"/portal/productIte/create"
    data={
	"productId": read_yaml("productId"),
	"displayName": "自动化测试",
	"name": "自动化测试",
	"code": randint(100000000,999999999),
	"description": "自动化测试",
	"itemType": "MAIN_SERVICE",
	"setMealType": "UN_LIMIT_TIME",
	"limitTime": None,
	"durationType": "DAY",
	"duration": "1",
	"retailPrice": 0.01,
	"currency": "CNY",
	"orderType": None,
	"subsLevel": None,
	"payType": None,
	"billChargeItem": None,
	"orderChannel": None,
	"startTime": "2023-11-29 11:35:05",
	"displayOrder": 0,
	"priceDescription": "自动化测试",
	"benefitIds": [],
	"paymentMode": "VOD",
	"wxPayId": "",
	"aliPayId": "",
	"resourcePoolGroupId": "",
	"payTemplateId": "{\"wxPlanId\":\"\",\"aliPlanId\":\"\"}"
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case4:SUCCESS")
        productItemId = result["data"]["productItem"]["id"]
        codeitem = result["data"]["productItem"]["code"]
        datas = {"productItemId": productItemId,
                 "codeitem": codeitem}
        write_yaml(datas)
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case4:FALL")

@allure.title("用例编号：CJHDG 用例名称：修改单品")#描述：针对产品管理模块-修改单品功能测试
def test_case5():
    url = baseurl + "/portal/productIte/update"
    data = {
        "productItemId": read_yaml("productItemId"),
        "productId": read_yaml("productId"),
        "displayName": "修改名称自动化测试",
        "name": "修改名称自动化测试",
        "code": read_yaml("codeitem"),
        "description": "自动化测试888",
        "itemType": "MAIN_SERVICE",
        "setMealType": "UN_LIMIT_TIME",
        "limitTime": None,
        "durationType": "DAY",
        "duration": "1",
        "retailPrice": 0.01,
        "currency": "CNY",
        "orderType": None,
        "subsLevel": None,
        "payType": None,
        "billChargeItem": None,
        "orderChannel": None,
        "startTime": "2023-11-29 11:35:05",
        "displayOrder": 0,
        "priceDescription": "自动化测试",
        "benefitIds": [],
        "paymentMode": "VOD",
        "wxPayId": "",
        "aliPayId": "",
        "resourcePoolGroupId": "",
        "payTemplateId": "{\"wxPlanId\":\"\",\"aliPlanId\":\"\"}"
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case5:SUCCESS")
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case5:FALL")

@allure.title("用例编号：CJHDJ 用例名称：产品下架")#描述：针对产品管理模块-产品下架功能测试
def test_case6():
    url = baseurl + "/portal/product/taskDown"  # 产品下架接口
    data={
        "productId":1747875589274337282
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case6:SUCCESS")
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case6:FALL")


@allure.title("用例编号：CJHDK 用例名称：产品上架")#描述：针对产品管理模块-产品上架功能测试
def test_case7():

    url = baseurl + "/portal/product/shelveProduct"  # 产品上架产品
    data = {
        "productId": 1747875589274337282
    }

    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case7:SUCCESS")
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case7:FALL")


@allure.title("用例编号：CJHDM 用例名称：单品上架")#描述：针对产品管理模块-单品上架功能测试
def test_case8():
    url = baseurl + "/portal/productIte/batchShelve"  # 单品上架接口

    data = {
        "productId":1747875589274337282,
        "productItemIds":[1747876163394863105]
    }

    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case8:SUCCESS")
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case8:FALL")

'''单品下架'''
@allure.title("用例编号：CJHDL 用例名称：单品下架")#描述：针对产品管理模块-单品下架功能测试
def test_case9():
    url = baseurl + "/portal/productIte/batchTakeDown"  # 单品下架接口

    data = {
        "productId": 1747875589274337282,
        "productItemIds":[1747876163394863105]
    }

    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case9:SUCCESS")
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case9:FALL")

@allure.title("用例编号：CJHDH 用例名称：删除单品")#描述：针对产品管理模块-删除单品功能测试
def test_case10():
    url=baseurl+"/portal/productIte/batchDelete"
    data={"productId":read_yaml("productId"),
          "productItemIds":[read_yaml("productItemId")]}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case10:SUCCESS")
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case10:FALL")

@allure.title("用例编号：CJHDI 用例名称：删除产品")#描述：针对产品管理模块-删除产品功能测试
def test_case11():
    url=baseurl+"/portal/product/delete"
    data={"productId":read_yaml("productId")}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case11:SUCCESS")
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case11:FALL")



@allure.title("用例编号：CJHDN 用例名称：新增兑换码")#描述：针对产品管理模块-新增兑换码功能测试
def test_case12():
    url=baseurl+"/portal/voucher/create"
    data={
    "name": "luo",
    "startTime": "2025-05-27 11:45:51",
    "endTime": "2025-05-30 00:00:00",
    "productId": "1925012194404470786",
    "productItemId": "1925012764209057793",
    "durationType": "WEEK",
    "duration": 1,
    "count": 1,
    "maxUseCount": 1,
    "generateType": "PRE_GENERATED",
    "isLimitUser": "false"
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case12:SUCCESS")
        batchid = result["data"]["voucherBatch"]["id"]
        datas = {"batchId": batchid}
        write_yaml(datas)
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case12:FALL")


@allure.title("用例编号：CJHDO 用例名称：生成兑换码")#描述：针对产品管理模块-生成兑换码功能测试
def test_case13():
    url=baseurl+"/portal/voucher/createVouchers"
    data={
    "batchId":read_yaml("batchId")
        }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Bproductmanagement.py:test_case13:SUCCESS")
    except Exception:
        logging.info("test_Bproductmanagement.py:test_case13:FALL")

if __name__ == '__main__':
    pytest.main(['-vs',"test_Bproductmanagement.py"])




