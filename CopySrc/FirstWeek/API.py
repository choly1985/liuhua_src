import json
import urllib.request
# post发送的数据
url = 'http://10.40.2.62:2087/gateway/'
values = ({
    "header": {
        "service": "com.globalegrow.member.spi.inter.IMemUserBaseInnerService",
        "method": "login",
        "domain": "",
        "version": "1.0.0",
        "tokenId": "809fdb0bfa0b2cfb9f4474690d3a3cb4"
    },
    "body": {
        "siteCode": "GB",
        "pipelineCode": "GB",
        "email": "583241254@qq.com",
        "password": "abc456456",
        "ip": "10.33.1.112",
        "loginType": 5,
        "plateform": 4,
        "imei": "11111",
        "userAgent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.11 (KHTML, like Gecko) Chrome/9.0.570.0 Safari/534.11",
        "timeZone": "+8",
        "country": "ES"
    }
}
)
jdata = json.dumps(values).encode()
req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
req.add_header("Content-Type", "application/json")
response = urllib.request.urlopen(req)  # 发送页面请求
content = response.read()
print(content)