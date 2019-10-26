'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-07-29 18:43:08
@LastEditors: liuhua
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-27 15:48:19
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Firefox()
# # driver=webdriver.Chrome()
# driver.maximize_window()
#driver.set_window_size(540, 960)


# 2.1操作浏览器基本方法
# driver.get('https://www.baidu.com')
# driver.refresh()
# time.sleep(3)
# driver.get_screenshot_as_file(
#     "C:\\Users\\Administrator\\Desktop\\Seleium\\Gif\\baidu.png")

# driver.get('http://www.hordehome.com')
# time.sleep(5)
# driver.get_screenshot_as_file(
#     "C:\\Users\\Administrator\\Desktop\\Seleium\\Gif\\hordehome.png")

# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.close()
# driver.quit()

# 2.2常用的8中元素定位
# <input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd">


# driver.get('https://www.baidu.com')

# time.sleep(3)

# driver.find_element_by_id('kw').send_keys('python')

# driver.find_element_by_name('wd').send_keys('python')

# driver.find_element_by_class_name('s_ipt').send_keys('python')

# driver.find_element_by_tag_name('input').send_keys('python')

# driver.find_element_by_link_text('hao123').click()

# driver.find_element_by_link_text('新闻').click()

# driver.find_element_by_partial_link_text('ao123').click()

# driver.find_element_by_xpath(".//input[@id='kw']").send_keys('python')
# driver.find_element_by_xpath("//*[@id='from']/*[@id='s_kw_wrap']") span标签

# driver.find_element_by_css_selector('#kw').send_keys('python')
# driver.find_element_by_css_selector('.s_ipt').send_keys('python')
# driver.find_element_by_css_selector("[type='submit']")
# driver.find_element_by_css_selector(
#     "form.fm>span>input.s_ipt").send_keys('python')
# driver.find_element_by_css_selector(
#    'form.fm>span>input#kw').send_keys('python')

# 2.3 xpath定位

# driver.find_elements_by_xpath("//*[@id='kw']")
# driver.find_elements_by_xpath("//*[@name='wd']")
# driver.find_element_by_xpath("//*[@class='s_ipt']")
# driver.find_element_by_xpath("//input[@id='kw']").send_keys('python')
# driver.find_element_by_xpath("//*[@autocomplete='off']").send_keys('python')
# driver.find_element_by_xpath("//span[@id='s_kw_wrap']") ???
# driver.find_element_by_xpath(
#    "//form[@id='form']/span[1]/input").send_keys('python')
#driver.find_element_by_xpath("//*[@id='kw'and @autocomplete='off']").send_keys('python')

# driver.find_element_by_xpath("//*[contains(text(),'hao123')]")
# driver.find_element_by_xpath("//*[contains(@id,'kw')]")
# driver.find_element_by_xpath("//*[starts_with('@id','s_kw_')]") XXX
# driver.find_elements_by_xpath("//*[ends-with('@id','kw_wrap')]")XXX
# driver.find_element_by_xpath("//*[match(text(),'hao123')]")XXX

# driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys('python')

# 2.6 操作元素（键盘和鼠标事件）

# driver.get("http://www.testerhorde.com")
# driver.implicitly_wait(10)
# driver.find_element_by_id("search-button").click()
# driver.find_element_by_id("search-term").clear()
# driver.find_element_by_id("search-term").send_keys('selenium')


# driver.get('https://www.baidu.com')
# driver.implicitly_wait(2)
# driver.find_element_by_id('kw').send_keys(u"测试部落")
# driver.find_element_by_id("kw").submit()

# driver.get("http://www.testerhorde.com")
# driver.implicitly_wait(10)
# driver.find_element_by_id("search-button").click()
# driver.find_element_by_id("search-term").clear()
# driver.find_element_by_id("search-term").send_keys('selenium')
# time.sleep(1)
# driver.find_element_by_id("search-term").send_keys(Keys.ENTER)

# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get('http://www.baidu.com/')
# driver.implicitly_wait(5)
# mouse = driver.find_element_by_xpath("//div[@id='u1']/a[8][text()='设置']")
# mouse = driver.find_element_by_xpath("//div[@id='u1']/a[8]")
# print(mouse)
# ActionChains(driver).move_to_element(mouse).perform()
# ActionChains(driver).double_click(mouse).perform()
# ActionChains(driver).context_click(mouse).perform()
# tar = driver.find_element_by_xpath("//div[@id='u1']/a[1]")
# ActionChains(driver).drag_and_drop(mouse, tar).perform()

# 2.7多窗口/句柄
# h = driver.current_window_handle
# print(h)
# s = driver.find_elements_by_css_selector('.tab>a')
# s[0].click() XX
# driver.find_element_by_id('app_tooltip').click()
# driver.implicitly_wait(1)
# all_h = driver.window_handles
# print(all_h)
# for i in all_h:
#     if i != h:
#         driver.switch_to_window(i)
#         time.sleep(1)
#         print(driver.title)
#         if u'百度新闻客户端—新鲜海量资讯' in driver.title:
#             print('页面打开正常')
#             driver.close()
#         else:
#             print('页面打开失败')
# time.sleep(3)
# driver.switch_to_window(h)
# driver.close()

# driver.get('http://sz.ganji.com/')
# driver.implicitly_wait(6)
# h = driver.current_window_handle
# s = driver.find_elements_by_css_selector(".dt-t")
# r = ['深圳招聘网', '深圳房产网', '深圳二手网', '深圳二手汽车网', '深圳宠物网', '深圳黄页大全', '深圳黄页大全']
# for a, b in zip(s, r):
#     a.click()
#     text = a.text
#     time.sleep(5)
#     all_h = driver.window_handles
#     for i in all_h:
#         if i != h:
#             driver.switch_to_window(i)
#             time.sleep(5)
#             print(driver.title)
#             if b in driver.title:
#                 print(text + "页面打开正常")
#             else:
#                 print(text + "页面打开失败")
#     driver.close()
#     driver.switch_to_window(h)
#     time.sleep(5)
# driver.quit()

# 2.8 定位一组元素find_elements


# driver.get("https://www.baidu.com")
# driver.implicitly_wait(2)
# driver.find_element_by_id('kw').send_keys('测试部落')
# driver.find_element_by_id('kw').submit()
# driver.implicitly_wait(2)
# s = driver.find_elements_by_css_selector('h3.t > a')
# for i in s:
#     print(i.get_attribute("href"))
# t = random.randint(0, 9)
# a = s[t].get_attribute("href")
# print(a, t)
# driver.get(a)
# s[t].click()
# time.sleep(3)

# 2.9 切换frame
# driver.get("https://mail.163.com/")
# driver.implicitly_wait(5)
# # driver.find_element_by_xpath("//a[@id='switchAccountLogin']").click()
# driver.find_element_by_css_selector(
#     "#lbNormal").click()
# time.sleep(1)
# iframe = driver.find_element_by_tag_name('iframe')
# driver.switch_to_frame(iframe)
# driver.find_element_by_name('email').send_keys('choly1985')
# driver.find_element_by_name('password').send_keys('xiaosj1955')
# time.sleep(1)
# driver.switch_to.default_content()

# 2.10 Select下拉框

from selenium.webdriver.support.select import Select
# driver = webdriver.Firefox()
# time.sleep(2)
# driver.maximize_window()
# url = 'https://www.baidu.com'
# driver.get(url)
# driver.implicitly_wait(5)
# mouse = driver.find_element_by_xpath("//div[@id='u1']/a[8]")
# ActionChains(driver).move_to_element(mouse).perform()
# time.sleep(1)
# # driver.find_element_by_link_text(
# #    "搜索设置").click()
# driver.find_element_by_xpath("/html/body/div[1]/div[6]/a[1]").click()
# s = driver.find_element_by_id("nr")
# # s.find_elements_by_xpath("//*[@id='nr']/option[2]").click() 无点击
# # Select(s).select_by_value("20")
# Select(s).select_by_visible_text("每页显示50条")
# driver.find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()
# time.sleep(0.5)
# t = driver.switch_to_alert()
# print(t.text)
# t.accept()
# time.sleep(0.5)
# driver.quit()

