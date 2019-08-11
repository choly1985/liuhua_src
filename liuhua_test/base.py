'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-08-10 14:16:06
@LastEditors: liuhua
@LastEditTime: 2019-08-11 23:55:00
'''
import xlrd

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

{
    "git.autofetch": true,
    "editor.fontSize": 20,
    "editor.renderWhitespace": "none",
    "editor.minimap.enabled": true,
    "breadcrumbs.enabled": true,
    "workbench.colorTheme": "Sublime Material Theme - Dark",
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "autopep8",
    "python.linting.enabled": false,
    "python.linting.flake8Args": [
        "--max-line-length=128"
    ],
    "editor.formatOnType": true,
    "editor.formatOnSave": true,
    "fileheader.customMade": {
        "Description": "python",
        "Version": "1.0",
        "Autor": "liuhua",
        "QQ": "434375025@qq.com",
        "Link": "https://github.com/choly1985",
        "Date": "Do not edit",
        "LastEditors": "liuhua",
        "LastEditTime": "Do not edit"
    },
    "fileheader.cursorMode": {
        "description": "python",
        "param": "param",
        "return": "None",
        "author": "liuhua"
    },
    "workbench.iconTheme": "vscode-icons",
    "debug.allowBreakpointsEverywhere": true,
    "debug.inlineValues": true,
    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
    "workbench.editor.enablePreview": false
}
# koroFileHeader
# python-autopep8
# vscode-icons
