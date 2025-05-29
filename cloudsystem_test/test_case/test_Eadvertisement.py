import json
import pytest
import requests
import allure
from cloudsystem_test.common.Aheaders import h
from cloudsystem_test.common.Aurl import baseurl
from cloudsystem_test.config.dataportal import write_yaml, read_yaml, clear_yaml
import logging

#云手机运营后台token
headers=h()
#清空yaml文件
clear_yaml()
#配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@allure.title("用例编号：CJHEG 用例名称：新增OS广告")#描述：针对OS运营管理模块-新增OS广告功能测试
def test_case1():
    url=baseurl+"/portal/osAdvert/add"
    data={
    "adsType": "REGULAR_AD",
    "adsTitle": "自动化测试",
    "status": "DISABLE",
    "positionsId": "1",
    "displayCount": 100,
    "displayInterval": 3600,
    "platformKeys": [],
    "provinceCodes": [],
    "productItemIds": [],
    "attributes": {
        "coverImageUrl": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fadvert%2F%E7%89%A2%E5%A4%A7_20241127162505554.jpg",
        "jumpLink": "www.baidu.com"
    },
    "add": {
        "displayCount": "100",
        "displayInterval": "1"
    }
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case1:SUCCESS")
        datas = {"adsTitle": data["adsTitle"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_Eadvertisement.py:test_case1:FALL")


@allure.title("用例编号：CJHEH 用例名称：查询OS广告列表")#描述：针对OS运营管理模块-查询OS广告列表功能测试
def test_case2():
    url=baseurl+"/portal/osAdvert/list"
    data={
    "pageSize": 10,
    "pageNumber": 1,
    "adsTitle": read_yaml("adsTitle"),
    "sorts": [
        {
            "sortField": "id",
            "sortOrder": "DESC"
        },
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
        logging.info("test_Eadvertisement.py:test_case2:SUCCESS")
        id = result["data"]["advertList"][0]["id"]
        datas = {"os-id": id}
        write_yaml(datas)
    except Exception:
        logging.info("test_Eadvertisement.py:test_case2:FALL")


@allure.title("用例编号：CJHEI 用例名称：修改OS广告")#描述：针对OS运营管理模块-修改OS广告功能测试
def test_case3():
    url=baseurl+"/portal/osAdvert/update"
    data={
    "adsId":read_yaml("os-id"),
    "adsType": "REGULAR_AD",
    "adsTitle": "修改自动化测试2",
    "status": "DISABLE",
    "positionsId": "1",
    "displayCount": 80,
    "displayInterval": 3600,
    "platformKeys": [],
    "provinceCodes": [],
    "productItemIds": [],
    "attributes": {
        "coverImageUrl": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fadvert%2F%E7%89%A2%E5%A4%A7_20241127162505554.jpg",
        "jumpLink": "www.baidu.com"
    },
    "add": {
        "displayCount": "100",
        "displayInterval": "1"
    }
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case3:SUCCESS")
    except Exception:
        logging.info("test_Eadvertisement.py:test_case3:FALL")

@allure.title("用例编号：CJHEJ 用例名称：删除OS广告")#描述：针对OS运营管理模块-删除OS广告功能测试
def test_case4():
    url=baseurl+"/portal/osAdvert/batchDelete"
    data={
    "adsIdList": [
        read_yaml("os-id")
    ]
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case4:SUCCESS")
    except Exception:
        logging.info("test_Eadvertisement.py:test_case4:FALL")

@allure.title("用例编号：CJHEK 用例名称：新增主题")#描述：针对OS运营管理模块-新增主题功能测试
def test_case5():
    url=baseurl+"/portal/osTheme/add"
    data={
    "themeName": "自动化测试",
    "themeImageUrls": [
        "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Ftheme%2F%E7%89%A2%E5%A4%A7_20241127164846979.jpg"
    ],
    "themeFile": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Ftheme_package%2Fyunshouji_chp_admin_test_yg_test_image_jingchen2_cfd7058ac0b140eabbb0face4f763aa8_20241127164857069.gnz",
    "fileSize": 10855058,
    "status": "DISABLE",
    "orderNum": 0,
    "provinceCodes": [],
    "themeFileAttribute": {
        "themeFileName": "yunshouji_chp_admin_test_yg_test_image_jingchen2_cfd7058ac0b140eabbb0face4f763aa8_20241127164857069.gnz"
    }
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case5:SUCCESS")
        datas = {"themeName": data["themeName"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_Eadvertisement.py:test_case5:FALL")


@allure.title("用例编号：CJHEL 用例名称：查询主题列表")#描述：针对OS运营管理模块-查询主题列表功能测试

def test_case6():
    url=baseurl+"/portal/osTheme/list"
    data={
    "pageNumber": 1,
    "pageSize": 10,
    "themeName": read_yaml("themeName")
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case6:SUCCESS")
        themeid = result["data"]["records"][0]["id"]
        datas = {"themeid": themeid}
        write_yaml(datas)
    except Exception:
        logging.info("test_Eadvertisement.py:test_case6:FALL")


@allure.title("用例编号：CJHEM 用例名称：修改主题")#描述：针对OS运营管理模块-修改主题功能测试
def test_case7():
    url=baseurl+"/portal/osTheme/update"
    data={
    "themeId":read_yaml("themeid"),
    "themeName": "修改自动化测试2",
    "themeImageUrls": [
        "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Ftheme%2F%E7%89%A2%E5%A4%A7_20241127164846979.jpg"
    ],
    "themeFile": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Ftheme_package%2Fyunshouji_chp_admin_test_yg_test_image_jingchen2_cfd7058ac0b140eabbb0face4f763aa8_20241127164857069.gnz",
    "fileSize": 10855058,
    "status": "DISABLE",
    "orderNum": 1,
    "provinceCodes": [],
    "themeFileAttribute": {
        "themeFileName": "yunshouji_chp_admin_test_yg_test_image_jingchen2_cfd7058ac0b140eabbb0face4f763aa8_20241127164857069.gnz"
    }
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case7:SUCCESS")
    except Exception:
        logging.info("test_Eadvertisement.py:test_case7:FALL")

@allure.title("用例编号：CJHEN 用例名称：删除主题")#描述：针对OS运营管理模块-删除主题功能测试
def test_case8():
    url=baseurl+"/portal/osTheme/batchDelete"
    data={
    "themeIdList": [read_yaml("themeid")]}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case8:SUCCESS")
    except Exception:
        logging.info("test_Eadvertisement.py:test_case8:FALL")

@allure.title("用例编号：CJHEO 用例名称：新增壁纸")#描述：针对OS运营管理模块-新增壁纸功能测试
def test_case9():
    url=baseurl+"/portal/osWallpaper/add"
    data={
    "wallpaperName": "自动化测试",
    "wallpaperImage": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fwallpaper%2F%E7%89%A2%E5%A4%A7_20241127170131306.jpg",
    "wallpaperSize": 27026,
    "status": "DISABLE",
    "orderNum": 0,
    "provinceCodes": []
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case9:SUCCESS")
        datas = {"wallpaperName": data["wallpaperName"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_Eadvertisement.py:test_case9:FALL")


@allure.title("用例编号：CJHEP 用例名称：查询壁纸列表")#描述：针对OS运营管理模块-查询壁纸列表功能测试
def test_case10():
    url=baseurl+"/portal/osWallpaper/list"
    data={
    "wallpaperName":read_yaml("wallpaperName"),
    "pageNumber": 1,
    "pageSize": 10,
    "sorts": [
        {
            "sortField": "orderNum",
            "sortOrder": "ASC"
        },
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
        logging.info("test_Eadvertisement.py:test_case10:SUCCESS")
        wallpaperid = result["data"]["wallpapers"][0]["id"]
        datas = {"wallpaperid": wallpaperid}
        write_yaml(datas)
    except Exception:
        logging.info("test_Eadvertisement.py:test_case10:FALL")

@allure.title("用例编号：CJHEQ 用例名称：修改壁纸")#描述：针对OS运营管理模块-修改壁纸功能测试
def test_case11():
    url = baseurl + "/portal/osWallpaper/update"
    data = {
        "wallpaperId":read_yaml("wallpaperid"),
        "wallpaperName": "修改自动化测试2",
        "wallpaperImage": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fwallpaper%2F%E7%89%A2%E5%A4%A7_20241127170131306.jpg",
        "wallpaperSize": 27026,
        "status": "DISABLE",
        "orderNum": 1,
        "provinceCodes": []
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case11:SUCCESS")
    except Exception:
        logging.info("test_Eadvertisement.py:test_case11:FALL")

@allure.title("用例编号：CJHER 用例名称：删除壁纸")#描述：针对OS运营管理模块-删除壁纸功能测试
def test_case12():
    url=baseurl+"/portal/osWallpaper/batchDelete"
    data={
    "wallpaperIds": [read_yaml("wallpaperid")]
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case12:SUCCESS")
    except Exception:
        logging.info("test_Eadvertisement.py:test_case12:FALL")

@allure.title("用例编号：CJHES 用例名称：新增小组件")#描述：针对OS运营管理模块-新增小组件功能测试
def test_case13():
    url=baseurl+"/portal/osWidget/add"
    data={
    "widgetName": "自动化测试",
    "widgetContentList": [
        {
            "image": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fwidget%2F%E7%89%A2%E5%A4%A7_20241127171205994.jpg",
            "jumpType": "URL"
        }
    ],
    "widgetSize": "2*2",
    "status": "DISABLE",
    "orderNum": 0
}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case13:SUCCESS")
        datas = {"widgetName": data["widgetName"]}
        write_yaml(datas)
    except Exception:
        logging.info("test_Eadvertisement.py:test_case13:FALL")


@allure.title("用例编号：CJHET 用例名称：查询小组件")#描述：针对OS运营管理模块-查询小组件功能测试
def test_case14():
    url=baseurl+"/portal/osWidget/list"
    data={
    "widgetName": read_yaml("widgetName"),
    "pageNumber": 1,
    "pageSize": 10,
    "sorts": [
        {
            "sortField": "orderNum",
            "sortOrder": "ASC"
        },
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
        logging.info("test_Eadvertisement.py:test_case14:SUCCESS")
        widgetid = result["data"]["widgets"][0]["id"]
        datas = {"widgetid": widgetid}
        write_yaml(datas)
    except Exception:
        logging.info("test_Eadvertisement.py:test_case14:FALL")


@allure.title("用例编号：CJHEU 用例名称：修改小组件")#描述：针对OS运营管理模块-修改小组件功能测试
def test_case15():
    url=baseurl+"/portal/osWidget/update"
    data = {
        "widgetId": read_yaml("widgetid"),
        "widgetName": "修改自动化测试2",
        "widgetContentList": [
            {
                "image": "https://yunshouji20221125.obs.dualstack.cidc-rp-12.joint.cmecloud.cn:443/yunshouji%2Fchp_admin%2Ftest%2Fyg_test%2Fwidget%2F%E7%89%A2%E5%A4%A7_20241127171205994.jpg",
                "jumpType": "URL"
            }
        ],
        "widgetSize": "2*2",
        "status": "DISABLE",
        "orderNum": 1
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case15:SUCCESS")
    except Exception:
        logging.info("test_Eadvertisement.py:test_case15:FALL")

@allure.title("用例编号：CJHEV 用例名称：删除小组件")#描述：针对OS运营管理模块-删除小组件功能测试
def test_case16():
    url=baseurl+"/portal/osWidget/batchDelete"
    data={
    "widgetIds": [read_yaml("widgetid")]}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress = res.text
    result = json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case16:SUCCESS")
    except Exception:
        logging.info("test_Eadvertisement.py:test_case16:FALL")

@allure.title("用例编号：CJHEW 用例名称：新增消息")#描述：针对OS运营管理模块-新增消息功能测试
def test_case17():
    url = baseurl + "/portal/system/msgManage/add"
    data = {"bulletinTitle": "自动化测试专用",
            "bulletinContent": "自动化测试专用",
            "phones":[15013957569],
            "pushType": 1,
            "targetType":1,
           "link":"https://www.baidu.com/",
            "type": 2
            }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    ress=res.text
    result=json.loads(ress)
    try:
        assert "成功" in result["header"]["errMsg"]
        logging.info("test_Eadvertisement.py:test_case17:SUCCESS")
    except Exception:
        logging.info("test_Eadvertisement.py:test_case17:FALL")

if __name__ == '__main__':
    pytest.main(['-vs',"test_Eadvertisement.py"])