# 2.11  alert\confirm\prompt
# driver = webdriver.Firefox()
# time.sleep(2)
# driver.maximize_window()
# url = 'file:///C:/Users/Administrator/Desktop/Seleium/Html/alert.html'
# driver.get(url)
# time.sleep(1)
# driver.find_element_by_id('alert').click()
# time.sleep(1)
# t = driver.switch_to_alert()
# print(t.text)
# # t.accept()
# t.dismiss()

# driver.find_element_by_id("confirm").click()
# time.sleep(1)
# t = driver.switch_to_alert()
# print(t.text)
# t.accept()
# #t.dismiss()
# time.sleep(2)
# driver.quit()

# driver.find_element_by_id("prompt").click()
# time.sleep(1)
# t = driver.switch_to_alert()
# print(t.text)
# t.send_keys('liuhua')
# t.accept()
# # t.dismiss()
# time.sleep(2)
# driver.quit()

# 2.12  单选和复选
# driver = webdriver.Firefox()
# time.sleep(2)
# driver.maximize_window()
# url = 'file:///C:/Users/Administrator/Desktop/Seleium/Html/radio.html'
# driver.get(url)
# time.sleep(1)
# print(driver.find_element_by_id('boy').is_selected())
# driver.find_element_by_id('boy').click()
# print(driver.find_element_by_id('boy').is_selected())

# driver.find_element_by_id('c1').click()
# c_python = driver.find_elements_by_css_selector("input[type='checkbox']")
# c_python = driver.find_elements_by_xpath("//input[@type='checkbox']")
# for i in c_python:
#     i.click()
#     print(i.is_selected())
# time.sleep(1)
# driver.quit()

# 2.13 table定位

# driver = webdriver.Firefox()
# time.sleep(2)
# driver.maximize_window()

# url = 'file:///C:/Users/Administrator/Desktop/Seleium/Html/tab.html'
# driver.get(url)
# time.sleep(1)
# t = driver.find_element_by_xpath("//table[@id='myTable']/tbody/tr[3]/td[1]")
# print(t.text)

# time.sleep(1)
# driver.quit()

# 2.14 加载firefox配置
# profile_directory=r''
# profile=webdriver.FirefoxProfile(profile_directory)
# driver.Firefox(profile)

# 2.15富文本

# 2.16 文件上传 send_keys

# 2.17 获取元素属性

# driver = webdriver.Firefox()
# time.sleep(2)
# driver.maximize_window()
# driver.get("https://www.baidu.com")
# time.sleep(2)
# name = driver.find_element_by_id('kw').get_attribute("class")
# driver.find_element_by_id('kw').send_keys('liuhua')
# value = driver.find_element_by_id('kw').get_attribute("value")
# print(name, driver.name, value)
# driver.quit()

# 2.18 爬取页面源码

# 2.19 cookie相关操作

# 2.21 Js处理滚动条

# driver = webdriver.Firefox()
# time.sleep(2)
# driver.maximize_window()
# url = 'file:///C:/Users/Administrator/Desktop/Seleium/Html/js.html'
# driver.get(url)
# time.sleep(1)

# js1 = "document.getElementById('yoyoketang').scrollTop=10000"
# driver.execute_script(js1)

# time.sleep(3)

# js2 = "document.getElementById('yoyoketang').scrollTop=0"
# driver.execute_script(js2)
# time.sleep(3)

# js3 = "document.getElementById('yoyoketang').scrollLeft=10000"
# driver.execute_script(js3)
# time.sleep(3)

# js4 = "document.getElementById('yoyoketang').scrollLeft=0"
# driver.execute_script(js4)
# time.sleep(3)

# js5 = "document.getElementsByClassName('scroll')[0].scrollTop=10000"
# driver.execute_script(js5)
# time.sleep(2)

# js6 = "document.getElementsByClassName('scroll')[0].scrollLeft=10000"
# driver.execute_script(js6)
# time.sleep(2)

# driver.quit()

print('hello world!!!!!!!!!!!!!!!123123!')
print(12345)
print(123123)
