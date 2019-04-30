#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-02 18:24:31
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
# bob = {}
# bob['name'] = 'liuhua'
# bob['age'] = 34
# bob['city'] = 'shenzhen'
# bob['money'] = 50
# sms = dict(name='liuli', age=37, city='beijing', money=100)


# family = {}
# family['bob'] = bob
# family['sms'] = sms
# print(family)

name = ['zhoushuai', 'chenwenjie', 'zhangbo']
age = [31, 34, 33]
# studentinfo = dict(zip(name, age))
# print(studentinfo)
# listnew = name + age
# print(listnew)
# name.append(1234)
# print(name)

oo = list((1, 'b'))
name[len(name):] = age
oo.append('wwww')
print(oo)

squares = list(map(lambda x: x**2, range(10)))
squares_1 = [x**2 for x in range(10)]
print(squares, squares_1)
