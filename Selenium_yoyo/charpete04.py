'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-08-10 15:57:46
@LastEditors: liuhua
@LastEditTime: 2019-08-10 18:36:11
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com")

# WebDriverWait(driver, 10).until(
#     lambda x: x.find_element_by_id("kw")).send_keys('liuhua')

# is_disappeared = WebDriverWait(driver, 10, 1).until_not(
#     lambda x: x.find_element_by_id('kw').is_displayed())
# print(is_disappeared)

# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

# driver.find_element("id", "kw").send_keys("yoyoketang")
# driver.find_element("css selector", '#su').click()

# print(driver.find_element('link text', '学术').text)
# print(driver.find_element('name', 'tj_trnews').text)
# print(driver.find_element('class name', 'bri').text)


# class Bolg(unittest.TestCase):
#     '''
#     @description: 登录博客
#     @param {null}
#     @return: null
#     @author: liuhua
#     '''

#     def setUp(self):
#         url = 'https://passport.cnblogs.com/user/signin'
#         self.driver = webdriver.Firefox()
#         self.driver.get(url)
#         time.sleep(3)

#     def login(self, username, psw):
#         '''
#         @description: 登录方法，账号和密码参数化
#         @param {None}
#         @return: None
#         @author: liuhua
#         '''
#         self.driver.find_element_by_id("LoginName").send_keys(username)
#         self.driver.find_element_by_id("Password").send_keys(psw)
#         self.driver.find_element_by_class_name('ladda-label').click()
#         time.sleep(4)

#     def is_login_sucess(self):
#         '''
#         @description: 判断用户是否获取到登录账户名称
#         @param {type} param
#         @return: bool
#         @author: liuhua
#         '''
#         try:
#             text = self.driver.find_element_by_id("lnk_current_user").text
#             print(text)
#             return True
#         except:
#             return False

#     def test_01(self):
#         '''
#         @description: 登录案例：账号，密码自己设置
#         @param {param}
#         @return: None
#         @author: liuhua
#         '''
#         self.login(u"choly1985", u"#xiaosj1955")
#         time.sleep(2)
#         text = self.driver.find_element_by_id("lnk_current_user").text
#         self.assertEqual(text, u"Real_xb", msg='error不相等')
#         self.assertNotEqual(text, u'Real_xb', msg='error相等')

#     def tearDown(self):
#         self.driver.quit()


l = ['a', 'b', 'c']
i = l.index('a')
j = l.index('c')
l[i], l[j] = l[j], l[i]
print(l)
# if __name__ == '__main__':
# unittest.main()
