#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/7/25 9:00
"""

"元组的不可变指的是元组所指向的内存中的内容不可变。"


def tuple():
    tup = ("张艺兴", "白敬亭", "王嘉尔")
    print(tup[0])
    print(tup[1:3])  # 注：不包含索引3

    tup[0] = "张加帅"  # 不支持修改元素


if __name__ == '__main__':
    tuple()
