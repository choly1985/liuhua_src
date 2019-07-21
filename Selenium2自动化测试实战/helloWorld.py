#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-08 16:30:00
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
import selenium
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# class BaiduSearch(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(1)
#         self.driver.get("https://www.baidu.com")

#     def tearDown(self):

#         self.driver.quit()

#     def test_baidu_search(self):
#         self.driver.find_element_by_id('kw').send_keys('war3')
#         self.driver.find_element_by_id('su').click()
#         time.sleep(3)
#         try:
#             assert 'war3' in self.driver.title
#             print('Test Pass')
#         except Exception as e:
#             print('Test Fail', format(e))


class login_gb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.get("https://login.gearbest.net/m-users-a-sign.htm?type=1")

    def tearDown(self):
        self.driver.quit()

    def test_login_gb(self):
        self.driver.find_element_by_id('email').send_keys('lh100@qq.com')
        self.driver.find_element_by_id('password').send_keys('aaaa1234')
        time.sleep(2)
        self.driver.find_element_by_id('js-btnSubmit').click()
        try:
            assert 'GearBest' in self.driver.title
            print('Test login pass')
        except Exception as e:
            print('Test login fail', format(e))

        self.driver.implicitly_wait(5)
        above = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/div/section[1]/div/div/ul/li[1]/a/div/span[1]/i')
        time.sleep(2)
        ActionChains(self.driver).move_to_element(above).perform()


if __name__ == '__main__':
    unittest.main()
