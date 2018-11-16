#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-16 18:07:39
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
import random
import string

# import day5
# # from FirstWeek.ForthDay import SouceCode   # import module
# # import FirstWeek    # import packages
#
# # module: python中，每个单独的文件， 代表一个module
# # packages : pip install requests  python site-packages/requests/， 每个文件夹代表packages

numbers = list(range(1, 100))
print(random.choice(numbers))  # random.choice 接受一个可迭代的对象， 从对象中随机取出一个元素， 并返回
# random.randint 接受2个参数，一个是起始点， 一个是结束点， 从这两个点之间(包含这两点)随机返回一个int类型的值
print(random.randint(1, 99))
print(random.sample(numbers, 8))
# random.sample 接受2个参数， 第一个参数为可迭代的对象，第二个参数为返回这个对象中的几个元素，返回列表类型
print([item for item in dir(string) if not item.startswith('__')])
print(numbers)
random.shuffle(numbers)
print(numbers)

print(string.ascii_letters)
print(string.digits)
print(string.ascii_lowercase)
print(string.ascii_uppercase)


numbers = list(string.digits)
random.shuffle(numbers)
headers = ['138', '139', '140', '131', '155', '157']
mobile_number = random.choice(headers) + ''.join(random.sample(numbers, 8))
# random.randint 接受2个参数，一个是起始点， 一个是结束点， 从这两个点之间(包含这两点)随机返回一个int类型的值
print(mobile_number)
