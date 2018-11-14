import requests
import json
token = "809fdb0bfa0b2cfb9f4474690d3a3cb4"
url = 'http://10.40.2.62:2087/gateway/'
headerdata = {
    "Content-type": "application/json"
}
postData = json.dumps({
    "header": {
        "service": "com.globalegrow.member.spi.inter.IMemUserBaseInnerService",
        "method": "login",
        "domain": "",
        "version": "1.0.0",
        "tokenId": "token"
    },
    "body": {
        "siteCode": "GB",
        "pipelineCode": "GB",
        "email": "583241254@qq.com",
        "password": "abc456456",
        "ip": "1.3.69.9",
        "loginType": 5,
        "plateform": 4,
        "imei": "11111",
        "userAgent": "jiangjiahao",
        "timeZone": "+8",
        "country": "ES"
    }
})
response = requests.post(url, data=postData)
print(response.text)
