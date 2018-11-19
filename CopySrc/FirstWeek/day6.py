#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-16 18:07:39
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
import random
import string

# import day5
# # from FirstWeek.ForthDay import SouceCode   # import module
# # import FirstWeek    # import packages
#
# # module: python中，每个单独的文件， 代表一个module
# # packages : pip install requests  python site-packages/requests/， 每个文件夹代表packages

# numbers = list(range(1, 100))
# print(random.choice(numbers))  # random.choice 接受一个可迭代的对象， 从对象中随机取出一个元素， 并返回
# # random.randint 接受2个参数，一个是起始点， 一个是结束点， 从这两个点之间(包含这两点)随机返回一个int类型的值
# print(random.randint(1, 99))
# print(random.sample(numbers, 8))
# # random.sample 接受2个参数， 第一个参数为可迭代的对象，第二个参数为返回这个对象中的几个元素，返回列表类型
# print([item for item in dir(string) if not item.startswith('__')])
# print(numbers)
# random.shuffle(numbers)
# print(numbers)

# print(string.ascii_letters)
# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)


# numbers = list(string.digits)
# random.shuffle(numbers)  # 打乱列表顺序
# print(numbers)
# headers = ['138', '139', '140', '131', '155', '157']
# mobile_number = random.choice(headers) + ''.join(random.sample(numbers, 8))
# # random.randint 接受2个参数，一个是起始点， 一个是结束点， 从这两个点之间(包含这两点)随机返回一个int类型的值
# print(mobile_number)

# num = 8 #生成几位邮箱前缀
# footer = ['@163.com', '@qq.com', '@yahoo.com', '@126.com']
# header = ''.join(random.sample(
#     list(string.digits + string.ascii_letters), num))
# email = header + random.choice(footer)
# print(email)

# 生成一个随机的8为密码，包含大小写，包含特殊符号
# numbers = list(string.digits + string.ascii_letters + string.punctuation)
# print(string.punctuation)
# random.shuffle(numbers)
# print(''.join(random.sample(numbers, 8)))

# 生成一个随机的四位数，四位数字不相等
# 然后让用户猜，猜对，则退出游戏
# 如果持续猜错，则累加错误次数，当错误次数达到10次，退出游戏

# number = random.sample(string.digits, 4)  # random.sample 不重复的
# print(number)
# success_number = 0
# fail_number = 0
# while 1:
#     user = input('请输入这不相同的4个数字：')  # 重构可以增加类型校验,仅限输入数字
#     # 用isdigit函数判断是否数字，isalpha判断是否字母，isalnum判断是否数字和字母的组合
#     if not user.isdigit():
#         print('你输入的不是纯数字，请重新输入')
#     else:
#         user = list(user)
#         if user == number:
#             success_number += 1
#             print("恭喜你！回答正确，退出游戏!")
#             break
#         else:
#             print("正糟糕！猜错了！")
#             fail_number += 1
#         if fail_number == 10:
#             print('回答错误次数达10次，退出游戏!')
#             break


