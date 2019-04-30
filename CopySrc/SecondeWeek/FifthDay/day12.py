#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-30 17:28:41
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
import json
import random
import string
import time

"""
实现一个构造测试数据的类
# 这个类能生成指定号段的手机号码
# 这个类能生成随机中文名字， 可指定生成名字的姓氏和长度
# 这个类可以生成一共用户信息的字典， 该用户信息字典包含 用户中文名 密码 邮箱 手机号 创建这条数据的时间
# 将用户信息存储到用户文件夹下
# 定义repr 查看对应类实例对象的基础信息
"""

FIRST_NAME_ENUM = '赵钱孙李周吴郑王'
LAST_NAME_ENUM = '洋华锐豪明林飞彬'


class Data:

    def __init__(self, mobile_number_head=None, frist_name_head=None, name_lenth=None):
