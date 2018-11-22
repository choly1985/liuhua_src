#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-22 23:07:19
# @Author  : liuhua (434375025@qq.com)
# @Link    : https://github.com/choly1985
# @Version : $Id$

import os
import json
from abc import ABCMeta
from abc import abstractmethod


class Fruits(metaclass=ABCMeta):
    """这是一个水果的父类"""

    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def throw(self):
        pass

    @abstractmethod
    def throw(self):
        pass

    @abstractmethod
    def sell(self):
        pass

    def param(self):
        pass


class Apple(Fruits):
    def buy(self):
        print('购买一个苹果')

    def sell(self):
        print('卖掉一个苹果')

    def throw(self):
        print('这个苹果坏了，扔掉它')


class Banana(Fruits):
    def buy(self):
        print('购买一个香蕉')

    def sell(self):
        print('卖掉一个香蕉')


class People(object):
    def __init__(self, name, age, city, work):
        self.users = name, age, city, work
        self.title = ('name', 'age', 'city', 'work')

    def get_user_info(self):
        return json.dumps({key: value for key, value in zip(self.title, self.users)}, indent=4, ensure_ascii=False)


class Teacher(People):
    def __init__(self, name, age, city):
        self.work = 'teacher'
        super(Teacher, self).__init__(name, age, city, self.work)
        # super初始化父类


class Student(People):
    def __init__(self, name, age, city):
        self.work = 'student'
        super(Student, self).__init__(name, age, city, self.work)


class Worker(People):
    def __init__(self):
        self.users = 'Raymond', '20', '北京', '工人'
        super(Worker, self).__init__(*self.users)


class Duck(object):
    """Duck class"""

    def __init__(self, _quack, _fly):
        self._quack = _quack
        self._fly = _fly
        self.type = '真'

    def swim(self):
        print("swiming ...!")

    def display(self):
        print(self._quack)
        print(self._fly)
        self.swim()
        return '我是一只{}的鸭子'.format(self.type)


class GreenDuck(Duck):
    def __init__(self):
        super(GreenDuck, self).__init__(None, None)
        self._quack = '我会叫'
        self._fly = '我会飞'
        self.type = '绿头'

    def green_quack(self):
        return 'gua gua gua'


class RubberDuck(Duck):
    """ 橡皮鸭子 """

    def __init__(self):
        self._quack = '我不会叫'
        self._fly = '我不会飞'
        super(RubberDuck, self).__init__(self._quack, self._fly)
        self.type = '橡皮'

    def swim(self):
        print('橡皮鸭漏气了，不会游泳了')
        return '我不能游泳了'


class DecoyDuck(RubberDuck):
    """诱饵鸭子"""

    def __init__(self):
        super(DecoyDuck, self).__init__()
        self.type = '诱饵'


if __name__ == '__main__':

    # fruits = Fruits() #TypeError抽象类无法被实例化
    # apple = Apple()
    # apple.buy()
    # apple.throw()
    # apple.sell()

    # worker = Worker()
    # print(worker.get_user_info())
    # # 继承父类的方法

    # teacher = Teacher('茶茶', '33', '上海')
    # print(teacher.get_user_info())

    # students = [
    #     ('gang', 18, 'chengdu'),
    #     ('随便', 20, '平顶山'),
    #     ('大哥', 19, '厦门')
    # ]

    # for student in students:
    #     st = Student(*student)
    #     print(st.get_user_info())

    # green = GreenDuck()
    # print(green.display())
    # green.swim()
    # print(green.green_quack())

    # duck = Duck('我会叫', '我会飞')
    # print(duck.display())
    # print('=============')
    # rubber = RubberDuck()
    # # print(duck.display())
    # print(rubber.display())  # display 是由父类实现,父类调用类方法看在子类中有无，有用子类方法
    # print(rubber.swim())

    decoy = DecoyDuck()
    print(decoy.display())
