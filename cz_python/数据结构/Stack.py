'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-09-25 10:05:24
@LastEditors: liuhua
'''


class Stack(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            None

    def is_empty(self):
        """判断栈顶是否为空"""
        return self.__list == []
        # return not self.__list

    def size(self):
        """返回栈顶的元素个数"""
        return len(self.__list)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    a = 1
    print('a', 'b')
