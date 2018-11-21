#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-21 13:51:10
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os

import json


class MyFirstClass:
    def __init__(self, name, age, city):
        self.log = True
        self.__name = name
        self.__age = age
        self.__city = city

    def __repr__(self)->str:
        if '_MyFirstClass__name' in dir(self):
            # print(dir(self))
            return '我的名字：{}，我的年龄{}，我在{}。当前的log信息状态为：{}'.format(
                self.__name, self.__age, self.__city, self.log)
        return 'user info is not define'

    def reset_name(self, new_name):
        self.__name = new_name

    def del_all_info(self):
        del self.__name, self.__age, self.__city, self.log


class Crawl:
    """docstring for Crawl"""

    def __init__(self, url, xpath, craw_name):
        self.info = url, xpath, craw_name

    def __repr__(self):
        # print(dir(self))
        return '需要请求的url:{},对应的解析xpath:{},爬虫对应的名字{}'.format(*self.info)


class PythonStudent:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.title = ('用户名', '年龄', '城市')

    def __repr__(self)->str:
        userinfo = (self.name, self.age, self.city)
        user_dict = {key: value for key, value in zip(self.title, userinfo)}
        user_json = json.dumps(user_dict, ensure_ascii=False, indent=4)

        # with open('Users_{}.json'.format(self.name), 'wb') as file:
        #     file.write(user_json.encode())
        #     # str按二进制读写,不指定编码的情况下
        #     file.close()

        with open('Users_{}.json'.format(self.name), encoding='utf-8', mode='w') as file:
            file.write(user_json)
            # 或者指定编码为utf-8
            file.close()
        return '数据存储完成，存储文件是Users_{}.json'.format(self.name)


if __name__ == '__main__':
    user_info = [
        ('Gang', 18, '上海'),
        ('liuhua', 33, '深圳'),
        ('Raymon', 20, '北京'),
        ('jiahao', 27, '西安'),
        ('谷子', 22, '天津')
    ]
    user = MyFirstClass(*user_info[2])
    print(user, type(user))
    user.reset_name('行者')
    print(user)
    user.reset_name('在路上')
    print(user)
    user.del_all_info()
    print(user)

    crawl = Crawl('http://baidu.com', '//title/text()', '百度')
    print(crawl, dir(crawl))

    for user in user_info:
        class_PythonStudent = PythonStudent(*user)
        print(class_PythonStudent)
