'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-09-25 10:24:23
@LastEditors: liuhua
'''


class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列尾部添加一个item元素
        (可以出栈入栈操作根据需要调整添加和删除元素从队尾还是队头)"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty():
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


class Deque(object):
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队列头部添加一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """往队列尾部添加一个item元素"""
        self.__list.append(item)

    def pop_rear(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def pop_front(self):
        """从队列尾部删除一个元素"""
        return self.__list.pop()

    def is_empty():
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
