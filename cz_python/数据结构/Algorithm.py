'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-08-22 12:50:47
@LastEditors: liuhua
'''

import random
import time
import string
import sys
import os


def dubbuleSort(arr):
    '''
    @description: 冒泡排序
    @param: 入参一个待排序列表
    @return: 运行时间
    @author: liuhua
    '''
    start_time = time.clock()
    __len = len(arr)
    for i in range(__len-1):
        for j in range(1, __len - i):
            if arr[j - 1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    end_time = time.clock()
    print('\n')
    return end_time-start_time


def qucik_sort1(arr, left, right):
    '''
    @description: 快速排序，一次比较arr[0]和其他元素，比arr[0]小，就原地删除
    ，然后插入到arr[0]前面，基准值后移，大于等于则不处理。然后递归
    @param 接受3个参数，待排序列表，左右基准
    @return: 函数无返回值
    @author: liuhua
    '''
    # 退出函数递归
    if left >= right:
        return

    flag = left
    for i in range(left + 1, right + 1):
        if arr[flag] > arr[i]:
            temp = arr[i]
            del arr[i]
            arr.insert(flag, temp)
            flag += 1
    qucik_sort1(arr, left, flag - 1)
    qucik_sort1(arr, flag+1, right)


def quick_sort2(alist, start, end):
    """快速排序"""
    if start >= end:
        return
    # 基准
    mid = alist[start]
    # 左边游标
    left = start
    # 右边游标
    right = end

    while left < right:
        while left < right and alist[right] >= mid:
            # 右边游标移动，左边游标不动
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] < mid:
            # 左边游标移动，右边游标不动
            left += 1
        alist[right] = alist[left]
    # 退出循环后 left与right重合，即相等
    alist[left] = mid
    # 递归的方式排左边的序列
    quick_sort2(alist, start, left - 1)
    # 递归的方式排右边的序列
    quick_sort2(alist, left + 1, end)


def shell_sort(arr: list):
    '''
    @description: 希尔排序，缩小增量排序，是直接插入排序算法的一种更高效的改进版本希尔排序是把记录按下标的一定增量分组，
    对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
    @param {type} 接受待排序序列
    @return: None
    @author: liuhua
    '''
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap //= 2


if __name__ == '__main__':
    # arr = [random.randint(1, 50000) for i in range(10000)]
    # print(dubbuleSort(arr))
    # print('\n')
    list = [''.join((random.sample(string.ascii_letters+string.digits+string.punctuation, 1)))
            for i in range(10)]
    arr = [random.randint(1, 1000000) for i in range(1000000)]
    # start_time = time.clock()
    # quick_sort2(arr, 0, len(arr) - 1)
    # arr.sort()
    # sorted(arr)
    # shell_sort(list)
    # end_time = time.clock()
    # 超大数打印费时间
    # for k in range(len(arr)):
    #     print('{:>5}'.format(arr[k]), end='\t')
    # print('\n')
    # print(end_time-start_time)
    # print(list)
    # print(os.path.split(os.path.abspath(__file__))[0])  # 获取本文件所在目录,并打印
    # print(os.path.split(os.path.realpath(__file__))[0])  # 获取本文件所在目录，并打印
    # print(os.path.abspath(__file__))  # 获取本文件绝对路径，并打印
    # print(os.path.dirname(__file__))  # 获取本文件所在目录，并打印
    # print(os.path.dirname(os.path.realpath(__file__)))  # 获取本文件所在目录，并打印
    # filePath, fileName = os.path.split(os.path.abspath(__file__))#获取当前文件目录，文件名
    # print(filePath, fileName, sep='\t')
