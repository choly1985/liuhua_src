#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-14 09:28:36
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
# dir用来查看入参的全部方法
# [dict.modules, clear, fromkeys, keys, values, pop, popitem]
# dict_modules = [item for item in dir(dict) if '__' not in item]
# print(dict_modules)

# # dict_moduemailles = [item for item in dir(dict) if not '__' in item]
# # print(dict_modules)
# # clear 是清空字典中的所有键值对， key=value
# # copy  是复制一个字典全部的key value
# # fromkeys 初始化字典，是接受一个列表或元组， 并把元组中的所有元素作为key， 默认赋值key的value为None
# userinfo = ('liuhua', 'zhaoyang', 'jianghao')
# userdict = dict.fromkeys(userinfo, 0)
# print(userdict)

# # dict 的取值方式有两种，第一种是.get(key, default)， 第二种是dict['key']
# # dict.get(key, default) 当key在字典中不存在的时候， 默认返回None，如果定义default的参数， 则返回default
# # dict['key'] 的取值方式中， 如果key不存在与字典中， 则直接抛出KeyError的异常
# # print(userdict.get('suibian'))
# # # print(userdict['suibian']) 抛异常
# # print(userdict.get('suibian', 'yes'))  # 返回默认值yes

# # for key in userdict.keys():
# #     print(key, userdict[key])

# # print(userdict.items())
# # for key, value in userdict.items():
# #     print(key, value)

# # pop : dict.pop(param), 删除指定param的key和value， 并返回value
# print(userdict.pop('jianghao'))
# print(userdict)

# # popitem ： dict.popitem 删除一个默认的key=value的键值对， 并返回这个键值对的key=value
# print(type(userdict.popitem()))
# print(userdict)
# userdict.popitem()

# # dict.setdefault : 可以在一个字典中增加一个值, 并返回他的value， 默认返回为None
# userdict.setdefault('suibian', 'abc')
# print(userdict)

# userdict.setdefault('suibian', 'erer')
# print(userdict)

# userdict.update(keke='111')
# print(userdict)
# userdict.update({'abcd': 123})
# print(userdict)
# # dict.update 如果key不存在， 则新增一个key并新增对应的value
# # dict.setdefault 如果key不存在， 则新增， 如果key存在， 则不做任何修改
# # dict[key] = new_value， 这样写法可以直接新增或修改对应的key的value

# python中，一个空的数据类型(string, list tuple, set) 或 0 或 None 或False bool值都为False
#
# print(bool(integer))
# print(bool(string))
# print(bool(f_bool))

l_list = []
l_tuple = ()
l_set = {}
l_dict = {}

# l_list.append('liuhua')
# new_list = l_list.copy()
# print(new_list)
# new_list = ['liuli']
# print(new_list)

# if new_list and len(new_list):
#     print('normal')
# elif not new_list:
#     print('list is empty')
# elif len(new_list)[0] * 2 == 2:
#     print('new_list第一个元素长度为5')
# else:
#     pass

if __name__ == '__main__':
    userinfo = ['liuhua', 'jianghao', 'zhaoyang']
    userdict = dict.fromkeys(userinfo, 0)
    string_text = 'hi liuhua'
    # for user in userinfo:
    #     print(user)
    # for text in string_text:
    #     print(text)
    # for key in list(userdict.keys()):
    #     print(key)
    # for key, value in userdict.items():
    #     print(key, value)
    # for param in userinfo:
    #     print(param)

    # while len(userinfo) <= 10:
    #     print(len(userinfo))
    #     userinfo.append('liuh')

    # for item in userinfo:
    #     if item == 'zhaoyang':
    #         break
    #     print(item)

    # while 1:
    #     pass
    #     num = 0
    #     for _ in range(10):
    #         if num == 5:
    #             break
    #         num += 1
    #         print(num)
# while 如果用的不恰当， 他会进入一个死循环无法跳出
# break 只跳出最近一层循环 不管是for 或是while

    print(list(range(10)))

    # for _ in range(3):
    #     userinfo.pop()
    #     print(userinfo)

    # numbers = []
    # for num in range(10):
    #     numbers.append(num)
    # print(numbers)

    userinfo = ['Raymond', 'gang', 'dog', 'devan', '牛仔']

    # for item in userinfo:
    #     if 'dog' == item:
    #         continue
    #     elif 'Raymond' == item:
    #         pass
    #     elif item == 'devan':
    #         break
    #     print(item)
    # range(10) ==> 0-9
    # range(10) list(range(10)) ==> 0-9
    # list(range(1, 11)) ==> 从1开始 到11结束但不包含11 也就是1-10
    # range(start, end, step)

    # for number in range(3, 13, 2):
    #     print(number)
    #     if number == 3:
    #         pass
    #     elif number == 5:
    #         continue
    #     elif number == 7:
    #         continue
    #     else:
    #         break

    for item in userinfo:
        if 'Raymond' == item:
            continue
        elif 'dog' == item:
            pass
        print(item)

    userpram = ['刘德华', '黎明', 'Raymond', 'dog', '随便', '牛仔']
    username = 'a'

    if bool(userpram.count('dog')):
        print(True)
    else:
        print(False)

    num = 0
    for user in userpram:
        if user == username:
            print('username 在userpram中')
        elif num == len(userpram) - 1:
            print('username不存在userpram中')
        num += 1

    print()
