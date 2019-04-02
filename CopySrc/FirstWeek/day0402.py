#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-02 18:24:31
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
bob = {}
bob['name'] = 'liuhua'
bob['age'] = 34
bob['city'] = 'shenzhen'
bob['money'] = 50
sms = dict(name='liuli', age=37, city='beijing', money=100)


family = {}
family['bob'] = bob
family['sms'] = sms
print(family)
