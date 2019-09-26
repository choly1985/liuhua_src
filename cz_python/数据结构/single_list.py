'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-09-25 10:50:26
@LastEditors: liuhua
'''


class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        cur = self._head
        # cur游标，记录移动节点
        # count记录数量
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素,pos从0开始"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1的位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def search(self, item):
        """查找节点是否存在"""
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 判断是否是头节点
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    ll = SingleLinkList()
    print(dir(ll))
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    ll.append(3)
    ll.add(8)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1, 9)  # 9 8 1 2 3 4 5 6
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3 4 5 6
    ll.travel()
    ll.append(7)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
    ll.remove(100)
    ll.travel()
