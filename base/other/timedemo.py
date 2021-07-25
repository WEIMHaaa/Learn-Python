#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/7/25 10:04
"""

import time


def timedemo():
    ticks = time.time()
    print("当前时间戳：", ticks)

    localtime1 = time.localtime(time.time())
    print("本地时间：", localtime1)

    localtime2 = time.asctime(time.localtime(time.time()))
    print("本地时间：", localtime2)

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))


if __name__ == '__main__':
    timedemo()