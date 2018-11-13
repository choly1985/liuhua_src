#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-13 16:16:31
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

from keyword import kwlist
import sys
if __name__ == '__main__':
    print('hello world!')
    print(123456)
    print('abcd1234', end='')
    print('a', 'b', 'c', end='++++++++++')
    print(1, 2, 3, end='\t')
    print(1 + 2)
    print('a' + 'b')
    print(True and False)
    print(123.456)
    print(abs)
    print('1')

    string = '1234'
    integer = 1234
    _float = 123.456
    _bool = True
    func = print
    _list = ['1234', abs, 1234, True, 1234]

    _list[2] = 666
    print(type(string), type(integer), type(_float), type(_list))

    _tuple = ('1234', abs, 1234, True, 1234)

    _set = {'1234', abs, 1234, True, 1234}
    _dict = {'key': 'value', '北京': '10000'}
    print(_dict)
    print(type(_dict.get('北京')))

    _dict = dict(key=1, 北京=00000)

    # dict.get方法 key需要带引号
    print(type(_dict.get('北京')))
    new_string_text = '11' + "22" + """3333"""
    print(type(new_string_text))
    print(type("True"))
    print(type("print"))
    print('"1234"')
    print('\'1234\'')
    print("""1234""")
    print("\"1234\"")

    print(type(123456))
    print(type(0))
    print(type(-555))
    print(type(99999999999999999999999999999999))
    print(5 / 3 * 2)
    print("500" * 2)

    print(type(1234.56789))
    print(0.0)
    print(type(-123.456))
    print(type(9999999999999999999999999.99999999999999999999))

    print(True or False)
    print(type(True))
    print(type(False))

    print(type(_list), _list)
    print(type(_tuple), _tuple)
    print(type(_set), _set)
    print(type(_dict), _dict)

    if True:
        print("True")
    if type(123) == int:
        print()
    if isinstance(123, int):
        print('yes')
    if not isinstance(123, str):
        print('not')

    print(type(_dict))
    print(isinstance(_dict, dict))
    print(dict)
    print(print)
    userinfo = dict(a='b', c='d')
    print(userinfo)
    print(kwlist)
    _kwlist = ['False', 'None', 'True', 'and', 'as', 'assert',
               'break', 'class', 'continue', 'def', 'del', 'elif',
               'else', 'except', 'finally', 'for', 'from', 'global',
               'if', 'import', 'in', 'is', 'lambda',
               'nonlocal', 'not', 'or', 'pass',
               'raise', 'return', 'try', 'while', 'with', 'yield']
    name = 'liuhua最帅'
    age = 'liuhua 18 岁'
    is_girlfriend = 'liuhua 有女友'
    print(name, age, is_girlfriend, sep=',',
          end='\t', file=sys.stdout, flush=True)
    TAGS = 'Bad Dog'
    print(TAGS)
    TAGS = 's'
    print(TAGS)
