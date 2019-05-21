#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-09 09:36:26
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os

dict_new = {}


# def build_dict(dict_key, dcit_value):
#     dict_new[dict_key] = dcit_value
#     return dict_new


# build_dict('深圳', '0755')
# build_dict(None, '020')
# print(dict_new)

# def greet_users(names):
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)

# usernames = ["Hannah", 'ty', 'margot']
# greet_users(usernames)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completd = []
# while unprinted_designs:
#     current_designs = unprinted_designs.pop()
#     print("Print model" + current_designs)
#     completd.append(current_designs)
# print(completd)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Print model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