if __name__ == '__main__':
    def make_a_mobile():
        # """
        #     doc string
        #     :return
        # """
        # # print('numbers {}'.format(st))
        number = list(string.digits)
        random.shuffle(number)
        headers = ['138', '139', '140', '131', '155', '157']
        mobile_number = random.choice(
            headers) + ''.join(random.sample(number, 8))
        # print(mobile_number)
        return mobile_number

    def hi(name):
        """
            这个函数接受一个必填参数
            param name 这是一个用户名
        """
        print('Hi {}'.format(name))
        return(name)
        # ’{}‘.format(name) 代表将一个字符串格式化，{}部分由format中的参数来替代
        # format 主要用于字符串格式化

     # apple = give_me_apple('apple')   # None
     # print(apple)

    # def give_me_apple(apple: str) ->str:
    #     if apple:
    #         return apple
    #     return apple * 2
    #     print(apple)
        # 每个函数中，只会出发一个return， return后面的代码将不会被执行
        # print(give_me_apple('a'))
        # 第一种 必传参数 func(a, b) 说明func这个函数默认接受2个必传参数， a和b, 一定要按照正确的顺序写入
        # 第二种 关键字参数 func(a=1, b=2) 说明func函数接受两个keywords参数，可以直接用key=value的形式对参数进行修改, 当前默认值为a=1, b=2

    # def number_sum(a=1, b=2):
    #     print('a+b', a + b)
    # number_sum()

    # def print_user_info(name, age, work):
    #     # str.format,{index}取得是对应的参数index值
    #     print('我是{2}，我今年{1}，我的工作是{0}'.format(name, age, work))

    # print_user_info('test', '33', 'liuhua')

    # user_info = ('IT', '20', 'Raymond')
    # 把这个列表中的每一位元素，拆分开传递给这个函数的必传参数
    # print_user_info(*user_info)

    # user_info = dict(name='Raymond', age=20, work='IT')
    # print_user_info(**user_info)
    # 把这个字典中的每一个key=value 传递给这个函数作为他的keywords参数

    def print_user_info_kwargs(name=None, age=None, work=None):
        """
            这个函数只有一个必填参数 name
            age 和 work可以为空
            :param name:
            :param age:
            :param work:
            :return:
        """
        if not name:
            name = '路人甲'
        if not age:
            age = '20'
        if not work:
            work = '待业'
        print('我是{}，我今年{},我的工作是{}'.format(name, age, work))

    # print_user_info_kwargs()
    # user_dict = dict(name='liuhua', age=30, work='IT')
    # print_user_info_kwargs(user_dict)  # 会把user_dict整体传给name
    # print_user_info_kwargs(**user_dict)

    # def print_user_info(*args, **kwargs):
    #     """
    #     """
    #     if kwargs.get('city'):
    #         print("城市的名字是{}".format(kwargs['city']))
    #     print(args, type(args), len(args))
    #     print(kwargs, type(kwargs))

    # name = 'liuhua'
    # age = 15
    # work = '软件测试工程师'

    # print_user_info(name, age, work, 1, 2, 3, 4, 5, 6,
    #                 7, a=1, b=2, c=2, cc=100, city='上海')
    # print_user_info_kwargs(work=work, name=name, age=age)

    def get_city_dict():
        city_code = [100000, 2100000, 457000]
        city_name = ['北京', '上海', '平顶山']
        # 字典推导式
        return {key: value for key, value in zip(city_code, city_name)}
    # print(get_city_dict())

    def get_city_code(code: int)->str:
        """
            这是一个通过邮编查询城市的函数，接受一个邮编，返回城市信息
        """
        city_dict = get_city_dict()
        print(city_dict)
        return city_dict.get(code, '我也不知道这个城市是哪？')
    # print(get_city_code(2100000))
    # print(get_city_code(1234))

    def get_user_info() -> tuple:
        user_mobile = make_a_mobile()
        num = 8
        footer = ['@163.com', '@qq.com', '@yahoo.com', '@126.com']
        header = ''.join(random.sample(
            string.digits + string.ascii_letters, num))
        user_email = header + random.choice(footer)
        user_password = ''.join(random.sample(
            string.digits + string.ascii_letters + string.punctuation, 8))
        return user_mobile, user_email, user_password

    def print_user_info()->None:
        """
            打印用户信息
            return:
        """

        user_mobile, user_email, user_password = get_user_info()
        print('当前用户的手机号码是：{},邮箱是：{},密码是：{}'.format(
            user_mobile, user_email, user_password))

 #   print_user_info()

    def save_user_info()->None:
        result = []
        text = ('mobile', 'email', 'password')
        for num in range(10):
            userinfo = get_user_info()
            result.append({key: value for key, value in zip(text, userinfo)})
        print(result)
    # save_user_info()


# 写一个函数
# 这个函数要自动生成中文用户名
# 可以指定姓氏，如果没有指定则随机姓氏
# 并返回一个2-3位的随机中文名字

    FIRST_NAME_ENUM = '赵钱孙李周吴郑王'
    LAST_NAME_ENUM = '与玉鱼汪千苗喵'

    def make_user_name(first_name=None)->str:
        if not first_name:
            first_name = random.choice(
                list(FIRST_NAME_ENUM))  # 推荐转成list，尽管str类型同样可行
        # 随机数大于50 rand=2，负责rand=1
        rand = 2 if random.randint(1, 100) > 50 else 1
        # 推荐转成list，尽管str类型同样可行
        last_name = ''.join(random.sample(list(LAST_NAME_ENUM), rand))
        print("用户名是：{}".format(first_name + last_name))
        return first_name + last_name
    make_user_name('刘')
