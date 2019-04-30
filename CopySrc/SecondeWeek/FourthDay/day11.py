#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-23 09:24:45
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
import time


# test = [item for item in range(100)]
# time_begin = time.clock()
# while test:
#     del test[0]
# time_end = time.clock()
# print(time_end - time_begin)

# num = 0
# for i in range(0, 100):
#     try:
#         if 1:
#             num += 1
#     except Exception as e:
#         raise e

# try:
#     print(a)
# except:
#     print("aaaabbbb")

from abc import ABCMeta, abstractmethod


def return_sum_number(*args, **kwargs):

    if kwargs.get('param'):
        args = kwargs.get('param')
    return sum(args)


class Animal(metaclass=ABCMeta):

    def __init__(self, animal_name, animal_age, animal_color, **kwargs: dict):
        self.animal_info = [animal_name, animal_age, animal_color]
        if kwargs:
            self.animal_info.append(kwargs)

    @abstractmethod
    def call(self):
        raise NotImplemented

    @abstractmethod
    def swin(self):
        raise NotImplemented

    @abstractmethod
    def fly(self):
        raise NotImplemented

    @abstractmethod
    def run(self):
        raise NotImplemented

    def display(self):

        if len(self.animal_info) == 3:
            print("这是一只{}动物,它今年{}岁了，它有一身漂亮的{}颜色".format(*self.animal_info))
        else:
            print("这是一只{}动物,它今年{}岁了，它有一身漂亮的{}颜色".format(
                *self.animal_info[0:3]))
            info = ''
            for key, value in self.animal_info[-1].items():
                info += key + ':' + value + ' ,'
            print('它还有一些特殊的属性呢{}'.format(info))

    def __repr__(self):
        result = self.display()
        return '' if not result else result


class Dog(Animal):
    def __init__(self, name, age, color, **kwargs):
        super(Dog, self).__init__(name, age, color, **kwargs)

    def call(self):
        print("汪汪汪!")

    def swin(self):
        print("狗子会游泳")

    def fly(self):
        print("狗子不会飞")

    def run(self):
        print("狗子跑的快")


class Duck(Animal):
    def __init__(self, name, age, color, **kwargs):
        super(Duck, self).__init__(name, age, color, **kwargs)

    def call(self):
        print("Quack！Quack!Quack!")

    def swin(self):
        print("鸭子会游泳")

    def fly(self):
        print("鸭子还会飞")

    def run(self):
        print("鸭子没有狗子跑的快")


class 搞事情(object):
    """docstring for """
    def __init__(实例对象, *搞事情的不确定参数, **搞事情的关键字参数):
        实例对象.不确定参数元组 = 搞事情的不确定参数
        实例对象.不确定关键字字典 = 搞事情的关键字参数
        实例对象.打印 = print

    def 遍历不确定参数元组(实例对象):
        for 参数 in 实例对象.不确定参数元组:
            实例对象.打印(参数)

    def 将字典中的元素全部打印出(实例对象):
        for 关键字, 值 in 实例对象.不确定关键字字典.items():
            print(关键字, 值)


if __name__ == '__main__':

    # balck_dog = Dog("狗子", 5, "黑色的")
    # print(balck_dog)

    # fat = Dog('狗子', 18, '斑点', eat="特别能吃", fly="跑的快了还能飞")
    # print(fat)

    # yellow_duck = Duck('小黄鸭', 2, "黄色")
    # print(yellow_duck)

    # green_duck = Duck('绿头鸭', 3, "彩色", hair='一头绿色的长发', fly='迎风就飞起来')
    # print(green_duck)

    搞 = 搞事情(1, 2, 3, 4, 5, 6, abc=123, bcd=456, abcd='深圳欢迎你')
    搞.将字典中的元素全部打印出()
    搞.遍历不确定参数元组()
