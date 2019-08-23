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

    for k in range(len(arr)):
        print('{:>5}'.format(arr[k]), end='\t')
    print('\n')
    return end_time-start_time


if __name__ == '__main__':

    arr = [random.randint(1, 10000) for i in range(300)]
    print(dubbuleSort(arr))
