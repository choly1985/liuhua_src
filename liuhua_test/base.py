'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-08-10 14:16:06
@LastEditors: liuhua
@LastEditTime: 2019-08-13 19:11:00
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
