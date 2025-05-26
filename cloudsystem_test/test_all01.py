from random import randint
def test_02():
    account = 18475952281
    productItemCode = 100032629126
    thirdOrderNo = randint(9, 99999999999999999999999999)
    renewOrderNo = ''
    orderType = "ORDER_BUY"  # 订购：ORDER_BUY，续订：ORDER_RENEW
    channelCode = "782976529302"
    test01(account, productItemCode, thirdOrderNo, renewOrderNo, orderType, channelCode)
def test01(self,account, productItemCode, thirdOrderNo, renewOrderNo, orderType, channelCode):
    MP = {
        "account": account,
        "productItemCode": productItemCode,
        "thirdOrderNo": thirdOrderNo,
        "renewOrderNo": renewOrderNo,
        "orderType": orderType,
        "channelCode": channelCode,
    }
    print(MP)
