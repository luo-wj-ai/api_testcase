import requests
import json
from cloudsystem_test.config.存储现网token值 import clear_Vyaml
from cloudsystem_test.common.Adata import  P
from cloudsystem_test.common.Aheaders import Token, Token2
from cloudsystem_test.common.Aurl import baseurl, encodeurl
from cloudsystem_test.config.存储token值 import read_yamlm, clear_yamlm
from cloudsystem_test.config.存储现网token值 import read_Vyaml
from cloudsystem_test.config.请求头签名 import app_id, timestamp, signature
from cloudsystem_test.config.deskfile import write_yaml, read_yaml
import logging

#配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

'''订购脚本'''
class test_CP:
    '''权益开通订购'''
    def test_ComputingPowerPackage(self, phone, channel, privateKey, skuCode, skuId, price):
        url = "http://cmtest.xyz/procurement/benefit/get?" \
              f"phone={phone}&" \
              f"channel={channel}&" \
              f"privateKey={privateKey}&" \
              f"skuCode={skuCode}&" \
              f"skuId={skuId}&" \
              f"price={price}"

        res = requests.get(url=url)
        # print(res.text)
        output = res.text
        outputs = output
        try:
            outputs = json.loads(outputs)
            logging.info("test_ComputingPowerPackage:SUCCESS")
            quantity = outputs["contractRoot"]["body"]["quantity"]
            orderItemId = outputs["contractRoot"]["body"]["orderItemId"]
            skuName = outputs["contractRoot"]["body"]["skuName"]
            createTime = outputs["contractRoot"]["body"]["createTime"]
            price2 = outputs["contractRoot"]["body"]["price"]
            serverNum = outputs["contractRoot"]["body"]["serverNum"]
            skuCode2 = outputs["contractRoot"]["body"]["skuCode"]
            skuId2 = outputs["contractRoot"]["body"]["skuId"]
            sign = outputs["contractRoot"]["head"]["sign"]
            reqTime = outputs["contractRoot"]["head"]["reqTime"]
            version = outputs["contractRoot"]["head"]["version"]
            transactionId = outputs["contractRoot"]["head"]["transactionId"]
            apiId = outputs["contractRoot"]["head"]["apiId"]
            channelCode = outputs["contractRoot"]["head"]["channelCode"]
            print(orderItemId)
            datas = {
                "quantity": quantity,
                "orderItemId": orderItemId,
                "skuName": skuName,
                "createTime": createTime,
                "price": price2,
                "serverNum": serverNum,
                "skuCode": skuCode2,
                "skuId": skuId2,
                "sign": sign,
                "reqTime": reqTime,
                "version": version,
                "transactionId": transactionId,
                "apiId": apiId,
                "channelCode": channelCode
            }
            write_yaml(datas)
        except Exception:
            logging.info("test_ComputingPowerPackage:FALL")


    def test_ComputingPowerPackage2(self):
        url2 = baseurl + '/cloudphone/procurement/commonBusinessOpen'
        payloadr = {"contractRoot":
            {"body": {
                "quantity": read_yaml("quantity"),
                "orderItemId": read_yaml("orderItemId"),
                "skuName": read_yaml("skuName"),
                "createTime": read_yaml("createTime"),
                "price": read_yaml("price"),
                "serverNum": read_yaml("serverNum"),
                "skuCode": read_yaml("skuCode"),
                "skuId": read_yaml("skuId")
            },
                "head": {
                    "sign": read_yaml("sign"),
                    "reqTime": read_yaml("reqTime"),
                    "version": read_yaml("version"),
                    "transactionId": read_yaml("transactionId"),
                    "apiId": read_yaml("apiId"),
                    "channelCode": read_yaml("channelCode")
                }}}

        headers = {'Content-Type': 'application/json'}
        res = requests.post(url=url2, json=payloadr, headers=headers)
        print(res.text)
        print(res.headers)
        result = res.text
        result = json.loads(result)
        try:
            if result["contractRoot"]["body"]["resultMsg"] == "开通成功":
                assert "开通成功" in result["contractRoot"]["body"]["resultMsg"]
            elif result["contractRoot"]["body"]["resultMsg"] == "开通中，待回调":
                assert "开通中，待回调" in result["contractRoot"]["body"]["resultMsg"]
            logging.info("test_ComputingPowerPackage2:SUCCESS")
        except Exception:
            logging.info("test_ComputingPowerPackage2:FALL")
    '''权益开通订购退订云机'''
    def test_ComputingPowerPackage3(self, phone, channelCode, privateKey):
        url = "http://cmtest.xyz/procurement/benefit/cancel?" \
              f"phone={phone}&" \
              f"channelCode={channelCode}&" \
              f"privateKey={privateKey}&" \
              f"orderItemId={read_yaml('orderItemId')}"

        res = requests.get(url=url)
        # print(res.text)
        output = res.text
        outputs = output
        try:
            outputs = json.loads(outputs)
            logging.info("test_ComputingPowerPackage3:SUCCESS")
            orderItemIdd = outputs["contractRoot"]["body"]["orderItemId"]
            skuName = outputs["contractRoot"]["body"]["skuName"]
            extCode = outputs["contractRoot"]["body"]["extCode"]
            createTime = outputs["contractRoot"]["body"]["createTime"]
            serverNum = outputs["contractRoot"]["body"]["serverNum"]
            skuCode = outputs["contractRoot"]["body"]["skuCode"]
            sign = outputs["contractRoot"]["head"]["sign"]
            reqTime = outputs["contractRoot"]["head"]["reqTime"]
            transactionId = outputs["contractRoot"]["head"]["transactionId"]
            apiId = outputs["contractRoot"]["head"]["apiId"]
            channelCode = outputs["contractRoot"]["head"]["channelCode"]
            datas = {
                "orderItemId": orderItemIdd,
                "skuName": skuName,
                "extCode": extCode,
                "createTime": createTime,
                "serverNum": serverNum,
                "skuCode": skuCode,
                "sign": sign,
                "reqTime": reqTime,
                "transactionId": transactionId,
                "apiId": apiId,
                "channelCode": channelCode
            }
            write_yaml(datas)
        except Exception:
            logging.info("test_ComputingPowerPackage3:FALL")

    def test_ComputingPowerPackage4(self):
        url2 = baseurl + '/cloudphone/procurement/commonOrderCancel'
        payloadr = {"contractRoot":
            {"body": {
                "orderItemId": read_yaml("orderItemId"),
                "skuName": read_yaml("skuName"),
                "extCode": read_yaml("extCode"),
                "createTime": read_yaml("createTime"),
                "serverNum": read_yaml("serverNum"),
                "skuCode": read_yaml("skuCode")
            },
                "head": {
                    "sign": read_yaml("sign"),
                    "reqTime": read_yaml("reqTime"),
                    "transactionId": read_yaml("transactionId"),
                    "apiId": read_yaml("apiId"),
                    "channelCode": read_yaml("channelCode")
                }}}

        headers = {'Content-Type': 'application/json'}
        res = requests.post(url=url2, json=payloadr, headers=headers)
        print(res.text)
        print(res.headers)
        result = res.text
        result = json.loads(result)
        try:
            assert "退货成功" in result["contractRoot"]["body"]["resultMsg"]
            logging.info("test_ComputingPowerPackage4:SUCCESS")
        except Exception:
            logging.info("test_ComputingPowerPackage4:FALL")

    '''政企权益'''
    def test_governmententerprises(self, phone, channel, privateKey, skuCode, skuId, price):
        url = "http://cmtest.xyz/procurement/benefit/get?" \
              f"phone={phone}&" \
              f"channel={channel}&" \
              f"privateKey={privateKey}&" \
              f"skuCode={skuCode}&" \
              f"skuId={skuId}&" \
              f"price={price}"

        res = requests.get(url=url)
        # print(res.text)
        output = res.text
        outputs = output
        try:
            outputs = json.loads(outputs)
            logging.info("test_governmententerprises:SUCCESS")
            quantity = outputs["contractRoot"]["body"]["quantity"]
            orderItemId = outputs["contractRoot"]["body"]["orderItemId"]
            skuName = outputs["contractRoot"]["body"]["skuName"]
            createTime = outputs["contractRoot"]["body"]["createTime"]
            price2 = outputs["contractRoot"]["body"]["price"]
            serverNum = outputs["contractRoot"]["body"]["serverNum"]
            skuCode2 = outputs["contractRoot"]["body"]["skuCode"]
            skuId2 = outputs["contractRoot"]["body"]["skuId"]
            sign = outputs["contractRoot"]["head"]["sign"]
            reqTime = outputs["contractRoot"]["head"]["reqTime"]
            version = outputs["contractRoot"]["head"]["version"]
            transactionId = outputs["contractRoot"]["head"]["transactionId"]
            apiId = outputs["contractRoot"]["head"]["apiId"]
            channelCode = outputs["contractRoot"]["head"]["channelCode"]
            datas = {
                "quantity": quantity,
                "orderItemId": orderItemId,
                "skuName": skuName,
                "createTime": createTime,
                "price": price2,
                "serverNum": serverNum,
                "skuCode": skuCode2,
                "skuId": skuId2,
                "sign": sign,
                "reqTime": reqTime,
                "version": version,
                "transactionId": transactionId,
                "apiId": apiId,
                "channelCode": channelCode
            }
            write_yaml(datas)
        except Exception:
            logging.info("test_governmententerprises:FALL")

    def test_governmententerprises2(self):
        url2 = baseurl + '/cloudphone/cmpp/rightOpen'
        payloadr = {"contractRoot":
            {"body": {
                "quantity": read_yaml("quantity"),
                "orderItemId": read_yaml("orderItemId"),
                "skuName": read_yaml("skuName"),
                "createTime": read_yaml("createTime"),
                "price": read_yaml("price"),
                "serverNum": read_yaml("serverNum"),
                "skuCode": read_yaml("skuCode"),
                "skuId": read_yaml("skuId")
            },
                "head": {
                    "sign": read_yaml("sign"),
                    "reqTime": read_yaml("reqTime"),
                    "version": read_yaml("version"),
                    "transactionId": read_yaml("transactionId"),
                    "apiId": read_yaml("apiId"),
                    "channelCode": read_yaml("channelCode")
                }}}
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url=url2, json=payloadr, headers=headers)
        print(res.text)
        print(res.headers)
        result = res.text
        result = json.loads(result)
        try:
            assert "开通成功" in result["contractRoot"]["body"]["resultMsg"]
            logging.info("test_governmententerprises2:SUCCESS")
        except Exception:
            logging.info("test_governmententerprises2:FALL")

        '''验证token是否失效'''
    def test_username(self):
        url=baseurl+"/cloudphone/member/getDetail"
        data={}
        headers = {
            'token': read_yamlm("token")
        }
        res=requests.post(url=url,json=data,headers=headers)
        result=res.text
        result=json.loads(result)

        if result["header"]["errMsg"] =="成功":
            pass
        else:
            clear_yamlm()
            Token()

        '''正向订购APP'''
    def test_AForwardordering(self, memberPackageId):
        test_CP().test_username()
        urlcode = baseurl + '/cloudphone/order/sendOrderConfirmationCode'
        payloadcode = {
            "memberPackageId": memberPackageId
        }

        headers = {
            'token': read_yamlm("token"),
            'Content-Type': 'application/json'
        }
        rescode = requests.post(url=urlcode, json=payloadcode, headers=headers)
        print(rescode.text)
        print(rescode.headers)
        write_yaml(payloadcode)
        result=rescode.text
        result=json.loads(result)
        try:
            assert "成功" in result["header"]["errMsg"]
            logging.info("test_AForwardordering:SUCCESS")
        except Exception:
            logging.info("test_AForwardordering:FALL")

    def test_AForwardordering2(self, phone):
        url = f'http://cc-hwy.cmtest.xyz/SendMailModule/smsList?mobile={phone}'
        res = requests.get(url=url)
        # print(res.content.decode('unicode-escape'))
        result = res.content.decode('unicode-escape')
        result = json.loads(result)
        smscode = result[-1]["template_var"][0:6]

        url = f"http://sbo.cmtest.xyz/cloudphone-sign/encry/smsCode?code={smscode}"
        res = requests.get(url=url)
        # print(res.content.decode('unicode-escape'))
        result2 = res.content.decode('unicode-escape')
        result2 = json.loads(result2)
        smscode2 = result2["encryptSmsCode"]
        datas = {"smscode2": smscode2}
        write_yaml(datas)

    def test_AForwardordering3(self, renewOrderNo, channel):
        url = baseurl + '/cloudphone/order/createOrder'
        payloadrr = {
            "memberPackageId": read_yaml("memberPackageId"),
            "smsCode": read_yaml("smscode2"),
            "renewOrderNo": renewOrderNo,
            "channel": channel
        }
        headers = {
            'token': read_yamlm("token"),
            'Content-Type': 'application/json'
        }

        res = requests.post(url=url, json=payloadrr, headers=headers)
        print(res.text)
        print(res.headers)
        result = res.text
        result = json.loads(result)
        try:
            assert "成功" in result["header"]["errMsg"]
            logging.info("test_AForwardordering3:SUCCESS")
            order = result["data"]["orderId"]
            ordervalue = {"order": order}
            write_yaml(ordervalue)
            errmsg = {"errmsg": result["header"]["errMsg"]}
            write_yaml(errmsg)
        except Exception:
            logging.info("test_AForwardordering3:FALL")


    def test_AForwardordering4(self):
                url3 = baseurl + '/cloudphone/order/cancelOrder'
                payloadrr3 = {
                    "orderId": read_yaml("order")
                }
                headers = {
                    'token': read_yamlm("token"),
                    'Content-Type': 'application/json'
                }
                res3 = requests.post(url=url3, json=payloadrr3, headers=headers)
                print(res3.text)
                print(res3.headers)
                result3 = res3.text
                result3 = json.loads(result3)
                try:
                    assert "成功" in result3["header"]["errMsg"]
                    logging.info("test_AForwardordering4:SUCCESS")
                except Exception:
                    logging.info("test_AForwardordering4:FALL")

    '''第三方正向订购'''
    def test_Thirddirectordering(self, account, productItemCode, thirdOrderNo, renewOrderNo, orderType, channelCode):
        url = encodeurl + '/rai/sign/thirdOrder'
        MP = {
            "account": account,
            "productItemCode": productItemCode,
            "thirdOrderNo": thirdOrderNo,
            "renewOrderNo": renewOrderNo,
            "orderType": orderType,
            "channelCode": channelCode,
        }

        headers2 = {'Content-Type': 'application/json'
                    }
        try:
            res = requests.post(url=url, json=MP, headers=headers2)
            logging.info("test_Thirddirectordering:SUCCESS")
            # print(res.text)
            output = res.text
            outputs = output
            outputs = json.loads(outputs)
            sign = outputs['sign']
            datas = {"sign": sign}
            write_yaml(datas)
            payload = {"MP": MP}
            write_yaml(payload)
        except Exception:
            logging.info("test_Thirddirectordering:FALL")


    def test_Thirddirectordering2(self):
        url2 = baseurl + '/cloudphone/order/third/submitOrder'
        MP2 = read_yaml("MP")
        MP2['account'] = read_yaml("MP")["account"]
        MP2['productItemCode'] = read_yaml("MP")['productItemCode']
        MP2['thirdOrderNo'] = read_yaml("MP")['thirdOrderNo']
        if read_yaml("MP")["renewOrderNo"] == '' or read_yaml("MP")["renewOrderNo"] == None:
            MP2['renewOrderNo'] = read_yaml("MP")['renewOrderNo']
            if read_yaml("MP")["orderType"] == "ORDER_BUY":
                pass
            elif read_yaml("MP")["orderType"] != "ORDER_BUY":
                read_yaml("MP")["orderType"] = ''
                print("购买类型有误！")
            else:
                print("输入有误！")
        elif read_yaml("MP")["renewOrderNo"] != '' or read_yaml("MP")["renewOrderNo"] != None:
            MP2['renewOrderNo'] = read_yaml("MP")['renewOrderNo']
            # print(MP2['renewOrderNo'])
            if read_yaml("MP")["orderType"] == "ORDER_RENEW":
                pass
            elif read_yaml("MP")["orderType"] != "ORDER_RENEW":
                read_yaml("MP")["orderType"] = ''
                print("购买类型有误！")
            else:
                print("输入有误！")
        else:
            print('输入有误!')
        MP2['orderType'] = read_yaml("MP")['orderType']
        MP2['channelCode'] = read_yaml("MP")['channelCode']
        MP2['sign'] = read_yaml("sign")

        headers = {'appId': app_id,
                   'timestamp': timestamp,
                   'signature': "third_sys " + signature}

        res2 = requests.post(url=url2, json=MP2, headers=headers)
        print(res2.text)
        print(res2.headers)
        result = res2.text
        result = json.loads(result)
        try:
            assert "成功" in result["header"]["errMsg"]
            logging.info("test_Thirddirectordering2:SUCCESS")
            order = result["data"]["orderId"]
            ordervalue = {"order": order}
            write_yaml(ordervalue)
            errmsg = {"errmsg": result["header"]["errMsg"]}
            write_yaml(errmsg)
        except Exception:
            logging.info("test_Thirddirectordering2:FALL")


    def test_Thirddirectordering3(self):
                url4 = baseurl + '/cloudphone/order/third/cancelOrder'
                MP4 = {
                    "orderId": read_yaml("order"),
                    "account": read_yaml("MP")["account"]
                }

                headers = {'appId': app_id,
                           'timestamp': timestamp,
                           'signature': "third_sys " + signature}

                res4 = requests.post(url=url4, json=MP4, headers=headers)
                print(res4.text)
                print(res4.headers)
                result3 = res4.text
                result3 = json.loads(result3)
                try:
                    assert "成功" in result3["header"]["errMsg"]
                    logging.info("test_Thirddirectordering3:SUCCESS")
                except Exception:
                    logging.info("test_Thirddirectordering3:FALL")

    '''营销订购'''
    def test_Marketing_platform(self, account, productItemCode, thirdOrderNo, renewOrderNo, orderType, channelCode):
        url = encodeurl + '/rai/sign/thirdOrder'
        MP = {
            "account": account,
            "productItemCode": productItemCode,
            "thirdOrderNo": thirdOrderNo,
            "renewOrderNo": renewOrderNo,
            "orderType": orderType,
            "channelCode": channelCode,
        }

        headers = {'appId': app_id,
                   'timestamp': timestamp,
                   'signature': "third_sys " + signature}
        try:
            res = requests.post(url=url, json=MP, headers=headers)
            logging.info("test_Marketing_platform:SUCCESS")
            # print(res.text)
            output = res.text
            outputs = json.loads(output)
            sign = outputs['sign']
            datas = {"sign": sign}
            write_yaml(datas)
            payload = {"MP": MP}
            write_yaml(payload)
        except Exception:
            logging.info("test_Marketing_platform:FALL")
        # output2 = res.json()
        # value=jsonpath.jsonpath(output2,"$.sign")
        # test_A.sign=value[0]
        # print(value[0])

    def test_Marketing_platform2(self):

        url2 = baseurl + '/cloudphone/subscribe/third/createOrder'

        MP2 = read_yaml("MP")
        MP2['account'] = read_yaml("MP")["account"]
        MP2['productItemCode'] = read_yaml("MP")["productItemCode"]
        MP2['thirdOrderNo'] = read_yaml("MP")["thirdOrderNo"]
        if read_yaml("MP")["renewOrderNo"] == '' or read_yaml("MP")["renewOrderNo"] == None:
            MP2['renewOrderNo'] = read_yaml("MP")['renewOrderNo']
            if read_yaml("MP")["orderType"] == "ORDER_BUY":
                pass
            elif read_yaml("MP")["orderType"] != "ORDER_BUY":
                read_yaml("MP")["orderType"] = ''
                print("购买类型有误！")
            else:
                print("输入有误！")

        elif read_yaml("MP")["renewOrderNo"] != '' or read_yaml("MP")["renewOrderNo"] != None:
            MP2['renewOrderNo'] = read_yaml("MP")['renewOrderNo']
            # print(MP2['renewOrderNo'])
            if read_yaml("MP")["orderType"] == "ORDER_RENEW":
                pass
            elif read_yaml("MP")["orderType"] != "ORDER_RENEW":
                read_yaml("MP")["orderType"] = ''
                print("购买类型有误！")
            else:
                print("输入有误！")
        else:
            print('输入有误')
        MP2['orderType'] = read_yaml("MP")['orderType']
        MP2['channelCode'] = read_yaml("MP")['channelCode']
        MP2['sign'] = read_yaml("sign")  # sign00

        headers = {'appId': app_id,
                   'timestamp': timestamp,
                   'signature': "third_sys " + signature}

        res = requests.post(url=url2, json=MP2, headers=headers)
        print(res.text)
        print(res.headers)
        result = res.text
        result = json.loads(result)
        try:
            assert "成功" in result["header"]["errMsg"]
            logging.info("test_Marketing_platform2:SUCCESS")
        except Exception:
            logging.info("test_Marketing_platform2:FALL")

    '''反向订购'''
    def test_Reverse_order(self,phone):
        urlr = f'http://sbo.cmtest.xyz/cloudphone-sign/rai/sign/encrypt?mobile={phone}'
        rr = requests.get(url=urlr)
        # print(rr.text)
        rrq = rr.text
        rrq = json.loads(rrq)
        customerId = rrq["mobile"]
        datas={"customerId":customerId}
        write_yaml(datas)

    def test_Reverse_order2(self,goodsId, outOrderId, oprType, notifyType, notifyiResult, expireTime, effectTime):
        url = baseurl + '/cloudphone/subscribe/third/raiBusinessNotify'
        PB = P
        PB["sign"] = "MCwCFB60foTBTR2342322249956456923423K66yRkfg=="
        PB["reqParam"]["orderItemList"][0]["goodsId"] = goodsId
        PB["reqParam"]["orderItemList"][0]["customerId"] =read_yaml("customerId")
        PB["reqParam"]["outOrderId"] = outOrderId
        PB["reqParam"]["oprType"] = oprType
        PB["reqParam"]["notifyType"] = notifyType
        PB["reqParam"]["notifyiResult"] = notifyiResult
        PB["reqParam"]["orderItemList"][0]["effectTime"] = effectTime
        PB["reqParam"]["orderItemList"][0]["expireTime"] = expireTime
        headers = {
            'Content-Type': 'application/json'
        }

        res = requests.post(url=url, json=PB, headers=headers)
        print(res.text)
        print(res.headers)
        result = res.text
        result = json.loads(result)
        payload={"P":P}
        write_yaml(payload)
        try:
            assert "成功" in result["data"]["rspParam"]["pubInfo"]["returnMsg"]
            logging.info("test_Reverse_order:SUCCESS")
        except Exception:
            logging.info("test_Reverse_order:FALL")

    '''验证token是否失效(现网环境)'''
    def test_username2(self):
        url="https://cpability.buy.139.com/cloudphone/member/getDetail"
        data={}
        headers = {
            'token': read_Vyaml("tokenn")
        }
        res=requests.post(url=url,json=data,headers=headers)
        # print(res.text)
        result=res.text
        result=json.loads(result)
        if result["header"]["errMsg"] =="成功":
            read_Vyaml("tokenn")
        else:
            clear_Vyaml()
            Token2()

    '''统一认证单点登录和订购'''
    def qtoken(self):
        test_CP().test_username2()
        url = "https://cpability.buy.139.com/cloudphone/user/login/sso/getUmcTmpToken"

        payload = json.dumps({})
        headers = {
        'token': read_Vyaml("tokenn"),
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)
        restoken=response.text
        restoken=json.loads(restoken)
        try:
            assert "成功" in restoken["header"]["errMsg"]
            logging.info("qtoken:SUCCESS")
            stoken = restoken["data"]["tmpToken"]
            datas = {"stoken": stoken}
            write_yaml(datas)
        except Exception:
            logging.info("qtoken:FALL")

    def test_sign(self,channelSrc,skuId,key,phone):
        urls=f"http://sbo.cmtest.xyz/cloudphone-sign/hmc/sign?key={key}&channelSrc={channelSrc}&skuId={skuId}&phone={phone}"

        hs=requests.get(url=urls)
        # print(hs.text)
        message=hs.text
        message=json.loads(message)
        timestamp=message["timestamp"]
        sign=message["sign"]
        datas={"timestamp":timestamp}
        datas2={"sign":sign}
        write_yaml(datas)
        write_yaml(datas2)

    def test_loginorder(self,channelSrc,skuId):

        url = "http://cc-hwy.cmtest.xyz/cloudphone/user/umcSSOAndOrder"

        payload = json.dumps({
        "token": read_yaml("stoken"),
        "channelSrc": channelSrc,
        "skuId": skuId,
        "timestamp": read_yaml("timestamp"),
        "sign": read_yaml("sign")
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        print(response.headers)
        result=response.text
        result=json.loads(result)
        try:
            assert "成功" in result["header"]["errMsg"]
            logging.info("test_loginorder:SUCCESS")
        except Exception:
            logging.info("test_loginorder:FALL")
