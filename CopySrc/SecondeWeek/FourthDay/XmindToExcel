# -*- coding: utf-8 -*-

__author__ = "庄锦弟-2018/09/28"
'''
导出xmind文件成Excel文档
'''

import xml.etree.ElementTree as ET
import xlwt
import argparse
import time

test_time = time.strftime ("%Y%m%d%H%M%S", time.localtime ())
g_row = 2
g_row2 = 2

#设置边框   #DASHED虚线  NO_LINE没有  THIN实线
borders = xlwt.Borders()
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN

# borders.left_colour = 0x40
# borders.right = 0x40
# borders.top = 0x40
# borders.bottom_colour = 0x40

# 设置单元格宽度
# borders = xlwt.Borders()
# borders.left = 1
# borders.right = 1
# borders.top = 1
# borders.bottom = 1
# borders.bottom_colour = 0x3A

font = xlwt.Font() #为样式创建字体
font.name = '微软雅黑'
font.bold = True

style = xlwt.XFStyle() # 初始化样式
style.borders = borders
style.font = font #为样式设置字体

def do_write_excel(text, row, col):
    ws.write(row, col, text)

#通过递归的获取子节点的形式达到获取 xml 等级,写入表格数据
def perf_func(elem, func, level = 0):
    global g_row
    func(elem, g_row, level)

    for child in list(elem):
        name = child.get('TEXT')
        perf_func(child, func, level + 1)
        if child.find('node') is None and name is not None:
            g_row = g_row + 1

#通过递归的获取子节点的形式达到获取 xml 等级，循环表格生成边框
def perf_func2(elem, func, level = 0):
    global g_row2
    func(elem, g_row2, level)

    for child in list(elem):
        name = child.get('TEXT')
        perf_func2(child, func, level + 1)
        if child.find('node') is None and name is not None:
            g_row2 = g_row2 + 1

def count_row(elem, row, level):
    pass

def write_excel(elem, row, level):
    name = elem.get('TEXT')
    if name is not None:
        do_write_excel(name, row, level)

'''
# 设置单元格对齐方式
VERT_TOP = 0x00 上端对齐
VERT_CENTER = 0x01 居中对齐（垂直方向上）
VERT_BOTTOM = 0x02 低端对齐
HORZ_LEFT = 0x01  左端对齐
HORZ_CENTER = 0x02 居中对齐（水平方向上）
HORZ_RIGHT = 0x03 右端对齐
'''
# 设置title
def setWsTitile():
    al = xlwt.Alignment()
    al.horz = 0x02  # 设置水平居中
    al.vert = 0x01  # 设置垂直居中
    style.alignment = al
    ws.write_merge(0, 0, 0, 7, 'O(∩_∩)O Testlink测试用例 O(∩_∩)O', style)  # 合并单元格
    ws.write(1, 0, '测试用例集路径', style)  # 使用样式
    ws.write(1, 1, '用例标题', style)  # 使用样式
    ws.write(1, 2, '预置条件', style)  # 使用样式
    ws.write(1, 3, '步骤', style)  # 使用样式
    ws.write(1, 4, '步骤动作', style)  # 使用样式
    ws.write(1, 5, '预期结果', style)  # 使用样式
    ws.write(1, 6, '优先级', style)  # 使用样式
    ws.write(1, 7, '是否自动化用例', style)  # 使用样式

#python 参数解析内嵌库 argparse,带两个参数
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input-file', type=str, dest='inputfile', required=True)
parser.add_argument('-o', '--output-file', type=str, dest='outputfile', default='测试用例'+test_time+'.xls', help='Default outputfile is freemind2excel.xls')

args = parser.parse_args()

if args.inputfile is None:
    parser.print_help()
    exit()

root = ET.parse(args.inputfile)
map_version = root.getroot()
first_node = map_version.find('node')

wb = xlwt.Workbook()
ws = wb.add_sheet('freemind2excel',cell_overwrite_ok=True)

#设置行高
ws.width=256*20
tall_style = xlwt.easyxf('font:height 480;')
ws_row = ws.row(0)
ws_row.set_style(tall_style)

# 设置单元格宽度
# ws.col(0).width = 3333
# for i in range(8):
# a=[0,1,2,3,4,5,6,7]
b=[0, 1, 4, 5]
for i in b:
    ws.col(i).width = 6666
ws.col(2).width = 3333

# 设置边框
perf_func2(first_node, count_row)
for row in range(1, g_row2+1):
    for col in range(8):
        ws.write(row, col, None, style)
#print(('行数'),'=',(g_row2))
# 插入数据
perf_func(first_node, write_excel)
# 设置title
setWsTitile()
# 保存文件
wb.save(args.outputfile)