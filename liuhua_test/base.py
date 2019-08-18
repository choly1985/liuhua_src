'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-08-10 14:16:06
@LastEditors: liuhua
'''

# import xlrd

# excel 操作方法如下
# 打开excel表格，参数文件路径
# data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\Seleium\test.xlsx')
# table = data.sheets()[0] #通过索引顺序获取
# table = data.sheet_by_index(0) #通过索引顺序获取
# table = data.sheet_by_name('Sheet1')  # 通过名称获取
# nrows = table.nrows  # 总行数
# ncols = table.ncols  # 总列数
# print(nrows, ncols)
# print(table.row_values(0), table.row_values(1),
#       table.row_values(2), table.row_values(3))  # 打印每一行
# print(table.col_values(0), table.col_values(1))  # 打印每一列
# print(table.row_values, table.col_values)

# 封装后代码如下


# class excel_data():
#     '''
#     @description: 读取excle数据
#     @param {type} param
#     @return: None
#     @author: liuhua
#     '''

#     def __init__(self, excelPath, sheetName):
#         self.data = xlrd.open_workbook(excelPath)
#         self.table = self.data.sheet_by_name(sheetName)

#         # 获取第一行作为key值
#         self.keys = self.table.row_values(0)
#         # 获取总行数
#         self.rowNum = self.table.nrows
#         # 获取总列数
#         self.colNum = self.table.ncols

#     def dict_data(self):
#         if self.rowNum <= 1:
#             print("总行数小于1")
#         else:
#             r = []
#             j = 1
#             for i in range(self.rowNum - 1):
#                 s = {}
#                 # 从第二行获取对应的values值
#                 values = self.table.row_values(j)
#                 for x in range(self.colNum):
#                     s[self.keys[x]] = values[x]
#                 r.append(s)
#                 j += 1
#             return r
# if __name__ == "__main__":
#     filePath = r'C:\Users\Administrator\Desktop\Seleium\test.xlsx'
#     sheetName = 'Sheet1'
# excel中数据需要设置单元格为文本格式，然后编辑数据，成功后有个小三角表示，不然读取数据是浮点数
#     data = excel_data(filePath, sheetName)
#     print(data.dict_data())


# import ddt
# import unittest

# # 测试数据
# testData = [{"username": "python", "password": "123456"}, {
#     'username': 'selenium', 'password': '123123'}, {'username': 'java', 'password': '121212'}]


# @ddt.ddt
# class Test(unittest.TestCase):
#     def setUp(self):
#         print("start")

#     def tearDown(self):
#         print('end!')

#     @ddt.data(*testData)
#     def test_ddt(self, data):
#         print(data)

# if __name__ == "__main__":
#     unittest.main()


# 模拟手机浏览器操作
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
# import time

# 谷歌手机浏览器手机设置，设计手机型号
# mobile_emulation = {'deviceName': 'iPhone X'}
# options = webdriver.ChromeOptions()
# options.add_experimental_option("mobileEmulation", mobile_emulation)
# driver = webdriver.Chrome(chrome_options=options)
# driver.get("http://m.baidu.com")
# time.sleep(100)
# driver.quit()

# 谷歌手机浏览器手机设置，设计分辨率
# WIDTH = 375
# HEIGHT = 812
# PIXEL_RATIO = 3.0
# UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) CriOS/27.0.1453.10 Mobile/10B350 Safari/8536.25'

# mobileEmulation = {"deviceMetrics": {"width": WIDTH,
#                                      "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
# options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation', mobileEmulation)

# driver = webdriver.Chrome(chrome_options=options)
# driver.set_window_size(WIDTH, HEIGHT)
# driver.get('http://m.baidu.com')
# time.sleep(10)
# driver.close()

# import logging
# logger = logging.getLogger('test')
# logger.setLevel(logging.INFO)

# # # 不写路径,会在git目录同级下，即Src下
# handler_warn = logging.FileHandler(r'C:\Users\liuhua2\Desktop\warning_log.txt')
# handler_warn.setLevel(logging.WARN)

# handler_info = logging.FileHandler(r'C:\Users\liuhua2\Desktop\info_log.txt')
# handler_info.setLevel(logging.INFO)

# formatter = logging.Formatter(
#     '%(asctime)s-%(name)s-%(levelname)s-%(message)s')  # 设置日志格式
# handler_warn.setFormatter(formatter)
# handler_info.setFormatter(formatter)

# show_window = logging.StreamHandler()
# show_window.setFormatter(formatter)

# logger.addHandler(handler_warn)
# logger.addHandler(handler_info)
# logger.addHandler(show_window)

# logger.info('Information——test')
# logger.warning('Warning——test')

# 异常处理案例
# 导入日志记录模块

# import logging
# # 创建一个记录器
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # 创建一个日志处理程序

# handler = logging.FileHandler('ex1_critical.txt', encoding='utf-8')
# handler.setLevel(logging.INFO)

# # 日志的格式
# formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# handler.setFormatter(formatter)

