'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-09-23 10:07:02
@LastEditors: liuhua
'''
# 1 标识符，关键字
"""
    import keyword
    keyword.kwlist
    if / else / elif / break / continue / for / while / and / or /in / not / is
    /Ture/ False / try / except / finally / as / import / from / def / class / return
    None / global / lambda / with / yield / pass / assert / raise / del ...
"""
# 2  变量、输入、输出
"""
	a = 100 引用

	a = 4
	b = 5

	c = a
	a = b
	b = c

	a = a+b
	b = a-b
	a = a-b

	a,b = b,a
"""
# 3. 字符串、列表、元组、字典、集合、列表生成式、类型转换
"""
"aaa"
	'sdfsdf'

	a = "abcd"
	a[:3]---->"abc"
	a[::-1]---->"dcba"

	[1,2,3,1,1,1]--->增删改查

	(1,2,3,1,1,1)-->只读

	{1,2,3,1,1,1}---->{1,2,3} 集合---元素不重复

	字典---->{key:value, key2:value}

	可变类型：列表、字典、集合
	不可变类型：数字、字符串、元组


	["aa","ddd"]

	{"name":"asdf","age":10}

	[{"name":"xxx","family":[{"小姑":"aa","family":["a","b","cc"]},"bb","ccc"]},{},{}]


	a = [111,22,33,1,111,111,111,343]
	b = set(a)
	c = list(b)
	d = tuple(a)

	"a"+"b"---->"ab"
"""
# 4. 切片
# 顺序、选择、循环
"""
5. if

	if 条件:
		xxxx


	if 条件:
		xxxx
	else:
		xxxx2


	if 条件1:
		xxx1
	elif 条件2:
		xxx2:
	elif 条件3:
		xxxx3
		.....
	else:
		xxxx


	if xxx:
		xxx
		xxx
		xx
		if yyy:
			yyyyy1

6. while

	i = 0
	while i<100:
		xxxx
		xxx
		xxx
		i+=1

	i = 100
	while i>0:
		print(i)
		i-=1

	while True:
		pass


	while xxx:
		while yyy:
			pass

7. for

	a = [111,22,33]
	for i in a:
		xxxxx



8. 各种嵌套


9. 函数、参数、返回值、全局/局部变量、多个return、一个return返回多个值

	def xxx(形参):
		。。。。。
		return 0
		return 1

		....
		return (0,1)
		return [0,1]

	xxx(实参)



	结束一个函数:return
	结束一个循环:break/continue
	结束一个程序:exit()



	def test(a,b,c=100,*args,**kwargs):
		pass

	test(b=11,a=22,100,200,300,400,mm=100,nn=20)


	num = 100
	def test():
		global num
		num=200



10. 类、对象


	class Animal(父类):

		类属性
		num = 100

		实例方法
		def __init__(self):
			self.xxx = 100 实例属性
			父类名字.父类方法(self)
			super().父类的方法名()
			super(当前类的名字Animal,self).父类的方法名()

		实例方法
		def tset(self):
			Animal.num = 300

		类方法
		@classmethod
		def xxx(cls):
			cls.num = 200

		静态方法
		@staticmethod
		def yyy():
			pass




	a = Animal()
	b = a

	del a----->不会调用__del__
	del b----->调用__del__方法


11. 异常


	try:

		xxxx

	except 异常的名字:
		异常的处理。。。。
	else:
		没有异常的时候执行
	finally:
		不管有没有产生异常，都会执行

12. 模块、包

	import 模块、包xxxx
	xxxx.功能()

	from 模块 import test1,test2
	test1()

	from .... import *

	if __name__ =="__main__":
		xxx
"""




import sys
import string
import os
import random
def sum_2_nums(a, b, c=22, *args, **kwargs):
    print(a, b, c, args, kwargs)


# A = (44, 55, 66)
# B = {'name': "laowang", "age": 20}
# sum_2_nums(1, 11,  22, A, B)

def count_input():
    a = input("请输入数字：")
    b = input("请输入数字:")
    return int(a) + int(b)


def show_info():
    print("=" * 40)
    print("=" + " " * 10 + "欢迎进入到身份认证系统V1.0")
    print("= 1. 登录")
    print("= 2. 退出")
    print("= 3. 认证")
    print("= 4. 修改密码")
    print("=" * 40)


# print(count_input())
# show_info()

def get_person_info():
    person_name = input("请输入姓名：")
    person_qq = input("请输入qq:")
    person_tel = input("请输入电话号码:")
    person_addr = input("请输入住址:")
    print("=" * 40)
    print("姓名：%s" % (person_name))
    print("QQ ：%s" % (person_qq))
    print("手机号：%s" % (person_tel))
    print("公司地址：%s" % (person_addr))


# get_person_info()
name = 'hello world ha ha'
# print(name.split(" "))
# print(name.capitalize())
# print(name.title())
# print(name.startswith('hello'))
# print(name.startswith('Hello'))
# print(name.endswith('ha'))
# print(name.endswith('Ha'))
# print(name.upper())
# print(name.lower())

# li = ('my', 'name', 'is', 'liuhua')
# print(' '.join(li))
# a = [1, 4, 3, 2, 1]
# sorted(a)
# print(a)

# offices = [[], [], []]
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# for name in names:
#     index = random.randint(0, 2)
#     offices[index].append(name)
# i = 1
# for tempNames in offices:
#     print("办公室%d人数为:%d" % (i, len(tempNames)))
#     i += 1
#     for name in tempNames:
#         print("%s" % name, end=' ')
#     print("\n")
#     print("-"*20)

name_info = {"liuhua": "hengyang", "liuhua1": "yueyang"}
# print(name_info.get("liuhua"))
# print(name_info.setdefault("liuhua3", "hello"))
info = {'liuli1': "beijing", "yiping": "changsha", "liuhua": "hengyang1"}
# name_info.update(info)
# print(name_info)
# del(name_info)
# print(name_info)


# tuple1 = [(2, 3), (4, 5)]
# print(tuple1[0][1])


# def print_info(**kwargs):
#     for item in kwargs.items():
#         print(item)
# print_info(**info)

def calNum(num):
    if num >= 1:
        result = num * calNum(num - 1)
    else:
        result = 1
    return result


def read_file(file):
    f = open(file, 'r')
    for line in f.readlines():
        if not line.startswith("#"):
            print(line.rstrip())
    f.close()


# read_file(r"C:\Users\liuhua2\Desktop\test.txt")


# def read_file_new(file):
#     with open(file, 'r') as f:
#         for line in f.readlines():
#             if (not line.rstrip().startswith("#")) and (not line.rstrip().endswith("#")):
#                 print(line.rstrip())
#             # if not line.rstrip().startswith("#"):
#             #     if not line.rstrip().endswith("#"):
#             #         print(line.rstrip())


# read_file_new(r"C:\Users\liuhua2\Desktop\test.txt")
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = map(lambda x, y: x+y, l1, l2)
# print(list(l3))

# a = {1, 2, 3, 4}
# b = {4, 5, 6, 7}
# print(a & b, a | b, a ^ b, a-b)

# print("\n".join("\t".join(["%s*%s=%s" % (x, y, x*y)
#                            for y in range(1, x+1)]) for x in range(1, 10)))

# while True:
#     player = int(input("请输入剪刀(0),石头(1)，布(2) :"))
#     computer = random.randint(0, 2)
#     if (player == 1 and computer == 0) or (player == 2 and computer == 1) or (player == 0 and computer == 2):
#         print("赢了")
#     elif player == computer:
#         print("平了")
#     elif player not in range(0, 3):
#         print("输入有误")
#     else:
#         print("输了")

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# s = input("请输入一行字符：")
# letter_count = 0
# digit_count = 0
# other_count = 0
# for c in s:
#     if c.isalpha():
#         letter_count += 1
#     elif c.isdigit():
#         digit_count += 1
#     elif c in string.punctuation:
#         other_count += 1
#     else:
#         pass
# print(letter_count, digit_count, other_count)

# a = 'dabcb'
# if a in 'abdabcbcd':
#     print(1)

# keys = ('狗子', '港', 'DAYDREAM')
# values = ('dog', 'gang', 'day')
# user_dict = {key: value for key, value in zip(keys, values)}
# print(user_dict)
# print(user_dict.setdefault('狗子1', 'dog2'))
# print(user_dict)

news = {'beijing': '北京', 'xian': "西安"}

# if news.get('beijing'):
#     print(news['beijing'])
# else:
#     print('北京不在字典中')
# news.popitem()
# print(news)

# userinfo = ['刘德华', '黎明', 'Raymond', 'dog', '随便', '牛仔']
# username = '牛仔1'
# num = 0
# for user in userinfo:
#     if user == username:
#         print('username 在 userinfo中')
#         break
#     elif num == len(userinfo)-1:
#         print('不存在userinfo中')
#     num += 1

# foot = ['@qq.com', '@163.com', '@hotmail.com', '@gmail.com']
# email = ''.join(random.sample(string.ascii_letters +
#                               string.digits, 8)) + random.choice(foot)

# for i in range(10):
#     email = ''.join(random.sample(string.ascii_letters +
#                                   string.digits, 16)) + random.choice(foot)
#     print(email)

# mobile_head = ['132', '133', '159', '181', '138', '180']
# for i in range(1000):
#     mobile = random.choice(mobile_head)+str(random.randint(10000000, 99999999))
#     print(mobile)

# 随机出一个数字
# 让用户去猜
# 如果用户持续猜错 可以选择继续猜，或者通过ctrl + c的方式结束游戏
# 如果用户猜对了， 则自动退出
# 如果错误， 则重新猜

# user_input_list = []
# while 1:
#     rand = random.randint(1, 11)
#     user = input('请输入一个数字:')
#     try:
#         user = int(user)
#         if user_input_list.count(user) >= 5:
#             print('该数字输入5次，不可继续输入啦！')
#             continue
#         if rand == int(user):
#             print('恭喜你，猜对了！游戏退出')
#             break
#         else:
#             user_input_list.append(user)
#             print('user : {}'.format(user), 'comp :{}'.format(rand))
#             print('猜错了哦， 继续加油， 或者 CTRL+C退出游戏！')
#     except KeyboardInterrupt:
#         sys.exit(0)
#     except ValueError:
#         print('输入类型错误， 只接受int类型的参数')

# number = random.sample(string.digits, 4)
# print(number)
# success_number = 0
# fail_number = 0
# while 1:
#     if success_number == 3 or fail_number == 10:
#         print('退出游戏！')
#         break
#     user = list(input('请输入这不相同的4个数字：'))
#     if user == number:
#         success_number += 1
#         print('恭喜你！回答正确')
#     else:
#         print('真糟糕！猜错了！')
#         fail_number += 1


# def print_user_info(name, age, work):
#     """
#         这个函数，接受三个必传参数，把他们拼接成一句话，不错返回
#     :param name: 用户名
#     :param age: 用户年龄
#     :param work: 用户的工作
#     :return: None
#     """
#     print('我是{}，我今年{}，我的工作是{}'.format(name, age, work))


# user_info = ('Raymond', 20, 'IT')
# print_user_info(*user_info)
# user_info = dict(name='Raymond', age=20, work='IT')
# print_user_info(**user_info)


FIRST_NAME_ENUM = '赵钱孙李周吴郑王'
LAST_NAME_ENUM = '与玉鱼汪千苗喵'


# def make_user_name(first_name=None) -> str:
#     """
#         生成一个随机的用户名
#     :return:
#     """
#     if not first_name:
#         first_name = random.choice(list(FIRST_NAME_ENUM))

#     rand = 2 if random.randint(1, 100) > 50 else 1
#     last_name = ''.join(random.sample(list(LAST_NAME_ENUM), rand))
#     print('用户名是 ：{}'.format(first_name + last_name))
#     return first_name + last_name

# make_user_name('上官')
# for i in range(10):
#     print('*'*10) if random.randint(1, 10) < 5 else print("-"*10)


# file = open('log.txt', mode='a', encoding='utf-8')
# file.writelines(['\n我是整行写入的', '\n我想在这行再加一些备注'])
# file.writelines(['\n我是第二个整行', '\n好吧我觉得我没什么写的了就是想在这里占一个位置'])
# file.close()

# string_text = '我是雷蒙德！'
# print('string text ', string_text, type(string_text))
# bytes_text = string_text.encode()   # str => bytes
# print('bytes_text ', bytes_text, type(bytes_text))
# bytes2string = bytes_text.decode()   # bytes => str
# print(bytes2string)

# with open('log.txt', mode='rb') as file:
#     data = file.read()
#     # print(file.read())   # 这里会返回一个空的bytes类型的数据，因为file.read()只会返回一次数据，返回后数据被消费掉
# # print(data.decode('gbk')) #gbk会报错
# file_text = data.decode()
# print(file_text)


# with open('log.txt', mode='r', encoding='utf-8') as file:
#     data = file.readlines()  # file.readlines() 返回一个完整的文件内容的列表，每一行用’，‘分割
#     for line, item in enumerate(data, 1):
#         print(line, item.replace('\n', ''))

# def sum1(start=1, *args):
#     print(start)
#     return start+sum(args)


# print(sum1(2, 2, 3, 4, 5, 6, 7, 8, 9))

# def 计算器(*args, seq='+'):
#     """
#         这是一个制作一种运算的计算器
#     :param args:
#     :param seq:
#     :return:
#     """
#     if seq == '+':
#         return sum(args)
#     if seq == '-':
#         head, foot = args[0], args[1::]
#         for num in foot:
#             head -= num
#         return head
#     if seq == '*':
#         res = 1
#         for num in args:
#             res *= num
#         return res
#     return '除法暂时不做处理'


# print(计算器(5, 5, 3, 3, seq='*'))


"""
# 实现一个构造测试数据的类
# 这个类能生成指定号段的手机号码
# 这个类能生成随机中文名字， 可指定生成名字的姓氏和长度
# 这个类可以生成一共用户信息的字典， 该用户信息字典包含 用户中文名 密码 邮箱 手机号 创建这条数据的时间
# 将用户信息存储到用户文件夹下
# 定义repr 查看对应类实例对象的基础信息
"""



import json
import random
import string
import time
import os


class Datas:
    """ 这是一个构造测试数据的类"""

    def __init__(self, mobile_number_head=None, first_name_head=None, name_lenth=None):
        """
        初始化Datas类并接受必要的入参
        :param mobile_number_head: 指定的手机号段
        :param first_name_head: 指定的姓
        :param name_lenth: 指定用户名的长度
        """
        self.mobile_head = mobile_number_head
        self.first_name = first_name_head
        self.name_lenth = name_lenth
        self.save_json_file_path = 'Users'
        self.return_title = 'Datas<{}>'
        self.func_args = [item for item in dir(self) if not item.startswith(
            '__') and callable(getattr(self, item))]


    def write_file(self, file_name, data):
        """ 讲文件写入Users路径"""
        file_name = '{}/{}/{}.json'.format(os.path.dirname(__file__),self.save_json_file_path, file_name)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(data)

    def make_user_json_and_write_file(self):
        """
            将随机生成的用户信息， 存储进文件
        :return:
        """
        titles = ('中文名', '密码', '手机号', '邮箱', '创建时间')
        name = self.make_user_name()

        infos = (
            name,
            self.make_random_password(),
            self.mobile(),
            self.make_user_email(),
            time.strftime('%Y-%m-%d %H:%M:%S')
        )
        data = json.dumps({key: value for key, value in zip(
            titles, infos)}, ensure_ascii=False, indent=4)
        self.write_file(name, data)
	
    def make_random_password(self):
        """
            创建一个随机的用户密码
        :return:
        """
        return ''.join(random.sample(string.digits + string.ascii_letters + string.punctuation, 8))

    def make_user_email(self):
        """
        :return:
        """
        buf = ['@163.com', '@qq.com', '@gmail.com', '@yahoo.com']
        head = random.sample(string.ascii_letters + string.digits, 8)
        email = ''.join(head) + random.choice(buf)
        return email

    def make_user_name(self) -> str:
        """
        生成一个随机的用户名
        return:
        """
        if not self.first_name:
            self.first_name = random.choice(list(FIRST_NAME_ENUM))
        if not self.name_lenth:
            self.name_lenth = 2 if random.randint(1, 100) > 50 else 1

        last_name = ''.join(random.sample(
            list(LAST_NAME_ENUM), self.name_lenth))
        print('用户名是 ：{}'.format(self.first_name + last_name))
        return self.first_name + last_name

    def mobile(self):
        """ 生成一个指定号段的手机号， 如果没有指定则随机返回一个号段的手机号"""
        if self.mobile_head:
            try:
                self.mobile_head
            except Exception as err:
                return err

        if self.mobile_head and len(list(self.mobile_head)) == 3:
            return self.mobile_head + ''.join(random.sample(list(string.digits), 8))
        mobile = ['137', '138', '139', '131', '140', '150', '177']
        return random.choice(mobile) + ''.join(random.sample(list(string.digits), 8))

    def __repr__(self):
        """
           pass
        :return:
        """
        return 'Datas(<{}>)'.format(self.func_args)


class InterfaceTest(Datas):
    def __init__(self):
        super(InterfaceTest, self).__init__()
        print(self.mobile())
        print(self.make_user_name())



class PythonStudent(object):

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.titles = ('用户名', '年龄', '城市')

    def __repr__(self):
        userinfo = (self.name, self.age, self.city)
        user_dict = {key: value for key, value in zip(self.titles, userinfo)}
        user_json = json.dumps(user_dict, ensure_ascii=False, indent=4)
        
        with open('{}/Users/{}.json'.format(os.path.dirname(__file__),self.name), 'w') as file:
            file.write(user_json.en)
        return "数据存储完成，存储文件是{}.json".format(self.name)


class MyFristClass(object):
    def __init__(self, name, age, city):
        self.log = True
        self.__name = name
        self.__age = age
        self.__city = city

    def __repr__(self) -> str:
        if '_MyFristClass__name' in dir(self):
            return '我的名字:{},我的年龄{},我在{},当前的log信息状态为{}'.format(
                self.__name, self.__age, self.__city, self.log)
        return 'user info is not define ...'

    def reset_name(self, new_name):
        self.__name = new_name

    def del_all_info(self):
        del self.__name,self.__age,self.__city,self.log		

class People:
    def __init__(self, name, age, city, work):
        self.users = name, age, city, work
        self.title = ('name', 'age', 'city', 'work')

    def get_user_info(self):
        return json.dumps({key: value for key, value in zip(self.title, self.users)}, indent=4, ensure_ascii=False)


class Worker(People):
    """ 这是一个工人的类"""

    def __init__(self):
        self.users = 'Raymond', 20, '北京', '工人'
        super(Worker, self).__init__(*self.users)

class Teacher(People):
    def __init__(self, name, age, city):
        self.work = 'teacher'
        super(Teacher, self).__init__(name, age, city, self.work)


from abc import ABCMeta
from abc import abstractmethod

class Animal(metaclass=ABCMeta):
    def __init__(self, animal_name):
        pass

    @abstractmethod
    def call(self):
        raise NotImplemented
class Dog(Animal):
    def __init__(self, animal_name):
        super(Dog,self).__init__(animal_name)

    def call(self):
        print('汪汪汪！')

class 搞事情(object):
    def __init__(实例对象, *搞事情的不确定参数, **搞事情的关键字参数):
        实例对象.不确定参数元祖 = 搞事情的不确定参数
        实例对象.不确定关键字字典 = 搞事情的关键字参数
        实例对象.打印 = print
    def 遍历不确定参数元祖(实例对象):
        for 参数 in 实例对象.不确定参数元祖:
            实例对象.打印(参数)

    def 遍历字典中的元素(实例对象):
        for 关键字, 值 in 实例对象.不确定关键字字典.items():
            实例对象.打印(关键字, 值)



if __name__ == '__main__':
    # datas = Datas('1459')
    # datas.make_user_json_and_write_file()
    # print(datas)
    # print(dir(datas))
    # interface = InterfaceTest()
    # user_infos = [
    #     ('Gang', 18, '上海'),
    #     ('随便', 30, '俄罗斯'),
    #     ('Raymon', 20, '北京'),
    #     ('狗子', 5, '新加坡'),
    #     ('年华', 25, '上海'),
    #     ('思', 30, '马来西亚')
    # ]
    # for user in user_infos:
    #     class_instance = PythonStudent(*user)
    #     print(class_instance)

    # user = MyFristClass(*user_infos[-2])
    # print(user)
    # user.reset_name('行者')
    # print(user)
    # user.del_all_info()
    # print(user)
    # worker = Worker()
    # print(worker.get_user_info())
    # teacher = Teacher('茶茶', 35, '上海')
    # print(teacher.get_user_info())
    # dog1 = Dog('旺财')
    # dog1.call()

    搞 = 搞事情(1, 2, 3, 4, 5, 6, abc=123, bcd='123', abcd='1234')
    搞.遍历不确定参数元祖()
    搞.遍历字典中的元素()
