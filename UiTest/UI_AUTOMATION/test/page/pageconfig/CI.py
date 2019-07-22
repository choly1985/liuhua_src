import json
import hashlib    #md5 加密库
import urllib.request
from UI_AUTOMATION.utils.config import Config
from UI_AUTOMATION.utils.HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from time import sleep
import time, datetime
import operator

# driver = webdriver.Chrome()
#
# driver.get("C:/Users/jiangjiahao/AppData/Roaming/Foxmail7/Temp-13608-20181228210533/Attach/PAY_Report%2020181228-211818.html")
# # driver.maximize_window()
# # sleep(0.5)
# # driver.find_element_by_xpath('//*[@src="https://css.gbtcdn.com/imagecache/GB3/images/domeimg/pay_method/PayU_BKM.png"]').click()
#
#
#
# # with open('F:\\python\\soa-ui-master\\UI_AUTOMATION\\report\\PAY_Report 20181229-155625.html') as f:
# #     s=f.read()
# # print(s)
#
#
#
# # import os
# # main = "F:\\python\\soa-ui-master\\UI_AUTOMATION\\report\\PAY_Report 20181229-155625.html"
# # r_v = os.system(main)
# sleep(0.5)
# # /html/body/div[2]/p[1]/text()
# title = driver.find_element_by_xpath("/html/body/div[2]/h1").text
# start_time = driver.find_element_by_xpath('//*[@class="heading"]/p[1]').text
# do_time = driver.find_element_by_xpath('//*[@class="heading"]/p[2]').text
# all_case = driver.find_element_by_xpath('//*[@id="result_table"]/tbody/tr[2]/td[2]').text
# case_pass_total = driver.find_element_by_xpath('//*[@id="result_table"]/tbody/tr[2]/td[3]').text
# case_wrong_total = driver.find_element_by_xpath('//*[@id="result_table"]/tbody/tr[2]/td[4]').text
# case_error_total = driver.find_element_by_xpath('//*[@id="result_table"]/tbody/tr[2]/td[5]').text
# case1 = driver.find_element_by_xpath('//*[@id="ft1.1"]/td[1]/div').text
# case1_status = driver.find_element_by_xpath('//*[@id="ft1.1"]/td[2]/span/a').text
#
# case2 = driver.find_element_by_xpath('//*[@id="ft1.2"]/td[1]/div').text
# case2_status = driver.find_element_by_xpath('//*[@id="ft1.2"]/td[2]/span/a').text

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