# # 将处理程序添加到记录器
# logger.addHandler(handler)


# def age():
#     logger.info('Inside function age()')
#     try:
#         logger.info('In the try Block')
#         age = int(input('请输入你当前年龄'))
#         logger.debug('Value of age is{}'.format(age))
#     except ValueError as e:
#         logger.critical('Invalid Input', exc_info=True)


# if __name__ == '__main__':
#     age()
# Visual Studio IntelliCode智能提醒插件 ***
# import unittest
# import logging
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By

# # create a logger

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # log handler
# # create and name xx.txt

# handler_critical = logging.FileHandler('xxxx.txt', 'w')
# handler_critical.setLevel(logging.WARNING)

# # output log message
# handler_info = logging.StreamHandler()
# handler_info.setLevel(logging.INFO)

# # log format
# formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
# handler_critical.setFormatter(formatter)
# handler_info.setFormatter(formatter)

# # add handler message
# logger.addHandler(handler_info)
# logger.addHandler(handler_critical)


# class YoutubeSearch(unittest.TestCase):
#     def setUp(self):
#         logger.info("------xxx------")
#         self.browser = webdriver.Firefox()
#         self.browser.get('http://www.xxx.com')
#         logger.info('------xxx------')

#     def tearDown(self):
#         logger.info('------xxx------')
#         self.browser.save_screenshot('XXX.png')
#         self.browser.quit()
#         logger.info('------xxx------')

#     def test_youtube_search(self):
#         logger.info('------xxx------')
#         try:
#             self.assertIn('xxx', self.browser.title)
#             searchElement = self.browser.find_element_by_id('xxx')
#         except AssertionError:
#             logger.critical('xxx', exc_info=True)
#             self.fail('xxx')
#         except NoSuchElementException:
#             logger.critical('xxx', exc_info=True)
#             self.fail('xxx')
#         else:
#             searchElement.send_keys('xxx')
#             searchElement.send_keys(Keys.RETURN)
#             logger.info('------xxx------')


# if __name__ == '__main__':
#     unittest.main(exit=False, warnings='ignore')


# import logging
# import os
# import time
# log_path = 'C:\\Users\\liuhua2\\Desktop\\'


# class print_log():
#     def __init__(self):
#         # filename
#         self.logname = os.path.join(
#             log_path, '{}.txt'.format(time.strftime('%Y-%m-%d')))
#         self.logger = logging.getLogger('__name__')
#         self.logger.setLevel((logging.DEBUG))

#         # log format
#         self.formatter = logging.Formatter(
#             '%(asctime)s-%(filename)s-%(levelname)s:%(message)s')

#     def __console(self, level, message):
#         # create a filehandler,for write local
#         fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
#         fh.setLevel(logging.DEBUG)
#         fh.setFormatter(self.formatter)
#         self.logger.addHandler(fh)
#         # create a StreamHandler,for output console
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#         ch.setFormatter(self.formatter)
#         self.logger.addHandler(ch)
#         if level == 'info':
#             self.logger.info(message)
#         elif level == 'debug':
#             self.logger.debug(message)
#         elif level == 'warning':
#             self.logger.warning(message)
#         elif level == 'error':
#             self.logger.error(message)
#         # clear log for avoid Repeat output
#         self.logger.removeHandler(ch)
#         self.logger.removeHandler(fh)
#         fh.close()

#     def debug(self, message):
#         self.__console('debug', message)

#     def info(self, message):
#         self.__console('info', message)

#     def warning(self, message):
#         self.__console('warning', message)

#     def error(self, message):
#         self.__console('error', message)


# if __name__ == '__main__':
#     log = print_log()
#     log.info('----测试开始----')
#     log.info('输入密码')
#     log.warning('----测试结束----')  # end


import time
import os
import logging
import unittest
from selenium import webdriver

log_path = r"C:\Users\Administrator\Desktop\Seleium"


class print_log():
    def __init__(self):
        # filename
        self.logname = os.path.join(
            log_path, '{}.txt'.format(time.strftime('%Y-%m-%d')))
        self.logger = logging.getLogger('__name__')
        self.logger.setLevel((logging.DEBUG))

        # log format
        self.formatter = logging.Formatter(
            '%(asctime)s-%(filename)s-%(levelname)s:%(message)s')

    def __console(self, level, message):
        # create a filehandler,for write local
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # create a StreamHandler,for output console
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # clear log for avoid Repeat output
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


log = print_log()


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.baidu.com')
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        log.info("-----测试用例结束-----")

    def test_01(self):
        log.info('-----测试用例开始-----')
        self.driver.find_element_by_id("kw").send_keys('yoyo')
        log.info('输入内容：yoyo')
        self.driver.find_element_by_id("su").click()
        log.info("点击按钮：id=su")
        time.sleep(2)
        log.info('获取title内容：{}'.format(self.driver.title))
        self.assertIn('百度搜索', self.driver.title)


if __name__ == "__main__":
    unittest.main()
