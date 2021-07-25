#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/7/25 17:07
"""


def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':

    arr = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(arr)
    for i in range(len(arr)):
        print("排序后:", "%d" % arr[i])