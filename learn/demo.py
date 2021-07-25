#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/5/23 8:49
"""

from os import path

# 合并两个字典：可以通过**符号解压字典，并将多个字典传入{}中，实现合并
from sys import path


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def merge():
    # 两个字典
    dict1 = {"name": "Joy", "age": 25}
    dict2 = {"name": "Joy", "city": "New York"}
    dict3 = Merge(dict1, dict2)
    print(dict3)


# 重复打印字符串
def repeat():
    n = 5
    string = "Hello!"
    print(string * n)


# 查找出现次数最多的元素：使用max方法找出列表中出现次数最多的元素。
def most_frequent(list):
    return max(set(list), key=list.count)

def most_frequent_exemple():
    mylist = [1, 1, 2, 3, 4, 1, 5, 6, 6, 2, 2]
    print("出现次数最多的元素是:", most_frequent(mylist))


if __name__ == '__main__':
    # merge()
    # repeat()
    most_frequent_exemple()
