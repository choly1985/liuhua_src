#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-15 23:26:33
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os

# user_dict = dict(a=1, b='a')  # 初始化字典
# print(user_dict)

# beijing = user_dict.get('beijing', '北京')
# print(beijing, user_dict)

# # print(user_dict['beijing'])

# user_dict = dict(beijing='北京', shanghai='上海', tianjin='天津')
# print(type(user_dict.keys()))
# print(type(user_dict.keys()))
# print(user_dict.keys()[1])
# 我们不能直接对dict.keys() 和 dict.values()返回的类型进行下标取值
# print(list(user_dict.keys())[1])
# 如果我们需要通过下标取出dict.keys or dict.values中对应index的元素， 可以用list(dict.keys())

# for key, value in user_dict.items():
#     print(key, value)
# for key in user_dict.keys():
#     print(key, user_dict[key])

# print(user_dict)
# userinfo = ('Raymond', '牛仔', 'gang', '老虎')
# user_dict = dict.fromkeys(userinfo, 0)  # 返回一个全新的dict，之前的dict值被替换
# print(user_dict)
# print(user_dict.pop('Raymond'))
# print(user_dict.popitem())
# pop输入一个key 然后删除掉字典中这个key所对应的键值对 key=value， 并返回value的值
# pop只返回value,但是popitem返回的是key和value的一个元组

# 改变字典的值
# user_dict['Raymond'] = 1
# user_dict.update(gang=2)
# user_dict.setdefault('随便', 'suibian')
# user_dict.setdefault('gang', 4)
# print(user_dict)

# print(bool(user_dict))
# print(bool(0))

if __name__ == '__main__':
    import sys
    userdict = {}
    # try:
    #     print(userdic['dog'])
    # # except KeyError as ex:
    #     print('捕获key Error异常，他的错误信息是：', ex)
    # # except NameError as ex:
    #     print('捕获name error 异常，他的错误消息是：', ex)
    # # except ValueError as ex:
    #     print('捕获value error异常，他的错误消息是：', ex)
    # except KeyError as msg:
    #     print(str(msg) + 'is not in dict')
    # except (NameError, ValueError, KeyError) as err:
    #     t, v, _ = sys.exc_info()
    #     print(t, v)
    # #print('捕获到key error 或 value error的相关错误, 错误信息为：', err)
    # except Exception as ex:
    #     print('捕获位置异常，异常消息为：', ex)
    # raise , 主动抛出异常的关键字

    from time import sleep

    # num = 0
    # while num < 100:
    #     num += 1
    #     try:
    #         if num == 100:
    #             raise ValueError('num==100,so except')
    #     except ValueError as ex:
    #         print(num)
    #         print(ex)
    #     # ValueError自定义错误信息，然后打印
    # print(num)

    num = 0
    redis = ''
    # while 1:
    #     print(num)
    #     if True:
    #         num += 1
    #         sleep(1)
    #     if num == 3:
    #         try:
    #             raise TimeoutError('异常失败处理，重复尝试3次请求依然失败')
    #         except TimeoutError as ex:
    #             #redis.set('error_random', url) ###不懂url#
    #             print('捕获位置异常，异常消息为：', ex)

    # class ValideJsonError(Exception):
    #     def __init__(self, msg):
    #         self.msg = msg

    #     def __repr__(self):
    #         return self.msg
    # raise ValideJsonError('错误的Json结构体')
