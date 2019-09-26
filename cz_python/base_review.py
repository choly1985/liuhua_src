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
print(name.upper())
print(name.lower())

li = ('my', 'name', 'is', 'liuhua')
print(' '.join(li))
a = [1, 4, 3, 2, 1]
sorted(a)
print(a)
