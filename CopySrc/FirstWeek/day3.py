#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-13 20:05:02
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
# 我们需要先把dict.keys的数据类型转换成list类型， 再做取值行为

# list.copy 复制一个列表
# userinfo = ['Raymond', '今晚打老鼠']
# new_userinfo = userinfo.copy()
# print(new_userinfo)

# list.extend 接受一个列表，并把接受的列表于原来列表合并
# userinfo.extend(new_userinfo)
# print(userinfo)

# list.reverse ：他会逆序一个list原有的index， 并改变这个列表
# numbers = [1, 2, 3, 4, 5]
# numbers.reverse()
# print(numbers)

# list.sort : 对列表进行升序排序， 并改变列表原有结构
# numbers = [2, 1, 6, 4, 5, 3, 7]
# numbers.sort()
# numbers ==> [1, 2, 3, 4, 5, 6, 7]
# numbers = sorted(numbers)
# number ==> [1, 2, 3, 4, 5, 6, 7]

if __name__ == '__main__':
    # dict_module = dir(dict)
    # dict_funs = [item for item in dict_module if '__' not in item]
    # print(dict_funs)

    # init_dict = dict(a=1, b=2, c='a')
    # print(init_dict)

    # clear清空一个字典
    # init_dict.clear()
    # print(init_dict)

    # copy 复制一个字典
    # test_dict = dict(a=1, b=2, c='a')
    # new_dict = test_dict.copy()
    # print(new_dict)

    # users = ('liuhua', 'zhaoyang', 'jianghao', 'tengfei')
    # values = ('a', 'b', 'c', 'd')
    # test_dict = {} #初始化字典
    # print(test_dict.fromkeys(users, values))
    # dict.fromkeys() : 是从一个列表或元祖中取出对应的元素，赋值给一个新的字典中的每一个key,values值不变

    # news = dict(beijing='北京', shanghai='上海', shenzhen='深圳')  # 初始化字典
    # print(news.get('shanghai'), news['shanghai'])
    # print(news.get('beijing'), news['beijing'])
    # print(news.get('shenzhen'), news['shenzhen'])

    # print(news.get('chengdu', '不存在的默认值'))
    # print(news.get('beijing', '不存在的默认值'))
    # print(news['chengdu'])
    # dict.get() : 输入一个key， 并返回这个key对应的value， 如果这个key不存在， 则默认返回None, 也可以传递给它一个默认值
    # dict['key'] : 如果这个key存在， 则返回key的value， 如果这个key不存在， 则抛出KeyError的异常

    # print(news)
    # news['shanghai'] = '夜上海'
    # print(news)
    # 如果我们需要修改一个字典对应key的value 我们可以用 dict['key'] = new_value的这种方式

    # news = {'beijing': "北京", 'shanghai': "上海", 'shenzhen': '深圳'}
    # news.update(beijing='新北京')
    # news['shanghai'] = '大上海'
    # dict.pop 不一样的点在于， dict.popitem返回的是一个(key, value) 而pop只返回value
    # dict.items() : 会返回一个字典对应的key value的全部结构体, 每一个元祖中，存储着对应的key， value

    # print(news.keys(), type(news.keys()))
    # print(news.values(), type(news.values()))
    # dict.keys() : 返回一个字典中全部的key， 返回的结构是dict_keys类型， 不能直接用index取值， 如果需要用index取值
    # 需要做一步转换 ： keys = list(dict.keys())
    # dict.values(): 返回一个字典中全部的value, 返回的结构是dict_values类型， 不能直接index取值， 如果需要用index取值
    # 需要做一步转换 ： keys = list(dict.values())

    # print(news.pop('beijing'))
    # print(news)

    # print(news.popitem())
    # print(news)
    # dict.pop 不一样的点在于， dict.popitem返回的是一个(key, value) 而pop只返回value

    # news.setdefault('chengdu', '成都')
    # print(news)
    # print(news.setdefault('hengyang', '衡阳'))
    # print(news)
    # dict.setdefault ：可以通过传递一个key 来给字典增加一个key value， 默认的value 为None，返回值为value

    # print(bool(''))
    # print(bool(0))
    # print(bool(' '))
    # print(bool(None))

    # f_list = []
    # f_dict = {}
    # f_set = set()
    # f_none = None
    # f_tuple = ()

    # print('f_list', bool(f_list))
    # print('f_tuple', bool(f_tuple))
    # print('f_dict', bool(f_dict))
    # print('f_set', bool(f_set))
    # print('f_none', bool(f_none))
    # print('please input num:')
    # num = input()
    # if num == 0:
    #     print('num!=0')
    # else:
    #     print('num==0')

    # news = {'beijing': '北京'}
    # if news.get('tianjin'):
    #     print('天津')
    # else:
    #     print('天津不在字典中')
    # num = 3
    # if isinstance(num, (int)):
    #     print('num is int')
    # elif isinstance(num, (str, dict)):
    #     print('num is str or dict object')
    # else:
    #     print('我也不知道num什么类型')
