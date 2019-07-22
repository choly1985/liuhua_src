from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from UI_AUTOMATION.utils.config import Config
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import  pymysql
import random
import string

from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("http://www.obs-pay.com")
# js = 'window.open("http://www.obs-pay.com");'  # 通过执行js，开启一个新的窗口
# driver.execute_script(js)
# window_1 = driver.current_window_handle
# # 获得打开的所有的窗口句柄
# windows = driver.window_handles
# # 切换到最新的窗口
# for current_window in windows:
#     if current_window != window_1:
#         driver.switch_to.window(current_window)
sleep(1.5)
driver.find_element_by_xpath("//*[@name='username']").send_keys("zhangwei")
driver.find_element_by_xpath("//*[@name='password']").send_keys("zhang1wei")
sleep(0.5)

driver.find_element_by_xpath("//input[@type='submit']").click()
sleep(1)
driver.get("http://www.obs-pay.com/#/pay/channel-platform-country/list")


# driver.maximize_window()
sleep(1)

driver.find_element_by_xpath("//*[contains(text(),'Turkey')]/../../td[5]/div/button[1]/span").click()
sleep(1)


# # 起点
# start = driver.find_element_by_xpath("//*[contains(text(),'checkout_credit')]")
# # 终点
# end = driver.find_element_by_xpath("//*[contains(text(),'checkout_credit')]/../li[1]")


# 起点
start = driver.find_element_by_xpath("//*[text()='checkout_credit']")
# 终点
end = driver.find_element_by_xpath("//*[text()='checkout_credit']/../li[1]")

sleep(0.5)
ActionChains(driver).drag_and_drop(start, end).perform()

# actions = ActionChains(driver)
# actions.drag_and_drop(start, end)
# # 执行
# actions.perform()
sleep(0.5)
# driver.find_element_by_xpath("//*[contains(text(),'确定')]").click()

#content-side > div:nth-child(2) > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div > ul > span > li:nth-child(4)











