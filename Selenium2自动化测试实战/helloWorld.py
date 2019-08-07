#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-08 16:30:00
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$
import sys
import os
import selenium
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import HTMLTestRunner
from selenium.webdriver.support.select import Select
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from email import encoders
from email.mime.base import MIMEBase
from selenium.webdriver.common.keys import Keys

# class login_gb(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(2)
#         self.driver.get("https://login.gearbest.net/m-users-a-sign.htm?type=1")

#     def tearDown(self):
#         self.driver.quit()

#     def test_login_gb(self):
#         self.driver.find_element_by_id('email').send_keys('lh100@qq.com')
#         self.driver.find_element_by_id('password').send_keys('aaaa1234')
#         time.sleep(2)
#         self.driver.find_element_by_id('js-btnSubmit').click()
#         try:
#             assert 'GearBest' in self.driver.title
#             print('Test login pass')
#         except Exception as e:

#             print('Test login fail', format(e))

#         self.driver.implicitly_wait(5)
# above = self.driver.find_element_by_xpath(
#     '/html/body/div[4]/div[1]/div/section[1]/div/div/ul/li[1]/a/div/span[1]/i')
# time.sleep(2)
# ActionChains(self.driver).move_to_element(above).perform()
#             print('Test Fail', format(e))


class login_gb(unittest.TestCase):

    def setUp(self):
        self.start = time.clock()
        self.profile_directory = "C:\\Users\\liuhua2\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\p18j8opt.default"
        self.profile = webdriver.FirefoxProfile(self.profile_directory)
        self.path = r"D:\Program Files\python\Scripts\geckodriver.exe"
        self.driver = webdriver.Firefox(
            firefox_profile=self.profile, executable_path=self.path)
        # self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_login_gb(self):
        self.driver.get("https://login.gearbest.net/m-users-a-sign.htm?type=1")
        time.sleep(1)
        self.driver.find_element_by_id('email').send_keys('lh100@qq.com')
        self.driver.find_element_by_id('password').send_keys('aaaa1234')
        self.driver.find_element_by_id('js-btnSubmit').click()
        # self.driver.implicitly_wait(4)  # 等待页面加载
        time.sleep(8)
        try:
            if 'Gearbest' in self.driver.title:
                print('Login success')
        except Exception as e:
            print('Login fail')
            raise e
        above = self.driver.find_element_by_xpath(
            '//*[@id="ucenter_content"]/div/div/ul/li[1]/a/img')
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath(
            '//*[@id="ucenter_content"]/div/div/ul/li[1]/a/div/span[1]/i').click()

        time.sleep(3)
        self.driver.find_element_by_xpath(
            "//div[@id='js-labelHeadCart']/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector(
            "div.cart_checkoutBtnBox>a.btn.middle.strong.proceed_checkout").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "div.ckSa_editAddressBtn>a.btn.middle.strong").click()
        time.sleep(3)

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='firstName'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='firstName'][class='address_input']").send_keys("firstname")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='lastName'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='lastName'][class='address_input']").send_keys("lastname")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='email'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='email'][class='address_input']").send_keys("lh100@qq.com")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='postalCode'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='postalCode'][class='address_input']").send_keys("13165-000")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='addressLine1'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='addressLine1'][class='address_input']").send_keys("addressline1")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='addressLine2'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='addressLine2'][class='address_input']").send_keys("addressline2")

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[7]/div[1]/div/p/i").click()
        time.sleep(2)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[7]/div[1]/div/div/ul/li[45]").click()
        time.sleep(2)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[8]/div[1]/div/p/i").click()
        time.sleep(2)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[8]/div[1]/div/div/ul/li[1]").click()
        time.sleep(2)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[9]/div[1]/div/p/i").click()
        time.sleep(2)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[9]/div[1]/div/div/ul/li[1]").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='nationalIdNumber'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='nationalIdNumber'][class='address_input']").send_keys("1591579971")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='middleName'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='middleName'][class='address_input']").send_keys("zgaoyans")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='taxNumber'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='taxNumber'][class='address_input']").send_keys("12321312")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='passportNo'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='passportNo'][class='address_input']").send_keys("qwedsadas")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='passportSerial'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='passportSerial'][class='address_input']").send_keys("asdsadasd")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='passportIssueDate'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='passportIssueDate'][class='address_input']").send_keys("12/12/2019")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='issuingAgency'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='issuingAgency'][class='address_input']").send_keys("1234")

        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='birthDay'][class='address_input']").clear()
        self.driver.find_element_by_css_selector(
            "div.address_data>input[name='birthDay'][class='address_input']").send_keys("2016-05-22")
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[19]/a[2]").click()

        time.sleep(1)

        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/div[3]/a[1]").click()
        time.sleep(4)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div[3]/div[2]/a").click()

        time.sleep(10)
        self.driver.find_element_by_css_selector(
            "span[class='compCheckbox_shape checked'][paychannel='PAYPAL']>i.compCheckbox_check").click()
        self.driver.find_element_by_css_selector(
            "div.pc_order_total>i.placeOrder.btn.block.toPayBtn").click()

        time.sleep(20)

        #
        self.driver.switch_to.frame(
            self.driver.find_element_by_css_selector("iframe[name='injectedUl']"))

        self.driver.find_element_by_css_selector("input#email").clear()
        self.driver.find_element_by_css_selector(
            "input#email").send_keys("liuhua2@globalegrow.com")

        self.driver.find_element_by_css_selector(
            "input#password").clear()
        self.driver.find_element_by_css_selector(
            "input#password").send_keys("aaaa1234")
        self.driver.find_element_by_css_selector("button#btnLogin").click()

        time.sleep(15)
        # self.driver.implicitly_wait(15)
        self.driver.switch_to_default_content()

        # 先点击父元素
        self.driver.find_element_by_id("button").click()
        self.driver.find_element_by_id("confirmButtonTop").click()

        # 需要js点击，不然无法点击
        # paypal_paynow_js = "document.getElementById('confirmButtonTop').click()"
        # self.driver.execute_script(paypal_paynow_js)

        time.sleep(15)
        try:
            if 'Gearbest' in self.driver.title:
                print('pay success')
        except Exception as e:
            print('pay fail')
            raise e
        # 弹窗无法截取
        # self.driver.get_screenshot_as_file(
        #     r"C:\Users\liuhua2\Desktop\testcase\pay.png")
        # self.imgs.append(self.driver.get_screenshot_as_base64())
        self.end = time.clock()
        print(self.end - self.start)
    # def test_baidu(self):
    #     url = 'https://www.baidu.com'
    #     self.driver.get(url)
    #     self.driver.implicitly_wait(5)
    #     self.driver.get_screenshot_as_file(
    #         r"C:\Users\liuhua2\Desktop\testcase\baidu.png")
    #     # self.imgs.append(self.driver.get_screenshot_as_base64())
    #     mouse = self.driver.find_element_by_xpath("//div[@id='u1']/a[8]")
    #     ActionChains(self.driver).move_to_element(mouse).perform()
    #     time.sleep(2)
    #     # driver.find_element_by_link_text(
    #     #    "搜索设置").click()
    #     self.driver.find_element_by_xpath(
    #         "/html/body/div[1]/div[6]/a[1]").click()
    #     time.sleep(0.5)
    #     s = self.driver.find_element_by_id("nr")
    #     # s.find_elements_by_xpath("//*[@id='nr']/option[2]").click() 无点击
    #     # Select(s).select_by_value("20")
    #     Select(s).select_by_visible_text("每页显示50条")
    #     # self.imgs.append(self.driver.get_screenshot_as_base64())
    #     self.driver.find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()
    #     # self.imgs.append(self.driver.get_screenshot_as_base64())
    #     time.sleep(0.5)

    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #     t = self.driver.switch_to_alert()
    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #     t.accept()
    #     time.sleep(0.5)
    #     self.imgs.append(self.driver.get_screenshot_as_base64())

    # def test_baidu_new(self):
    #     url = 'https://www.baidu.com'
    #     self.driver.get(url)
    #     self.driver.implicitly_wait(5)
    #     self.driver.get_screenshot_as_file(
    #         r"C:\Users\liuhua2\Desktop\testcase\baidu.png")
    #     # self.imgs.append(self.driver.get_screenshot_as_base64())
    #     mouse = self.driver.find_element_by_xpath("//div[@id='u1']/a[8]")
    #     ActionChains(self.driver).move_to_element(mouse).perform()
    #     time.sleep(2)
    #     # driver.find_element_by_link_text(
    #     #    "搜索设置").click()
    #     self.driver.find_element_by_xpath(
    #         "/html/body/div[1]/div[6]/a[1]").click()
    #     time.sleep(0.5)
    #     s = self.driver.find_element_by_id("nr")
    #     # s.find_elements_by_xpath("//*[@id='nr']/option[2]").click() 无点击
    #     # Select(s).select_by_value("20")
    #     Select(s).select_by_visible_text("每页显示50条")
    #     # self.imgs.append(self.driver.get_screenshot_as_base64())
    #     self.driver.find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()
    #     # self.imgs.append(self.driver.get_screenshot_as_base64())
    #     time.sleep(0.5)

    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #     t = self.driver.switch_to_alert()
    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #     t.accept()
    #     time.sleep(0.5)
    #     self.imgs.append(self.driver.get_screenshot_as_base64())


