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
        self.mobile_head = mobile_number_head
        self.first_name = frist_name_head
        self.name_lenth = name_lenth
        self.save_json_file_path = 'Users'
        self.return_title = 'Datas<{}>'
        self.func_args = [item for item in dir(self) if not item.startswith(
            '__') and callable(getattr(self, item))]

    def write_file(self, file_name, data):
        file_name = '{}/{}.json'.format(self.save_json_file_path, file_name)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(data)

    def make_user_json_and_write_file(self):
        titles = ('中文名', '密码', '手机号', '邮箱', '创建时间')
        name = self.make_user_name()

        infos = (
            name,
            self.make_random_password(),
            self.mobile(),
            self.make_user_email(),
            time.strftime('%Y-%m-%d %H:%M:%S')
        )
        data = json.dumps({key: value for key, value in zip(
            titles, infos)}, ensure_ascii=False, indent=4)
        self.write_file(name, data)

    def make_random_password(self):
        return ''.join(random.sample(string.digits + string.ascii_letters + string.punctuation, 8))

    def make_user_email(self):
        buf = ['@163.com', '@qq.com', '@gmail.com',
               '@yahoo.com', '@hotmail.com']
        head = random.sample(string.ascii_letters + string.digits, 8)
        email = ''.join(head) + random.choice(buf)
        return email

    def make_user_name(self)->str:
        if not self.first_name:
            self.first_name = random.choice(list(FIRST_NAME_ENUM))
        if not self.name_lenth:
            self.name_lenth = 2 if random.randint(1, 100) > 50 else 1

        last_name = ''.join(random.sample(
            list(LAST_NAME_ENUM), self.name_lenth))
        print('用户名是 :{}'.format(self.first_name + last_name))
        return self.first_name + last_name

    def mobile(self):
        if self.mobile_head:
            try:
                int(self.mobile_head)
            except Exception as err:
                raise err

        if self.mobile_head and len(list(self.mobile_head)) == 3:
            return self.mobile_head + ''.join(random.sample(list(string.digits), 8))
        mobile = ['137', '138', '139', '131', '140', '150', '177']
        return random.choice(mobile) + ''.join(random.sample(list(string.digits), 8))

    def __repr__(self):
        return 'Datas(<{}>)'.format(self.func_args)


class FruitsMarket:
    def __init__(self, mkname, create_time=time.strftime('%Y-%m-%d')):
        self.mkname = mkname
        self.create_time = create_time
        print(self.create_time)
        self.all_fruits_count = 100

    def buy_some_fruits(self, fruits_count):
        self.all_fruits_count += fruits_count

    def cell_some_fruits(self, fruits_count):
        self.all_fruits_count -= fruits_count

    def throw_some_fruits(self):
        self.all_fruits_count -= 2

    def __repr__(self):
        return str(self.all_fruits_count)


class InterfaceTest(Data):
    def __init__(self):
        super(InterfaceTest, self).__init__()
        print(self.mobile())
        print(self.make_user_name())


if __name__ == '__main__':
    # datas = Data()
    # datas.make_user_json_and_write_file()
    # print(datas)

    market = FruitsMarket('上海贸易中心', '2019-05-05')
    print(market)
    market.cell_some_fruits(21)
    print(market)
    market.buy_some_fruits(15)
    print(market)
    market.throw_some_fruits()
    print(market)

    # interface = InterfaceTest()

    # with open("Users/赵明.json", encoding='utf-8') as file:
    # message = file.read()
    # print(message)

    # with open('Users/testfile.txt', encoding='utf-8') as file_object:
    #     for line in file_object:
    #         print(line.rstrip())  # 文件末尾有看不见的换行符，print语句会加上

    # with open("Users/testfile.txt", encoding='utf-8') as file_object:
    #     lines = file_object.readlines()

    # for line in lines:
    #     print(line.rstrip())

    # pi_string = ''
    # for line in lines:
    #     pi_string += line.strip()
    # print(len(pi_string))
