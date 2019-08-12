'''
@Description:
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-08-07 00:00:53
@LastEditors: liuhua
@LastEditTime: 2019-08-12 10:10:42
'''

import sys
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class login_gb(unittest.TestCase):
    def setUp(self):
        self.start = time.clock()
        self.profile_directory = "C:\\Users\\liuhua2\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\p18j8opt.default"
        self.profile = webdriver.FirefoxProfile(self.profile_directory)
        self.path = r"D:\Program Files\python\Scripts\geckodriver.exe"
        self.driver = webdriver.Firefox(firefox_profile=self.profile,
                                        executable_path=self.path)
        # self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_gb(self):
        self.driver.get("https://login.gearbest.net/m-users-a-sign.htm?type=1")
        time.sleep(3)
        # 登录
        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_id('email')).send_keys('lh100@qq.com')
        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_id('password')).send_keys('aaaa1234')
        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_id('js-btnSubmit')).click()

        # 收藏页添加物品至购物车
        time.sleep(1)
        above = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
            '//*[@id="ucenter_content"]/div/div/ul/li[1]/a/img'))
        ActionChains(self.driver).move_to_element(above).perform()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            '//*[@id="ucenter_content"]/div/div/ul/li[1]/a/div/span[1]/i')).click()
        time.sleep(2)

        # 点击购物车
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(
            "//div[@id='js-labelHeadCart']/a/span[2]")).click()

        # 点击跳转订单确认页
        time.sleep(4)

        # WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
        #    "div.cart_checkoutBtnBox>a.btn.middle.strong.proceed_checkout")).click()
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_css_selector(
            "div.cart_checkoutBtnBox>a.btn.middle.strong.proceed_checkout")).send_keys(Keys.ENTER)

        time.sleep(1)
        # 点击编辑地址
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_css_selector(
            "div.ckSa_editAddressBtn>a.btn.middle.strong")).click()

        # 编辑地址信息
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='firstName'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='firstName'][class='address_input']")).send_keys("firstname")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='lastName'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='lastName'][class='address_input']")).send_keys("lastname")

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='email'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='email'][class='address_input']")).send_keys("lh100@qq.com")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='postalCode'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='postalCode'][class='address_input']")).send_keys("13165-000")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='addressLine1'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='addressLine1'][class='address_input']")).send_keys("addressline1")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='addressLine2'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='addressLine2'][class='address_input']")).send_keys("addressline2")

       # 点击编辑国家下拉框
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[7]/div[1]/div/p/i")).click()

        # 编辑国家
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[7]/div[1]/div/div/ul/li[45]")).click()

        # 点击编辑州省下拉框
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[8]/div[1]/div/p/i")).click()

        # 编辑州省
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[8]/div[1]/div/div/ul/li[1]")).click()

        # 点击编辑城市下拉框
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[9]/div[1]/div/p/i")).click()

        # 编辑城市
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[9]/div[1]/div/div/ul/li[1]")).click()

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='nationalIdNumber'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='nationalIdNumber'][class='address_input']")).send_keys("1591579971")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='middleName'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='middleName'][class='address_input']")).send_keys("zgaoyans")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='taxNumber'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='taxNumber'][class='address_input']")).send_keys("12321312")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='passportNo'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='passportNo'][class='address_input']")).send_keys("qwedsadas")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='passportSerial'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='passportSerial'][class='address_input']")).send_keys("asdsadasd")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='passportIssueDate'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='passportIssueDate'][class='address_input']")).send_keys("12/12/2019")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='issuingAgency'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='issuingAgency'][class='address_input']")).send_keys("1234")

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='birthDay'][class='address_input']")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "div.address_data>input[name='birthDay'][class='address_input']")).send_keys("2016-05-22")

        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/form/div[19]/a[2]")).click()

        time.sleep(3)
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/div[3]/a[1]")).click()

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div[3]/div[2]/a")).click()

        # 注意写法 class属性注意
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_css_selector(
            "span[class='compCheckbox_shape checked'][paychannel='PAYPAL']>i.compCheckbox_check")).click()

        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_css_selector(
            "div.pc_order_total>i.placeOrder.btn.block.toPayBtn")).click()

        self.driver.switch_to.frame(WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_css_selector("iframe[name='injectedUl']")))

        WebDriverWait(self.driver, 8).until(
            lambda x: x.find_element_by_css_selector("input#email")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "input#email")).send_keys("liuhua2@globalegrow.com")

        WebDriverWait(self.driver, 8).until(
            lambda x: x.find_element_by_css_selector("input#password")).clear()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_css_selector(
            "input#password")).send_keys("aaaa1234")

        WebDriverWait(self.driver, 8).until(
            lambda x: x.find_element_by_css_selector("button#btnLogin")).click()
        self.driver.switch_to_default_content()

        time.sleep(0.5)
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_id(
            "confirmButtonTop"))
        time.sleep(10)
        WebDriverWait(self.driver, 15).until(
            lambda x: x.find_element_by_id("confirmButtonTop")).click()

        WebDriverWait(self.driver, 25).until(lambda x: x.find_element_by_xpath(
            "//*[@id='siteWrap']/div/div/div/div/div/a"))
        if EC.title_is(u'Gearbest: Affordable Quality, Fun Shopping'):
            print('支付成功')
        self.end = time.clock()
        print(self.end - self.start)


if __name__ == '__main__':
    unittest.main()
