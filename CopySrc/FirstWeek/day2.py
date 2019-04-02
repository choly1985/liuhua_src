#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-13 16:16:31
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
if __name__ == '__main__':
    # user_list = ['小布', 'mytest', 'liuhua', 'zhangbo', 'liuli']
    # print(type(user_list))
    # print(isinstance(user_list, list))
    # print(user_list[0], user_list[-5], user_list[-1], user_list[4])

    # user_string_text = '0123456789'
    # print(user_string_text[2], user_string_text[9], type(user_string_text))

    # user_tuple = ('小布', 'mytest', 'liuhua', 'zhangbo', 'liuli')
    # print(user_tuple[0], user_tuple[-5], user_tuple[-1])
    # print(user_tuple, type(user_tuple))

    # # dir python中查看一个对象他包含哪些可用方法
    # # print(dir(user_list))
    # # print(dir(user_tuple))
    # print(user_list[-1])
    # user_list.append(0)
    # print(user_list[-1])
    # # user_list.clear()  # clear方法， 是清空一个列表
    # # print(user_list)
    # print(user_list.count(0))  # count统计列表元素
    # print(user_list.index('liuhua', 0, 3))  # index 获取列表元素下标

    # user_list.insert(0, 'liuhua')  # 在user_list这个列表0号index位置， 增减一个元素
    # print(user_list)

    # print(user_list.pop())  # 删除一个列表中最后一位， 并把这个元素返回回来
    # print(user_list)

    # print(user_list.remove('liuhua'))  # remove 是移除list中的第一个该元素
    # print(user_list)

    # user_list.sort()  # 对列表进行升序排序， 并改变列表原有的index
    # print(user_list)
    # print(user_list[0])

    # print(sorted(user_list))
    # print(user_list)
    # print(user_list[0])  # python内置的sorted 是不会改变原有的listindex位置的

    # print(user_list[2:5])  # 切片中，第一个元素是包含的， 第二个元素是不包含的

    # print(user_tuple[0:5])

    # user_string_text = 'choly is good man!'
    # print(user_string_text[4:7])
    # print(user_string_text[0::2])

    # number_list = [item for item in range(0, 100)]  # 列表推导式赋值
    # print(number_list)
    # print(number_list[2:10:2])
    # print(number_list[-2:-10:-2])  # 可以实现列表倒序
    # print(number_list[-1:-50:-2])

    # a_list = sorted([1, 2, 2, 3, 4, 5, 2], reverse=True)
    # # print(a_list, a_list[0])
    # # b_list = sorted(list(set(a_list)))
    # # print(b_list, b_list[0])
    # # print(b_list.remove(2))
    # # print(b_list)

    # uniq_a_list = set(a_list)
    # # print(uniq_a_list, type(uniq_a_list))
    # b_list = list(uniq_a_list)
    # # print(b_list, type(b_list))
    # new_b_list = sorted(b_list)
    # # print(new_b_list)
    # # new_b_list.remove(2)
    # # print(new_b_list)
    # b = sorted(new_b_list)
    # b.remove(3)
    # print(b)
    # print(new_b_list)
    # new_b_list.remove(3)
    # print(new_b_list)

    # sorted(b_list).remove(2)
    # list.sort 是操作原有list并改变index顺序， 始终操作的是list本身
    # sorted(list) 是一个新的list，如果需要操作新的list 需要把这个新的list进行变量赋值

    import requests
    # dict_dir_list = dir(dict)
    # dict_module = [item for item in dict_dir_list if '__' not in item]    # 列表推导式
    # print(dict_module)
    # a_list = ['a', 'b', 'c', 'd', 'e']
    # b_list = ['ab', 'abc', 'agg', 'ff']
    # list_1 = [item for item in b_list if '' not in item]
    # print(list_1)
    # keys = ('zhaoyang', 'liuhua', 'jianghao')
    # values = ('27', '33', '27')
    # user_age = {key: value for key, value in zip(keys, values)}
    # print(user_age)

    # print(list(user_age.keys())[2])  # dict.keys 和dict.values并不能直接通过下标取值的形式直接取值
    # print(list(user_age.values())[2])  # 我们需要先把dict.keys的数据类型转换成list类型， 再做取值行为

    # tuple 只有1个元素时候加,不然会认为是一个str类型
    # tuple1 = ('list',)
    # list1 = ['list']
    # print(type(tuple1))
