import json
import allure
from cloudsystem_test.common.Aheaders import Get_Authorization_new
from cloudsystem_test.common.Aurl import baseurl
from cloudsystem_test.utils.RequestHandler import RequestHandler
from cloudsystem_test.utils.ResponseValidator import ResponseValidator


"""
新增ai助手入口/portal/aiAssistant/create
修改灵ai手入口/portal/aiAssistant/update
上架ai助手入口/portal/aiAssistant/batchUpdateStatus
下架ai助手入口/portal/aiAssistant/batchUpdateStatus
查询ai助手入口详情/portal/aiAssistant/details
获取ai助手入口与产商品关联关系/portal/aiAssistant/queryAiItems
查询ai助手入口列表/portal/aiAssistant/list
"""
@allure.title("用例编号：CJHA1 用例名称：新增AI助手入口")
def test_case01():
    url = baseurl + "/portal/aiAssistant/create"

    payload = {
        "aiAssistantId": None,
        "aiAssistantName": "^测^试^勿^动",
        "productItemList": [
            {
                "productId": "1930063579810500610",
                "productItemId": "1930064456256458754"
            }
        ],
        "remark": None,
        "status": "DISABLE",
        "aiAssistantContentList": [
            {
                "displayLocation": "FLOATING_BALL_POSITION",
                "image": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fapp_library%2F%E5%8A%A8%E6%BC%AB%E5%96%9D%E6%B0%B4%E5%B0%91%E5%A5%B3_20250606173049271.jpg",
                "link": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji2Fchp_admin2Ftest2Fyg_test2Fapp_library2F89d99879ly1hpesm57czuj20j60pkabj_20250422170148459.jpg"
            }
        ]
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'csrfToken': 'null',
        'Cookie': 'sidebarStatus=1',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    response = RequestHandler.send_request(
        method="POST",
        url=url,
        data=json.dumps(payload),
        headers=headers
    )

    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功","存在")


@allure.title("用例编号：CJHA2 用例名称：修改灵犀助手入口")
def test_case02():
    url = baseurl + "/portal/aiAssistant/update"

    payload = {
        "aiAssistantId": "1",
        "aiAssistantName": "灵犀助手",
        "status": "ENABLE",
        "productItemList": [
            {
                "productId": "1906898725532729345",
                "productItemId": "1906898923889754113"
            }
        ],
        "aiAssistantContentList": [
            {
                "image": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fapp_library%2F89d99879ly1hpesm57czuj20j60pkabj_20250422170148459.jpg",
                "displayLocation": "FLOATING_BALL_POSITION",
                "link": "lingxi://app/activity?screenType=0"
            },
            {
                "image": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fapp_library%2F%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20240926112448_20250409194002998.png",
                "displayLocation": "BOTTOM_TOOLBAR",
                "link": "lingxi://app/activity?screenType=0"
            }
        ]
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'Content-Type': 'application/json;charset=UTF-8',
        'csrfToken': 'null'
    }

    response = RequestHandler.send_request(
        method="POST",
        url=url,
        data=json.dumps(payload),
        headers=headers
    )

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")

@allure.title("用例编号：CJHA3 用例名称：上架ai助手入口")
def test_case03():
    url = baseurl + "/portal/aiAssistant/batchUpdateStatus"

    payload = {
        "status": "ENABLE",
        "aiAssistantIdList": ["1"]
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'csrfToken': 'null',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    response = RequestHandler.send_request(
        method="POST",
        url=url,
        data=json.dumps(payload),
        headers=headers
    )

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")

@allure.title("用例编号：CJHA4 用例名称：下架ai助手入口")
def test_case04():
    url = baseurl + "/portal/aiAssistant/batchUpdateStatus"

    payload = {
        "status": "DISABLE",
        "aiAssistantIdList": ["1"]
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'csrfToken': 'null',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    response = RequestHandler.send_request(
        method="POST",
        url=url,
        data=json.dumps(payload),
        headers=headers
    )

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")

@allure.title("用例编号：CJHA5 用例名称：查询ai助手入口详情")
def test_case05():
    url = baseurl + "/portal/aiAssistant/details"

    payload = {
        "aiAssistantId": "1"
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'csrfToken': 'null',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    response = RequestHandler.send_request(
        method="POST",
        url=url,
        data=json.dumps(payload),
        headers=headers
    )

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")

@allure.title("用例编号：CJHA06 用例名称：获取AI助手入口与产商品关联关系")
def test_case06():
    url = baseurl +"/portal/aiAssistant/queryAiItems"

    payload = {
        "pageNumber": 1,
        "pageSize": 10,
        "aiAssistantProductItemIdList": ["9", "10"],
        "aiAssistantIdList": ["1", "4"],
        "productIdList": ["product001", "product002"],
        "productItemIdList": ["item002", "item001"]
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'csrfToken': 'null',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    response = RequestHandler.send_request(method="POST",url=url,data=json.dumps(payload), headers=headers)

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")


@allure.title("用例编号：CJHA7 用例名称：查询ai助手入口列表")
def test_case07():
    url = baseurl + "/portal/aiAssistant/list"

    payload = {
        "aiAssistantName": None,
        "productItemCode": None,
        "status": None,
        "pageNumber": 1,
        "pageSize": 10
    }

    headers = {
        'Authorization': Get_Authorization_new(),
        'csrfToken': 'null',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    response = RequestHandler.send_request(
        method="POST",
        url=url,
        data=json.dumps(payload),
        headers=headers
    )

    ResponseValidator.assert_status_code(response, 200)
    ResponseValidator.assert_field_in_response(response, "header.errMsg", "成功")
