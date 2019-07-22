import json
import urllib.request
from UI_AUTOMATION.utils.config import Config
import time
import random
import requests
# global content

class GBConnect():

    def __init__(self):
        c = Config().get('connect_date')
        self.tokenId = c.get('tokenId')
        self.url = c.get('url')
        self.userId = c.get('userId')
        self.orderSn = 13070510973314034652 + random.randint(0, 100000)



### 收银台url生成 ####
    def GB_payurl(self):
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
        GBpayurl = a[index:index + 66]
        print(GBpayurl)
        return GBpayurl

    def ZF_payurl(self):
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
                    "siteCode": "ZF",
                    "platform": 1,
                    "pipelineCode":"ZF",
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
        # print(GBpayurl)
        return GBpayurl



    ####默认地址####

    def GB_adress_US(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"Akiak",
                "countryCode":"US",
                "countryName":"United States",
                "email":"jiangjiahao@globalegrowUS.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "issuingAgency":"aaaaaaa",
                "middleName":"aaaa",
                "nationalIdNumber":"e324234",
                "passportIssueDate":936720000,
                "passportNo":"aaaaaaa",
                "passportSerial":"aaaaaaa",
                "phone":"1234567890",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"03189",
                "provinceCode":"3479",
                "provinceName":"Alava",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "122",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Spain(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"citttt",
                "countryCode":"ES",
                "countryName":"Spain",
                "email":"jiangjiahao@globalegrowES.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"03189",
                "provinceCode":"3479",
                "provinceName":"Alava",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "44",
                "nationalIdNumber":"234",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Peru(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"AIJA",
                "countryCode":"PE",
                "countryName":"Peru",
                "email":"jiangjiahao@globalegrowPE.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"234234",
                "provinceCode":"2857",
                "provinceName":"Ancash",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "1617",
                "nationalIdNumber":"12345678",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)


    def GB_adress_Italy(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"Acqui Terme",
                "countryCode":"IT",
                "countryName":"Italy",
                "email":"jiangjiahao@globalegrowIT.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"1234567890",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"09170",
                "provinceCode":"1679",
                "provinceName":"Alessandria",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "1617",
                "nationalIdNumber":"234",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Slovakia(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"COYHAIQUE",
                "countryCode":"SK",
                "countryName":"Slovakia",
                "email":"jiangjiahao@globalegrowSK.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"08203",
                "provinceCode":"3233",
                "provinceName":"KoSicky kraj",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "3170",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Chile(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"COYHAIQUE",
                "countryCode":"CL",
                "countryName":"Chile",
                "email":"jiangjiahao@globalegrowCL.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"234234",
                "provinceCode":"798",
                "provinceName":"Aysen Region",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "783",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Thailand(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"ccity",
                "countryCode":"TH",
                "countryName":"Thailand",
                "email":"jiangjiahao@globalegrowTH.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"234234",
                "provinceCode":"C3699",
                "provinceName":"Chaiyaphum",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "3699",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Malaysia(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"ccity",
                "countryCode":"MY",
                "countryName":"Malaysia",
                "email":"jiangjiahao@globalegrowMY.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"234234",
                "provinceCode":"2652",
                "provinceName":"Melaka",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "2590",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Nigeria(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"ccity",
                "countryCode":"NG",
                "countryName":"Nigeria",
                "email":"jiangjiahao@globalegrowNG.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"234234",
                "provinceCode":"2701",
                "provinceName":"Anambra",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "29",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Germany(self):

            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"BERLIN",
                "countryCode":"DE",
                "countryName":"Germany",
                "email":"jiangjiahao@globalegrowDE.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"1234567890",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"99510",
                "provinceCode":"920",
                "provinceName":"Berlin",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "29",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Austria(self):

            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"METNITZ",
                "countryCode":"AT",
                "countryName":"Austria",
                "email":"jiangjiahao@globalegrowAT.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"08215",
                "provinceCode":"323",
                "provinceName":"Karnten",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "10",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Belgium(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"AARTSELAAR",
                "countryCode":"BE",
                "countryName":"Belgium",
                "email":"jiangjiahao@globalegrowBE.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"2970",
                "provinceCode":"503",
                "provinceName":"Antwerpen",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "310",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Argentina(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"SALTA",
                "cityCode":"cityCode",
                "countryCode":"AR",
                "countryName":"Argentina",
                "email":"jiangjiahao@globalegrowAR.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"1234567890",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"08215",
                "provinceCode":"297",
                "provinceName":"Salta",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "310",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Colombia(self):

            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"TAME",
                "cityCode":"cityCode",
                "countryCode":"CO",
                "countryName":"Colombia",
                "email":"jiangjiahao@globalegrowCO.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"08215",
                "provinceCode":"825",
                "provinceName":"Arauca",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "taxNumber":"hhhhh, 455434, 999",
                "cdpId": "810",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Indonesia(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"cityg",
                "cityCode":"cityCode",
                "countryCode":"ID",
                "countryName":"Indonesia",
                "email":"jiangjiahao@globalegrowIn.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"62-666555444",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"08215",
                "provinceCode":"1526",
                "provinceName":"Bengkulu",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "cdpId":"1464",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Russian(self):
            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"ffff",
                "countryCode":"RU",
                "countryName":"Russian Federation",
                "email":"jiangjiahao@globalegrowru.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"1234567890",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"100000",
                "provinceCode":"3115",
                "provinceName":"Bryanskaya oblast",
                "siteCode":"GB",
                "birthDay":"2000-00-00",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Mexico(self):

            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345",
                "cityName":"ffff",
                "countryCode":"MX",
                "countryName":"Mexico",
                "email":"jiangjiahao@globalegrowmx.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"1888888812",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"60950",
                "provinceCode":"2618",
                "provinceName":"Baja California",
                "siteCode":"GB",
                "taxNumber":"hhhhh, 455434, 999",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Turkey(self):

            values = {
                "addressId":6,
                "addressLine1":"hhhhh123456",
                "addressLine2":"12345ee",
                "cityName":"ffff",
                "countryCode":"TR",
                "countryName":"Turkey",
                "email":"jiangjiahao@globalegrow.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"90-1888888812",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"01960",
                "provinceCode":"C3342",
                "provinceName":"Agri",
                "siteCode":"GB",
                "taxNumber":"hhhhh, 455434, 999",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Poland(self):

            values = {
                "addressId":6,
                "addressLine1":"hhhhh2343224",
                "addressLine2":"12345",
                "cityName":"ffff",
                "countryCode":"PL",
                "countryName":"Poland",
                "email":"haoauto@1ui.compersi",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"123456789",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"00-950",
                "provinceCode":"2997",
                "provinceName":"Opolskie",
                "siteCode":"GB",
                "taxNumber":"hhhhh, 455434, 999",
                "userId":self.userId
            }

            GBConnect().GB_adress(values)

    def GB_adress_Brazilpoli(self):

            values = {
                "addressId":6,
                "addressLine1":"hhhhh01354445654",
                "addressLine2":"12345",
                "cityName":"ffff",
                "countryCode":"BR",
                "countryName":"Brazil",
                "email":"haoauto@1ui.comBRpoli",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"55-1888888812",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"13165-000",
                "provinceCode":"640",
                "provinceName":"Bahia",
                "siteCode":"GB",
                "taxNumber":"hhhhh, 455434, 999",
                "userId":self.userId
            }

            GBConnect().GB_adress(values)

    def GB_adress_Brazil(self):

            values = {
                "addressId":6,
                "addressLine1":"hhhhh01354445654",
                "addressLine2":"12345",
                "cityName":"ffff",
                "countryCode":"BR",
                "countryName":"Brazil",
                "email":"haoauto@1ui.comBR",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"55-1888888812",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"13165-000",
                "provinceCode":"640",
                "provinceName":"Bahia",
                "siteCode":"GB",
                "taxNumber":"hhhhh, 455434, 999",
                "userId":self.userId
            }
            GBConnect().GB_adress(values)

    def GB_adress_Portugal(self):

            values = {
                "addressId":6,
                "addressLine1":"hhhhh01354445654",
                "addressLine2":"12345",
                "cityName":"ffff",
                "countryCode":"PT",
                "countryName":"Portugal",
                "email":"haoauto@1ui.comPT",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"55-1888888812",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"4490-601",
                "provinceCode":"3013",
                "provinceName":"Evora",
                "siteCode":"GB",
                "taxNumber":"hhhhh, 455434, 999",
                "userId":self.userId
            }

            GBConnect().GB_adress(values)




    def GB_adress_India(self):

        values = {
                "addressId":6,
                "addressLine1":"hhhhh01354445654",
                "addressLine2":"12345",
                "cityName":"ffff",
                "countryCode":"IN",
                "countryName":"India",
                "email":"haoauto@1ui.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"1888888822",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"234234",
                "provinceCode":"C3342",
                "provinceName":"Orissa",
                "siteCode":"GB",
                "taxNumber":"hhhhh, 455434, 999",
                "userId":self.userId
            }
        GBConnect().GB_adress(values)



    def GB_adress(self, values):
        url = self.url
        values = ({
            "header":{
                "service":"com.globalegrow.member.spi.inter.IMemAddressInnerService",
                "method":"edit",
                "domain":"",
                "version":"1.0.0",
                "tokenId":self.tokenId
            },
            "body":
                values
        })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        print(content)
        # return content

    def GB_adress_Switzerland(self):

        values = {"addressId":6,
                "addressLine1":"hhhhh01354445654",
                "addressLine2":"12345",
                "cityName":"GRUB AR",
                "countryCode":"CH",
                "countryName":"Switzerland",
                "email":"haoauto@1CH.com",
                "firstName":"hhh",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"51-123456789",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"2970",
                "provinceCode":"3571",
                "provinceName":"Appenzell Ausserrhoden",
                "siteCode":"GB",
                "taxNumber":"test test test, test",
                "userId": self.userId}
        GBConnect().GB_adress(values)

    def GB_adress_Philippines(self):

        values = {"addressId":6,
                "addressLine1":"hhhhh01354445654",
                "addressLine2":"12345",
                "cityName":"Butuan City",
                "cityCode":"Butuan City",
                "countryCode":"PH",
                "countryName":"Philippines",
                "email":"haoauto@1PH.com",
                "firstName":"hhh",
                "middleName":"hhh",
                "passportSerial":"hhh",
                "passportNo":"hhh",
                "passportIssueDate":"1576080000",
                "dateInput":"12/12/2019",
                "issuingAgency":"Austria",
                "isDefaultAddr":1,
                "lastName":"hhh",
                "phone":"63-1234567890",
                "pipelineCode":"GB",
                "platform":1,
                "postalCode":"411023",
                "provinceCode":"2903",
                "provinceName":"Appenzell Ausserrhoden",
                "siteCode":"GB",
                "taxNumber":"test test test, test",
                "cdpId":"2840",
                "userId": self.userId}
        GBConnect().GB_adress(values)

    ####信用卡渠道抛送（新）####
    def GB_CREDITCARD_channel_worldpay(self):
        url = self.url
        values = ({
            "header": {
                "service": "com.globalegrow.spi.mpay.inter.PayChannelPlatformCountryService",
                "method": "update",
                "domain": "",
                "version": "1.0.0",
                "tokenId": self.tokenId
            },
            "body": {
                "channelCodes":"[\"worldpay\",\"checkout_credit\",\"GC\",\"ADN_CC\"]",
                "id":77,
                "logInfo":{
                    "ip":"10.33.1.189",
                    "userId":177,
                    "userName":"chenmudan"
                },
                "settingStatus":1
            }
            })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        # print(content)

    def GB_CREDITCARD_channel_checkout_credit(self):
        url = self.url
        values = ({
            "header": {
                "service": "com.globalegrow.spi.mpay.inter.PayChannelPlatformCountryService",
                "method": "update",
                "domain": "",
                "version": "1.0.0",
                "tokenId": self.tokenId
            },
            "body": {
                "channelCodes":"[\"checkout_credit\",\"worldpay\",\"GC\",\"ADN_CC\"]",
                "id":77,
                "logInfo":{
                    "ip":"10.33.1.189",
                    "userId":177,
                    "userName":"chenmudan"
                },
                "settingStatus":1
            }
        })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        print(content)


    def GB_CREDITCARD_channel_ADN_CC(self):
        url = self.url
        values = ({
            "header": {
                "service": "com.globalegrow.spi.mpay.inter.PayChannelPlatformCountryService",
                "method": "update",
                "domain": "",
                "version": "1.0.0",
                "tokenId": self.tokenId
            },
            "body": {
                "channelCodes":"[\"ADN_CC\",\"worldpay\",\"checkout_credit\",\"GC\"]",
                "id":77,
                "logInfo":{
                    "ip":"10.33.1.189",
                    "userId":177,
                    "userName":"chenmudan"
                },
                "settingStatus":1
            }
            })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        # print(content)


    def GB_CREDITCARD_channel_GC(self):
        url = self.url
        values = ({
            "header": {
                "service": "com.globalegrow.spi.mpay.inter.PayChannelPlatformCountryService",
                "method": "update",
                "domain": "",
                "version": "1.0.0",
                "tokenId": self.tokenId
            },
            "body": {
                "channelCodes":"[\"GC\",\"ADN_CC\",\"worldpay\",\"checkout_credit\"]",
                "id":77,
                "logInfo":{
                    "ip":"10.33.1.189",
                    "userId":177,
                    "userName":"chenmudan"
                },
                "settingStatus":1
            }
            })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        # print(content)




    ####土耳其国家支付抛送####

    def GB_creditcard(self):
        url = self.url
        values = ({
            "header": {
                "service": "com.globalegrow.spi.mpay.inter.PayChannelRelationService",
                "method": "addPayChannelCountryRelation",
                "domain": "",
                "tokenId": self.tokenId,
                "version": "1.0.0"
            },
            "body": {
                "countryPayTypes":{
                    "main":[
                        "PAYPAL",
                        "GC",
                        "BOLETO",
                        "WESTERN",
                        "BANK_TRANSFER",
                        "WALLET",
                        "worldpay",
                        "CashU",
                        "ideal",
                        "yandex_money",
                        "checkout_credit",
                        "ebanxinstalment",
                        "BankTransfer",
                        "PagoEfectivo",
                        "OXXO",
                        "PSE",
                        "SOFORT_SSL",
                        "Giropay",
                        "LipaPay",
                        "ADN_CC",
                        "Postepay",
                        "EBX_MXCC",
                        "ADN_RUCT",
                        "PayU_BKM",
                        "PayU_TRCC",
                        "CREDITCARD",
                        "PP_Express",
                        "PP_Credit_E",
                        "PP_Credit",
                        "PP_CC",
                        "ADN_EPS",
                        "ADN_DEGP",
                        "ADN_TRSP",
                        "ADN_MYOB",
                        "ADN_IDATM",
                        "ADN_IDACS",
                        "ADN_THOB",
                        "ADN_BEBC",
                        "WP_P24",
                        "WP_QIWI",
                        "poli",
                        "EBX_AGPC",
                        "ADN_PTMB",
                        "EBX_SVPG",
                        "IE_RUWM",
                        "WPG_Pay",
                        "PayU_INNB",
                        "ZYPaytm",
                        "PayU_UPI",
                        "DGPAY_PHdp"
                    ],
                    "TR":[
                        "PAYPAL",
                        "BOLETO",
                        "WESTERN",
                        "WALLET",
                        "qiwi",
                        "checkout_credit",
                        "ebanxinstalment",
                        "BankTransfer",
                        "EBX_MXCC",
                        "PayU_BKM",
                        "PayU_TRCC",
                        "EBX_AGPC",
                        "EBX_SVPG"
                    ]
                },
                "countrys":"TR",
                "logInfo":{
                    "ip":"10.33.1.189",
                    "userId":2,
                    "userName":"zhangwei"
                },
                "pipelineCode":"GB",
                "platform":1,
                "siteCode":"GB"
               }
               })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type", "application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        # print(content)

    def GB_worldpay(self):
        url = self.url
        values = ({
        "header": {
            "service": "com.globalegrow.spi.mpay.inter.PayChannelRelationService",
            "method": "addPayChannelCountryRelation",
            "domain": "",
            "tokenId":self.tokenId,
            "version": "1.0.0"
        },
        "body": {
            "countryPayTypes":{
                "main":[
                    "PAYPAL",
                    "GC",
                    "BOLETO",
                    "WESTERN",
                    "BANK_TRANSFER",
                    "WALLET",
                    "worldpay",
                    "CashU",
                    "ideal",
                    "yandex_money",
                    "checkout_credit",
                    "ebanxinstalment",
                    "BankTransfer",
                    "PagoEfectivo",
                    "OXXO",
                    "PSE",
                    "SOFORT_SSL",
                    "Giropay",
                    "LipaPay",
                    "ADN_CC",
                    "Postepay",
                    "EBX_MXCC",
                    "ADN_RUCT",
                    "PayU_BKM",
                    "PayU_TRCC",
                    "CREDITCARD",
                    "PP_Express",
                    "PP_Credit_E",
                    "PP_Credit",
                    "PP_CC",
                    "ADN_EPS",
                    "ADN_DEGP",
                    "ADN_TRSP",
                    "ADN_MYOB",
                    "ADN_IDATM",
                    "ADN_IDACS",
                    "ADN_THOB",
                    "ADN_BEBC",
                    "WP_P24",
                    "WP_QIWI",
                    "poli",
                    "EBX_AGPC",
                    "ADN_PTMB",
                    "EBX_SVPG",
                    "IE_RUWM",
                    "WPG_Pay",
                    "PayU_INNB",
                    "ZYPaytm",
                    "PayU_UPI",
                    "DGPAY_PHdp"
                ],
                "TR":[
                    "PAYPAL",
                    "BOLETO",
                    "WESTERN",
                    "worldpay",
                    "qiwi",
                    "ebanxinstalment",
                    "BankTransfer",
                    "EBX_MXCC",
                    "PayU_BKM",
                    "PayU_TRCC",
                    "EBX_AGPC",
                    "EBX_SVPG"
                ]
            },
            "countrys":"TR",
            "logInfo":{
                "ip":"10.33.1.189",
                "userId":2,
                "userName":"zhangwei"
            },
            "pipelineCode":"GB",
            "platform":1,
            "siteCode":"GB"
            }
            })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type", "application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        # print(content)

    def GB_ADN_CC(self):
        url = self.url
        values = ({
            "header": {
                "service": "com.globalegrow.spi.mpay.inter.PayChannelRelationService",
                "method": "addPayChannelCountryRelation",
                "domain": "",
                "tokenId": self.tokenId,
                "version": "1.0.0"
            },
            "body": {
                "countryPayTypes":{
                    "main":[
                        "PAYPAL",
                        "GC",
                        "BOLETO",
                        "WESTERN",
                        "BANK_TRANSFER",
                        "WALLET",
                        "worldpay",
                        "CashU",
                        "ideal",
                        "yandex_money",
                        "checkout_credit",
                        "ebanxinstalment",
                        "BankTransfer",
                        "PagoEfectivo",
                        "OXXO",
                        "PSE",
                        "SOFORT_SSL",
                        "Giropay",
                        "LipaPay",
                        "ADN_CC",
                        "Postepay",
                        "EBX_MXCC",
                        "ADN_RUCT",
                        "PayU_BKM",
                        "PayU_TRCC",
                        "CREDITCARD",
                        "PP_Express",
                        "PP_Credit_E",
                        "PP_Credit",
                        "PP_CC",
                        "ADN_EPS",
                        "ADN_DEGP",
                        "ADN_TRSP",
                        "ADN_MYOB",
                        "ADN_IDATM",
                        "ADN_IDACS",
                        "ADN_THOB",
                        "ADN_BEBC",
                        "WP_P24",
                        "WP_QIWI",
                        "poli",
                        "EBX_AGPC",
                        "ADN_PTMB",
                        "EBX_SVPG",
                        "IE_RUWM",
                        "WPG_Pay",
                        "PayU_INNB",
                        "ZYPaytm",
                        "PayU_UPI",
                        "DGPAY_PHdp"
                    ],
                    "TR":[
                        "PAYPAL",
                        "BOLETO",
                        "WESTERN",
                        "WALLET",
                        "qiwi",
                        "ebanxinstalment",
                        "BankTransfer",
                        "ADN_CC",
                        "EBX_MXCC",
                        "PayU_BKM",
                        "PayU_TRCC",
                        "EBX_AGPC",
                        "EBX_SVPG"
                    ]
                },
                "countrys":"TR",
                "logInfo":{
                    "ip":"10.33.1.189",
                    "userId":2,
                    "userName":"zhangwei"
                },
                "pipelineCode":"GB",
                "platform":1,
                "siteCode":"GB"
            }
            })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type", "application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        # print(content)

    def GB_GC(self):
        url = self.url
        values = ({
            "header": {
                "service": "com.globalegrow.spi.mpay.inter.PayChannelRelationService",
                "method": "addPayChannelCountryRelation",
                "domain": "",
                "tokenId": self.tokenId,
                "version": "1.0.0"
            },
            "body": {
                "countryPayTypes":{
                    "TR":[
                        "PAYPAL",
                        "GC",
                        "BOLETO",
                        "WESTERN",
                        "WALLET",
                        "qiwi",
                        "BankTransfer",
                        "EBX_MXCC",
                        "PayU_BKM",
                        "PayU_TRCC",
                        "EBX_AGPC",
                        "EBX_SVPG"
                    ],
                    "main":[
                        "PAYPAL",
                        "GC",
                        "BOLETO",
                        "WESTERN",
                        "BANK_TRANSFER",
                        "WALLET",
                        "worldpay",
                        "CashU",
                        "webmoney",
                        "qiwi",
                        "ideal",
                        "yandex_money",
                        "checkout_credit",
                        "ebanxinstalment",
                        "BankTransfer",
                        "PagoEfectivo",
                        "OXXO",
                        "PSE",
                        "SOFORT_SSL",
                        "Przelewy24",
                        "Giropay",
                        "LipaPay",
                        "ADN_CC",
                        "Postepay",
                        "EBX_MXCC",
                        "ADN_RUCT",
                        "PayU_BKM",
                        "PayU_TRCC",
                        "CREDITCARD",
                        "PP_Credit",
                        "PP_CC",
                        "ADN_EPS",
                        "ADN_DEGP",
                        "ADN_TRSP",
                        "ADN_MYOB",
                        "ADN_IDATM",
                        "ADN_IDACS",
                        "ADN_THOB",
                        "ADN_BEBC",
                        "WP_P24",
                        "WP_QIWI",
                        "poli",
                        "EBX_AGPC",
                        "ADN_PTMB",
                        "EBX_SVPG",
                        "PayU_INNB",
                        "PayU_UPI",
                        "DGPAY_PHdp"
                    ]
                },
                "countrys":"TR",
                "logInfo":{
                    "ip":"10.33.1.189",
                    "userId":2,
                    "userName":"zhangwei"
                },
                "pipelineCode":"GB",
                "platform":1,
                "siteCode":"GB"
            }
            })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type", "application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        # print(content)

    #######支付排序#####

    def GB_sort_Brazil(self):
        url = self.url
        values = ({
            "header": {
                "service": "com.globalegrow.spi.mpay.inter.PayChannelRelationService",
                "method": "addPayChannelCountryRelation",
                "domain": "",
                "tokenId": self.tokenId,
                "version": "1.0.0"
            },
            "body": {
                "countryInfoList":[
                    {
                        "countryCode":"BR",
                        "countryName":"Brazil"
                    }
                        ],
                        "defaultChannel":"PAYPAL",
                        "hasDefault":1,
                        "logInfo":{
                            "ip":"10.33.1.189",
                            "userId":2,
                            "userName":"zhangwei"
                        },
                        "payChannelInfoList":[
                            {
                                "displayOrder":0,
                                "payChannelCode":"ebanxinstalment",
                                "payChannelName":"ebanx-instalment"
                            },
                            {
                                "displayOrder":1,
                                "payChannelCode":"PAYPAL",
                                "payChannelName":"PAYPAL"
                            },
                            {
                                "displayOrder":2,
                                "payChannelCode":"BOLETO",
                                "payChannelName":"BOLETO"
                            },
                            {
                                "displayOrder":3,
                                "payChannelCode":"CREDITCARD",
                                "payChannelName":"Credit Card"
                            },
                            {
                                "displayOrder":4,
                                "payChannelCode":"WPG_Pay",
                                "payChannelName":"WPG_Pay"
                            },
                            {
                                "displayOrder":5,
                                "payChannelCode":"PP_Credit",
                                "payChannelName":"PP_Credit"
                            },
                            {
                                "displayOrder":6,
                                "payChannelCode":"EBX_MXCC",
                                "payChannelName":"EBX_MXCC"
                            },
                            {
                                "displayOrder":7,
                                "payChannelCode":"ideal",
                                "payChannelName":"ideal"
                            },
                            {
                                "displayOrder":8,
                                "payChannelCode":"OXXO",
                                "payChannelName":"OXXO"
                            },
                            {
                                "displayOrder":9,
                                "payChannelCode":"WP_P24",
                                "payChannelName":"WP_P24"
                            },
                            {
                                "displayOrder":10,
                                "payChannelCode":"Przelewy24",
                                "payChannelName":"Przelewy24"
                            },
                            {
                                "displayOrder":11,
                                "payChannelCode":"SOFORT_SSL",
                                "payChannelName":"SOFORT"
                            },
                            {
                                "displayOrder":12,
                                "payChannelCode":"ADN_DEGP",
                                "payChannelName":"ADN_DEGP"
                            },
                            {
                                "displayOrder":13,
                                "payChannelCode":"ADN_EPS",
                                "payChannelName":"ADN_EPS"
                            },
                            {
                                "displayOrder":14,
                                "payChannelCode":"yandex_money",
                                "payChannelName":"yandex_money"
                            },
                            {
                                "displayOrder":15,
                                "payChannelCode":"webmoney",
                                "payChannelName":"webmoney"
                            },
                            {
                                "displayOrder":16,
                                "payChannelCode":"qiwi",
                                "payChannelName":"qiwi"
                            },
                            {
                                "displayOrder":17,
                                "payChannelCode":"Postepay",
                                "payChannelName":"WP_PSTP"
                            },
                            {
                                "displayOrder":18,
                                "payChannelCode":"ADN_BEBC",
                                "payChannelName":"ADN_BEBC"
                            },
                            {
                                "displayOrder":19,
                                "payChannelCode":"PSE",
                                "payChannelName":"PSE"
                            },
                            {
                                "displayOrder":20,
                                "payChannelCode":"LipaPay",
                                "payChannelName":"LipaPay"
                            },
                            {
                                "displayOrder":21,
                                "payChannelCode":"PagoEfectivo",
                                "payChannelName":"PagoEfectivo"
                            },
                            {
                                "displayOrder":22,
                                "payChannelCode":"PayU_BKM",
                                "payChannelName":"PayU_BKM"
                            },
                            {
                                "displayOrder":23,
                                "payChannelCode":"PayU_TRCC",
                                "payChannelName":"PayU_TRCC"
                            },
                            {
                                "displayOrder":24,
                                "payChannelCode":"ADN_IDATM",
                                "payChannelName":"ADN_IDATM"
                            },
                            {
                                "displayOrder":25,
                                "payChannelCode":"ADN_IDACS",
                                "payChannelName":"ADN_IDACS"
                            },
                            {
                                "displayOrder":26,
                                "payChannelCode":"ADN_MYOB",
                                "payChannelName":"ADN_MYOB"
                            },
                            {
                                "displayOrder":27,
                                "payChannelCode":"ADN_THOB",
                                "payChannelName":"ADN_THOB"
                            },
                            {
                                "displayOrder":28,
                                "payChannelCode":"ADN_RUCT",
                                "payChannelName":"ADN_RUCT"
                            },
                            {
                                "displayOrder":29,
                                "payChannelCode":"ADN_TRSP",
                                "payChannelName":"ADN_TRSP"
                            },
                            {
                                "displayOrder":30,
                                "payChannelCode":"BankTransfer",
                                "payChannelName":"BankTransfer"
                            },
                            {
                                "displayOrder":31,
                                "payChannelCode":"BANK_TRANSFER",
                                "payChannelName":"银行卡转账"
                            },
                            {
                                "displayOrder":32,
                                "payChannelCode":"WESTERN",
                                "payChannelName":"西联"
                            },
                            {
                                "displayOrder":33,
                                "payChannelCode":"WALLET",
                                "payChannelName":"WALLET"
                            },
                            {
                                "displayOrder":34,
                                "payChannelCode":"BITCOIN",
                                "payChannelName":"Bitcoin"
                            },
                            {
                                "displayOrder":35,
                                "payChannelCode":"CashU",
                                "payChannelName":"CashU"
                            },
                            {
                                "displayOrder":36,
                                "payChannelCode":"EPS",
                                "payChannelName":"EPS"
                            },
                            {
                                "displayOrder":37,
                                "payChannelCode":"GIFTCARD",
                                "payChannelName":"GIFTCARD"
                            },
                            {
                                "displayOrder":38,
                                "payChannelCode":"Giropay",
                                "payChannelName":"Giropay"
                            },
                            {
                                "displayOrder":39,
                                "payChannelCode":"PP_CC",
                                "payChannelName":"PP_CC"
                            },
                            {
                                "displayOrder":40,
                                "payChannelCode":"PP_Express",
                                "payChannelName":"PP_Express"
                            },
                            {
                                "displayOrder":41,
                                "payChannelCode":"PP_Credit_E",
                                "payChannelName":"PP_Credit_E"
                            },
                            {
                                "displayOrder":42,
                                "payChannelCode":"WP_QIWI",
                                "payChannelName":"WP_QIWI"
                            },
                            {
                                "displayOrder":43,
                                "payChannelCode":"ADN_PTMB",
                                "payChannelName":"ADN_PTMB"
                            },
                            {
                                "displayOrder":44,
                                "payChannelCode":"EBX_SVPG",
                                "payChannelName":"EBX_SVPG"
                            },
                            {
                                "displayOrder":45,
                                "payChannelCode":"EBX_AGPC",
                                "payChannelName":"EBX_AGPC"
                            },
                            {
                                "displayOrder":46,
                                "payChannelCode":"poli",
                                "payChannelName":"poli"
                            },
                            {
                                "displayOrder":47,
                                "payChannelCode":"PayU_UPI",
                                "payChannelName":"PayU_UPI"
                            },
                            {
                                "displayOrder":48,
                                "payChannelCode":"PayU_INNB",
                                "payChannelName":"PayU_INNB"
                            },
                            {
                                "displayOrder":49,
                                "payChannelCode":"IE_RUWM",
                                "payChannelName":"IE_RUWM"
                            },
                            {
                                "displayOrder":50,
                                "payChannelCode":"ZYPaytm",
                                "payChannelName":"ZYPaytm"
                            },
                            {
                                "displayOrder":51,
                                "payChannelCode":"Zero_OrderPayment",
                                "payChannelName":"Zero_OrderPayment"
                            },
                            {
                                "displayOrder":52,
                                "payChannelCode":"DGPAY_PHdp",
                                "payChannelName":"DGPAY_PHdp"
                            }
                        ],
                        "platform":1,
                        "siteCode":"GB",
                        "templateCode":"PT18110418354706",
                        "templateName":"baxi"
                    }
                })
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type", "application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        # print(content)
        # return content

    def GB_delete_card(self):
        url = "https://cashier.gearbest.net/api/v1/delete/card"
        values = {
                "token": "O190409009733145055JE2",
                "tokenisation": "asdkjrhwiuehfauishfuiwehfukashgtuwetlkas"
        }
        res = requests.post(url=url, json=values, verify=False)  # JSON格式的请求，将数据赋给json参数
        print(res.text)




if __name__ == "__main__":

    # GBConnect().GB_creditcard()
    # GBConnect().GB_adress_Brazil()
    # GBConnect().GB_CREDITCARD_channel_checkout_credit()
    # GBConnect().GB_adress_Turkey()
    # GBConnect().GB_worldpay()
    # GBConnect().GB_payurl()
    # GBConnect().ZF_payurl()
    # GBConnect().GB_delete_card()
    GBConnect().GB_adress_Spain()


