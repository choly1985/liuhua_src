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
    #             #redis.set('error_random', url) ###不懂url??#
    #             print('捕获位置异常，异常消息为：', ex)

    # class ValideJsonError(Exception):
    #     def __init__(self, msg):
    #         self.msg = msg

    #     def __repr__(self):
    #         return self.msg
    # raise ValideJsonError('错误的Json结构体')
    import random
    import string

# print([item for item in dir(random) if not item.startswith('__')])
# print([item for item in dir(random) if '__'not in item])
# print(type([item for item in dir(random) if '__'not in item]))

# print(random.randint(1, 2))  # random.randint包含右边的值
# print(string.ascii_letters)
# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

# buf = ['@163.com', '@qq.com', '@gmail.com', '@yahoo.com']

# head = random.sample(string.ascii_letters + string.digits, 8)
# print(type(str(head)))
# print(head[0])
# print(head)
# email = ''.join(head) + random.choice(buf)
# print(''.join(head))
# print(email)
# print('join: 将一个列表转换成一个字符串：', ''.join(head))
# # '分隔符'.join 快速的把一个列表转换成字符串
# # '元素/分隔符/元素/分隔符....
# tuple1 = list((1, 2))
# print(tuple1)
# print(type((1, 2)))

    # mobile_head = ['137', '138', '139', '140', '150', '177']
    # print(random.choice(mobile_head) + str(random.randint(10000000, 99999999)))


# class Usage(Exception):
#     """dmsgtring for  Usage"""

#     def __init__(self, msg):
#         super(Usage, self).__init__()
#         self.msg = msg

#     def __repr__(self):
#         return self.msg


# raise Usage('Usage error')
# user_input = int('1')
# print(user_input, type(user_input))
# user_input = input('请输入一个数字：')
# print('用户输入的数字是：', user_input, '类型是', type(user_input))
# input接受的类型 是一个字符串
# input的作用是接受用户输入的一个参数, 传递给一个变量,变量类型为

# 随机出一个数字
# 让用户去猜
# 如果用户持续猜错 可以选择继续猜，或者通过ctrl + c的方式结束游戏
# 如果用户猜对了， 则自动退出
# 如果错误， 则重新猜

    import sys

    user_input_list = []
    while 1:
        rand = random.randint(1, 10)
        print('rand is {}'.format(rand))
        user_input = input('请输入一个数字:')
        print(u)
        try:
            user_input = int(user_input)
            if user_input_list.count(user_input) >= 5:
                print('该数字输入5次，不可继续输入啦!')
                continue
            if rand == int(user_input):
                print('恭喜你，猜对了！游戏退出')
                break
            else:
                user_input_list.append(user_input)
                print('user_input :{}'.format(
                    user_input), 'comp :{}'.format(rand))
                print('猜错了哦，继续加油，或者CTRL+C退出游戏！')
        except KeyboardInterrupt:
            sys.exit(0)
        except ValueError:
            print('输入参数错误，只接受int类型的参数')