def all_case():
    case_dir = r"F:\Src\LearningPython\Selenium2自动化测试实战"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        case_dir, pattern='hello*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTest(test_case)
    print(testcase)
    return(testcase)


def send_email(file_new):

    subject = '自动化测试报告'

    # sender = 'choly1985@163.com'
    # #receiver = '958905266@qq.com'
    # receiver = 'liuhua2@globalegrow.com'

    sender = 'liuhua2@globalegrow.com'
    receiver = 'liuhua2@globalegrow.com'

    msgRoot = MIMEMultipart('related')
    msgRoot['from'] = sender
    msgRoot['to'] = receiver
    msgRoot['subject'] = subject

    text_content = 'Python自动化测试报告'
    msg_text = MIMEText(text_content, _charset='utf-8')
    msgRoot.attach(msg_text)

    # 成功的代码别动
    part = MIMEBase('application', "text/html")
    part.set_payload(open(file_new, "rb").read())
    encoders.encode_base64(part)
    # filename 不要省略了文件名的后缀 否则会变成乱码 eg.:ATT00002.bin
    part.add_header('Content-Disposition', 'attachment',
                    filename=('Report-' + time.strftime('%Y%m%d-%H%M%S') + ".html"))
    msgRoot.attach(part)

    try:

        # 非SSL邮件发送
        # smtp = smtplib.SMTP()
        # smtp.connect("smtp.163.com", port=25)
        # smtp.login("choly1985@163.com", 'xlab0628')

        # ssl 邮件发送
        smtp = smtplib.SMTP_SSL('newmailf.globalegrow.com', port=465)
        smtp.connect('newmailf.globalegrow.com', port=465)
        smtp.login('liuhua2@globalegrow.com', 'JcXrsP3HXWGiTrYr')

        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()
        print('邮件发送成功')

    # 非ssl异常
    # except smtp.SMPTException as e:
    #     print(e)
    #      print('邮件发送失败')

    # ssl下异常
    except smtplib.SMTPAuthenticationError as e:
        print(e)
        print('邮件发送失败')


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + r"\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new


if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # report_path = r"C:\Users\liuhua2\Desktop\report.html"
    # fp = open(report_path, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp, title='自动化测试报告', description='用例执行情况：')
    # runner.run(all_case())
    # fp.close()

    # test_report = r'C:\Users\Administrator\Desktop'
    # new_report1 = new_report(test_report)
    # send_email(r'C:\Users\liuhua2\Desktop\report.html')
    unittest.main()
    print(123, end=' ')
