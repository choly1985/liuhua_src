#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-19 15:44:05
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os

# log

# pythonÐ´ÎÄ¼þ
# mode :r,rb,w,wb,a,a+

# file = open('log.txt', mode='w', encoding='utf-8')
# file.write('这是python写进来的log\n\r\n')
# file.write('好吧， 我要写很多个file.write\r')
# # w在操作的过程中会覆盖原有的文件
# file.write('123')
# file.close()
# print(file.close)

# mode=a 追加写入，不存在就会创建
# file = open('log.txt', mode='a', encoding='utf-8')
# file.write('mode=a的时候，我要在这个文件的最后位置新增一行信息')
# file.close()

# writelines 多行写入
# file = open('log.txt', mode='w', encoding='utf-8')
# file.writelines(['\n我是整行写入的', '\n我想在这行再加一些备注'])
# file.writelines(['\n我是第二个整行', '\n好吧我觉得我没什么写的了就是想在这里占一个位置'])
# file.close()


# str=>bytes
# bytes=> str

# string_text='我是雷蒙德！'
# print('string_text',string_text,type(string_text))
# bytes_text=string_text.encode() #str=>bytes
# print(bytes_text,type(bytes_text))
# bytes2string=bytes_text.decode() #bytes=>str
# print(bytes2string)

# with open('log.txt', mode='rb') as file:
#     data = file.read()
#     data1 = file.read()
#     # print(file.read())

# with open('log.txt',mode='rb') as file:
#     data1=file.read()
#     print(data)
# # 这里会返回一个空的bytes类型的数据，因为file.read()只会返回一次数据，返回后数据被消费掉

# print(data.decode('utf-8'))
# file_text=data.decode()
# print(file_text)

# with open('log.txt', mode='r', encoding='utf-8') as file:
#     for line, item in enumerate(file, 1):
#         print(line, item.replace('\n', ''))

# with open('log.txt', mode='r', encoding='utf-8') as file:
#     data = file.readlines()
#     for line, item in enumerate(data, 1):
#         print(line, item.replace('\n', ''))

# my_logs = ['这是一个美丽的下午\n', '非常适合学习\n', '如果有人一起学习就更好了\n']


# def write_file(mode: str, logs: list)->str:
#     """
#         接受一个log的列表，并把这个log的列表写入到一个文件中
#         :param mode:
#         :param logs:
#         :return: 写入成功
#     """
#     if 'w' in mode:
#         with open('log.txt', mode=mode, encoding='utf-8') as file:
#             file.writelines(logs)

#     if 'r' in mode:
#         with open('log.txt', mode=mode, encoding='utf-8') as file:
#             print(file.readlines())
#     if 'a' in mode:
#         with open('log.txt', mode=mode, encoding='utf-8') as file:
#             file.writelines(logs)
#     return '输入的mode是{},文件已经执行完成'.format(mode)


# print(write_file('r', my_logs))

# str1='abcd'
# if 'a' in str1:
#     print('a in str1')
# else:
#     print('a not in str1')


# def sum(a, b, c): return (a + b) * c


# print(sum(1, 2, 4))
# python中的匿名函数
# lambda
# lambda 关键字后面跟的是这个函数的入参
# lambda ：后面表达的是这个函数的返回结果


def recurtion(a, b): return {key: value for key, value in zip(a, b)}
# recurstion 是一个将两个元组或列表转换成字典的匿名函数


# name = ('liuhua', 'zhaoyang', 'jiahao', 'jindi')
# city = ['北京', '上海', '重庆', '济南']
# print(recurtion(name, city))


def recurs(a, b):
    return {key: value for key, value in zip(a, b)}


def sum(a, b):
    return a + b


# print(recurs(name, city))
# print(sum(3, 4))


# def sum(a, b): return a + b
# 写一个计算器
# 这个计算器接受不确定个数的参数
# 他接受一个seq参数， 这个参数代表 + - * /
# 通过seq参数 将所有输入进来的参数进行对应操作 / 不做处理返回错误信息


def 计算器(*args, seq='+'):
    if seq == '+':
        # index = 0
        # sum_count = 0
        # while index <= len(args) - 1:
        #     sum_count += args[index]
        #     index += 1
        # return sum_count
        sum, sum_re = args[0], args[1::]
        for num in sum_re:
            sum += num
        return sum
    if seq == '-':
        head, foot = args[0], args[1::]
        for num in foot:
            # print(foot)
            # print(num)
            head -= num
        return head
    if seq == '*':
        res = 1
        for num in args:
            res *= num
        return res
    return '除法暂时不做处理'


print(计算器(1, 2, 3, 4, 5, seq='+'))
