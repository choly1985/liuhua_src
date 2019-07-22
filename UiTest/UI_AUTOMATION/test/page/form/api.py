import json
import urllib.request
from UI_AUTOMATION.utils.config import Config
import time
import random
import jsonpath
import types
import re


# global content

class GBConnect():

    def __init__(self):
        c = Config().get('connect_date')
        self.tokenId = c.get('tokenId')
        self.url = c.get('url')
        self.userId = c.get('userId')
        self.orderSn = 13070510973314034652 + random.randint(0, 100000)

    # 获取字典中的objkey对应的值，适用于字典嵌套
    # dict:字典
    # objkey:目标key
    # default:找不到时返回的默认值
    # def dict_get(dict, objkey, default):
    #     tmp = dict
    #     for k, v in tmp.items():
    #         if k == objkey:
    #             return v
    #         else:
    #             if type(v) is types.DictType:
    #                 ret = dict_get(v, objkey, default)
    #                 if ret is not default:
    #                     return ret
    #     return default
    #
    # # 如
    # dicttest = {"result": {"code": "110002", "msg": "设备设备序列号或验证码错误"}}
    # ret = dict_get(dicttest, 'msg', None)
    # print(ret)


    def GB_token(self):
        url = self.url
        values = ({
                "header": {
                    "service": "com.globalegrow.spi.pay.inter.PayService",
                    "method": "checkout",
                    "domain": "",
                    "version": "1.0.0",
                    "tokenId": self.tokenId
                },
                "body": {
                    "siteCode": "GB",
                    "platform": 1,
                    "pipelineCode":"GB",
                    "lang": "en",
                    "parentOrderSn": str(self.orderSn),
                    "payAmount": 1000,
                    "returnUrl": "https://pay-dev.api.hqygou.com/solo/test/return",
                    "cancelUrl": "https://pay-dev.api.hqygou.com/solo/test/cancel",
                    "notifyUrl": "https://pay-dev.api.hqygou.com/solo/test/notify",
                    "orderInfos": [{
                        "orderSn": str(self.orderSn),
                        "orderType": 0,
                        "orderAmount": 1000,
                        "couponDeductAmount": 0,
                        "integralDeductAmount": 0,
                        "activityDeductAmount": 0,
                        "logisticCouponDeductAmount": 0,
                        "shippingFee": 0,
                        "insuranceFee": 0,
                        "trackingFee": 0,
                        "currencyCode": "TRY",
                        "currencyRate": 1,
                        "hasUseCoupon": 0,
                        "userId": 123,
                        "userEmail": "583241254@qq.com",
                        "exponent": 2,
                        "createTime": int(time.time()),
                        "orderAddressInfo": {
                            "firstName": "jiang",
                            "lastName": "jiahao",
                            "countryName": "United States",
                            "countryCode": "US",
                            "state": "Ariona",
                            "city": "Amado",
                            "addressLine1": "test",
                            "addressLine2": "test",
                            "postalCode": "00000000",
                            "telephone": "0000000000",
                            "email": "583241254@qq.com"
                        },
                        "orderGoodsInfos": [{
                            "goodsSn": "1111",
                            "title": "test",
                            "categoryId": 11111,
                            "categoryName": "test",
                            "price": 1000,
                            "qty": 1
                        }]
                    }],
                    "userInfo": {
                        "userId": 123,
                        "userEmail": "583241254@qq.com",
                        "createTime": 1552468638,
                        "userIp": "10.33.2.221",
                        "hasShippedRecords": 0
                    },
                    "billingAddressInfo": {
                        "firstName": "豪",
                        "lastName": "豪",
                        "countryCode": "US",
                        "state": "California",
                        "city": "Los Angeles",
                        "addressLine1": "test456",
                        "addressLine2": "test6456",
                        "postalCode": "00000000",
                        "telephone": "0000000000",
                        "email": "test@abc.com",
                        "streetNumber": "999"
                    }
                }
            })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()    # b'{"body":"{\\"code\\":0,\\"data1\\":{\\"payCurrencyAmount\\":\\
        # print(type(content),content)
        py_data = json.loads(content)    # {'body': '{"code":0,"data1":{"payCurrencyAmount":"",
        # print(type(py_data),py_data)
        a = py_data.get("body")
        # a = a.get("data1")
        # print(type(a), a)
        # a = re.findall(r'https://.*en/', a)
        index = a.find("https")
        # print(index)
        GBpayurl = a[index:index + 61]
        print(GBpayurl)



GBConnect().GB_token()
# GBConnect().dict_get()

