#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-08 15:05:52
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
"""打印9*9乘法表"""
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{}*{}={}".format(j, i, i * j), end='\t')
#     print('')


"""有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？"""
# list_number = []
# count = 0
# for i in range(1, 10):
#     for j in range(1, 9):
#         for k in range(1, 9):
#             if (i != j) and (i != k) and(j != k):
#                 count += 1
#                 list_number.append(100 * i + 10 * j + k)
# print("4个数字组成不重复数字共有{}个".format(count), list_number)


"""企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间
时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100
万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键
盘输入当月利润I，求应发放奖金总数？"""
# I = float(input('请输入当月利润：'))
# if I < 100000:
#     print('当月应发奖金总数为{}'.format(I * 0.1))
# elif I < 200000:
#     print('当月应发奖金总数为{}'.format(100000 * 0.1 + (I - 100000) * 0.075))
# elif I < 400000:
#     print('当月应发奖金总数为{}'.format(100000 * 0.1 +
#                                100000 * 0.075 + (I - 200000) * 0.05))
# elif I < 600000:
#     print('当月应发奖金总数为{}'.format(100000 * 0.1 + 100000 *
#                                0.075 + 200000 * 0.05 + (I - 400000) * 0.03))
# elif I < 1000000:
#     print('当月应发奖金总数为{}'.format(100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 +
#                                +(I - 600000) * 0.015))
# else:
#     print('当月应发奖金总数为{}'.format(100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 +
#                                +400000 * 0.015 + (I - 1000000) * 0.01))
# import time
# time_start = time.time()
# for i in range(1, 10):
#     for j in range(10):
#         for k in range(10):
#             for m in range(10):
#                 for n in range(10):
#                     if (10000 * i + 1000 * j + 100 * k + 10 * m + n) * 9 == 10000 * n + 1000 * m + 100 * k + 10 * j + i:
#                         print('{}'.format(10000 * i + 1000 *
#                                           j + 100 * k + 10 * m + n))
# time_end = time.time()
# print(time_end - time_start)

# time_start = time.time()
# for i in range(10000, 100000):
#     if i * 9 == (int(i % 10) * 10000 + int(i % 100 / 10) * 1000 + int(i % 1000 / 100) * 100 + int(i % 10000 / 1000) * 10 + int(i / 10000)):
#         print(i)
# time_end = time.time()
# print(time_end - time_start)
