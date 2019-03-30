#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-30 00:26:28
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os

# 属性引用


# class Person(object):
#     """docstring for ClassName"""
#     role = 'person'

#     def walk(self):
#         print("person is walking..")


# print(Person.role)
# print(Person.walk)

# 实例化

class NewPerson(object):
    """docstring for NewPerson"""
    role = 'new person'

    def __init__(self, name):
        super(NewPerson, self).__init__()
        self.name = name

    def walk(self):
        print("new person is walking..")


testPerson = NewPerson('test')
print(testPerson.role, testPerson.name)
testPerson.walk()