class GBConnect():
    def __init__(self):
        c = Config().get('connect_date')
        self.tokenId = c.get('tokenId')
        self.url = c.get('url')
        self.userId = c.get('userId')

    def CI_pc_page(self, report1, runner):                     #通过页面获取数据
        driver = webdriver.Chrome()
        driver.get(report1)
        sleep(0.5)
        driver.find_element_by_xpath("//a[contains(text(),'所有')]").click()
        sleep(0.5)
        title = driver.find_element_by_xpath("/html/body/div[2]/h1").text
        excute_start_time = driver.find_element_by_xpath('//*[@class="heading"]/p[1]').text
        excute_start_time = excute_start_time[6:26]
        excute_time = driver.find_element_by_xpath('//*[@class="heading"]/p[2]').text
        excute_time = excute_time[6:26]
        case_total = driver.find_element_by_xpath('//*[@id="result_table"]/tbody/tr[2]/td[2]').text
        case_pass_total = driver.find_element_by_xpath('//*[@id="result_table"]/tbody/tr[2]/td[3]').text
        case_wrong_total = driver.find_element_by_xpath('//*[@id="result_table"]/tbody/tr[2]/td[4]').text
        case_error_total = driver.find_element_by_xpath('//*[@id="result_table"]/tbody/tr[2]/td[5]').text
        # try:
        #     case1 = driver.find_element_by_xpath('//*[@id="ft1.1"]/td[1]/div').text     # //*[@id="pt1.1"]/td[1]/div
        #     case1_status = driver.find_element_by_xpath('//*[@id="ft1.1"]/td[2]/span/a').text  # //*[@id="pt1.1"]/td[2]/span
        # except:
        #     case1 = driver.find_element_by_xpath('//*[@id="pt1.1"]/td[1]/div').text     # //*[@id="pt1.1"]/td[1]/div
        #     case1_status = driver.find_element_by_xpath('//*[@id="pt1.1"]/td[2]/span').text   #  //*[@id="pt1.1"]/td[2]/span
        # try:
        #     case2 = driver.find_element_by_xpath('//*[@id="ft1.2"]/td[1]/div').text    #  //*[@id="ft1.2"]/td[1]/div
        #     case2_status = driver.find_element_by_xpath('//*[@id="ft1.2"]/td[2]/span/a').text
        # except:
        #     case2 = driver.find_element_by_xpath('//*[@id="pt1.2"]/td[1]/div').text  # //*[@id="ft1.2"]/td[1]/div
        #     case2_status = driver.find_element_by_xpath('//*[@id="pt1.2"]/td[2]/span').text
        execute_detail = [{'case_suit_name': title, 'module': 'buy', 'case_total': case_total, 'case_pass_total': case_pass_total, 'case_pass_rate': (int(case_pass_total))/int(case_total)}]

        '''
        # 转换成时间数组
        timeArray = time.strptime(excute_start_time, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳   ****
        excute_start_time = time.mktime(timeArray)
        print("excute_start_time", excute_start_time)

        # 转换成时间数组
        timeArray = time.strptime(excute_time, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳   ****
        excute_time = time.mktime(timeArray)
        print("excute_time", excute_time)

        excute_end_time = excute_start_time+excute_time
        # 使用time   时间戳转换标准日期格式
        timeArray = time.localtime(excute_end_time)
        excute_end_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print("excute_end_time", excute_end_time)  # 2013--10--10 23:40:00

        # # 使用datetime
        # timeStamp = 1381419600
        # dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
        # otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        # print(otherStyleTime)
        '''

        url = 'http://godeye.hqygou.com/api/receiveAutoTestResult'
        values = ({
            "project_id": 10300,  # Jira上的项目ID
            "project_name": "Payment",  # Jira上的项目项目
            "platform": "PC",
            "level": "Core",
            "case_total": case_total,
            "case_pass_total": case_pass_total,
            "case_pass_rate": (int(case_pass_total))/int(case_total)*100,
            "execute_detail": execute_detail,
            "execute_env": "RegressionTest",
            "execute_scene": "BaselineRelease",
            "execute_type": "CI",
            "autotest_type": "UI",
            "autotest_source": "sTest",
            "excute_start_time": excute_start_time,
            "excute_end_time": str(runner.stopTime),
            "excute_time": excute_time,
            "test_result": "success",
            "execute_result": "success"
        })
        # jdata = json.dumps(values,  cls=DateEncoder).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        jdata = json.dumps(values).encode(encoding='UTF8')  # 对数据进行JSON格式化编码
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type", "application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        print(content)  # 反参
        print(values)  # 请求的参数


    #  代码执行结果获取数据
    def CI_pc_date(self, runner, aa):

        # print("error_count=====>" + str(aa.error_count))
        # print("success_count=====>" + str(aa.success_count))
        # print("result=====>" + str(aa.result))
        success_count = aa.success_count
        error_count = aa.error_count
        failure_count = aa.failure_count
        amount = str(success_count+error_count+failure_count)
        case_pass_rate = round(success_count/(success_count+error_count+failure_count), 1)*100
        # print("=====>" + str(runner.STATUS))
        # print("=====>" + str(runner.startTime))
        # print("=====>" + str(runner.stopTime))
        # print("=====>" + str(runner.description))
        title = runner.title
        print("=====>title" + str(runner.title))
        startTime = runner.startTime
        startTime = str(startTime)
        startTime = startTime[0:19]
        stopTime = runner.stopTime
        stopTime = str(stopTime)
        stopTime = stopTime[0:19]
        execute_detail = [{"case_suit_name": title, "module": "pay", "case_total": str(amount), "case_pass_total": str(case_pass_rate), "case_pass_rate": str(case_pass_rate)}]
        # 转换成时间数组
        timeArray = time.strptime(startTime, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳   ****
        startTime0 = time.mktime(timeArray)
        # print("startTime", startTime0)
        # 转换成时间数组
        timeArray = time.strptime(stopTime, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳   ****
        stopTime0 = time.mktime(timeArray)
        # print("stopTime0", stopTime0)
        excute_time = stopTime0-startTime0
        url = 'http://godeye.hqygou.com/api/receiveAutoTestResult'
        values = ({
                    "api_key": "2b0e740f99f20906a54d04ebe9816d9b",
                    "project_id": 10300,
                    "project_name": "Payment",
                    "platform": "PC",
                    "level": "Core",
                    "case_total": str(amount),
                    "case_pass_total": str(success_count),
                    "case_pass_rate": str(case_pass_rate),
                    "api_total": 0,
                    "api_pass_total": 0,
                    "api_pass_rate": 0,
                    "execute_detail": [{"case_suit_name": title, "module": "pay", "case_total": str(amount), "case_pass_total": str(success_count), "case_pass_rate": str(case_pass_rate)}],
                    "execute_stage": "RegressionTest",
                    "execute_scene": "BaselineRelease",
                    "execute_type": "Normal",
                    "autotest_type": "UI",
                    "autotest_source": "sTest",
                    "excute_start_time": str(startTime),
                    "excute_end_time": str(stopTime),
                    "excute_time": str(excute_time),
                    "test_result": 1,
                    "execute_result": 1
                    })

        values = sorted(values.items(), key=operator.itemgetter(0))  # 按照item中的第一个字符进行排序，即按照key排序
        values = dict(values)  # 变成字典

        sorted_x = "".join('%s' % id for id in list(values.values())) + 'sTest123!@#'  # 列表变成纯字符串
        sorted_x = sorted_x.replace("\'", "\"")
        sorted_x1 = sorted_x[0:86]
        sorted_x2 = sorted_x[86:]
        sorted_x2 = sorted_x2.replace(" ", "")
        sorted_x = sorted_x1 + sorted_x2
        # print('排序后value值:', sorted_x)
        md5 = hashlib.md5(sorted_x.encode(encoding='UTF-8')).hexdigest()
        print('md5', md5)
        values['api_sign'] = md5

        jdata = json.dumps(values).encode(encoding='UTF-8')  # 对数据进行JSON格式化编码
        print("入参", jdata)  # 请求的参数
        req = urllib.request.Request(url, jdata)  # 生成页面请求的完整数据
        req.add_header("Content-Type", "application/json")
        response = urllib.request.urlopen(req)  # 发送页面请求
        content = response.read()
        print("反参", content)  # 反参


if __name__ == "__main__":
    GBConnect().CI_pc_page()
    GBConnect().CI_pc_date()


