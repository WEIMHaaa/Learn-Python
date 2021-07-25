#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/7/25 17:17
"""


def jishu_and_oushu():
    num = int(input("请输入一个数字："))
    if (num % 2) == 0:
        print("{}是偶数".format(num))
    else:
        print("{}是奇数".format(num))


if __name__ == '__main__':
    jishu_and_oushu()
