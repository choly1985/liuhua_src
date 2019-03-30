#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-22 10:38:54
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
import json


class Student(object):
    """他是一个学生信息管理的类"""

    def __init__(self, name, age, sex, classinfo):
        """
            类在初始化的时候接受三个必传参数
            :param name: 学生名
            :param age: 学生年龄
            :param sex: 学生的性别
            :param classinfo: 班级信息
        """
        self.user_info = name, age, sex, classinfo
        # self.user_info是一个tuple类型
        print(type(self.user_info))
        if len(self.user_info) != 4:
            raise AttributeError('传递进来的参数错误，请验证后重新传递')
        self.user_info_back = self.user_info
        self.users_path = 'Users'
        self.titles = ('用户名', '年龄', '性别', '班级')
        self.user_info_dict = {key: value for key,
                               value in zip(self.titles, self.user_info)}
        print(dir(self))

    def save_userinfo(self):
        """
            将用户信息存储到对应的路径下
            :return:
        """
        if '{}.json'.format(self.user_info_back[0]) in os.listdir(os.path.abspath(self.users_path)):
            return '用户名信息已经存在'

        with open('{}/{}.json'.format(self.users_path, self.user_info_back[0]), 'wb') as file:
            file.write(json.dumps(self.user_info_dict,
                                  indent=4, ensure_ascii=False).encode())

    def get_userinfo(self):
        """
            查询用户信息的方法
            :return:
        """
        if '{}.json'.format(self.user_info_back[0]) not in os.listdir(os.path.abspath(self.users_path)):
            enter = input('用户信息已删除，是否重新存储？：Y/N')
            if enter == 'Y':
                self.save_userinfo()
            else:
                return '用户信息不存在请查询其他用户'
        print(json.dumps(self.user_info_dict, indent=4, ensure_ascii=False))

    def del_userinfo(self):
        """
            删除掉这个类实例保存的用户信息
            :return:
        """
        del self.user_info

    def __repr__(self):
        if 'user_info' not in dir(self):
            return '用户信息已删除'
        return '<Student"{}">'.format(self.user_info_back[0])


class Fruits(object):
    """这是一个水果类"""

    def apple(self):
        """
            return apple
        """
        print('这里有一个苹果')

    @classmethod  # 引用不需要实例化，staticmethod也不需要实例化，且不需要self,cls参数
    def banana(cls):
        """
            return banana
        """
        print("这里有一个香蕉")

    def orange(self):
        """
            return orange
        """
        print('这里有一个橘子')

    def all_fruits(self):
        self.apple()
        self.banana()
        self.orange()


class Sum(object):
    """Sum"""

    def __init__(self, num_a, num_b):
        self.numbers = [num_a, num_b]

    def return_sum(self):
        return sum(self.numbers)

    def modify_num(self, num_index: int, value):
        try:
            self.numbers[num_index] = value
        except IndexError:
            print('超过最大index,请重新输入')

    def __repr__(self):
        return '<Sum({}+{}:{})>'.format(*self.numbers, self.return_sum())


# if __name__ == '__main__':

    # userinfo = ['liuli', 33, '男', '三班']
    # ray = Student(*userinfo)
    # # ray.del_userinfo()
    # print(ray.save_userinfo())
    # # ray.del_userinfo()  # 删除自定的类对象
    # print(ray)
    # ray.get_userinfo()
    # # print(ray.user_info)
    # print(dir(ray))

    # print('user_info' in dir(ray))  # 表达式的值 True or False
    # print(ray.user_info in dir(ray), ray.user_info, ray, ray.get_userinfo())
    # ray.get_userinfo()
    # fruits = Fruits()
    # fruits.apple()
    # fruits.banana()
    # fruits.orange()
    # Fruits.banana()
    # sum_ = Sum(10, 5)
    # print(sum_)

    # sum_.modify_num(0, 100)
    # print(sum_)

    # sum_.modify_num(1, 55)
    # print(sum_)

    # sum_.modify_num(2, 100)  # 抛出异常
