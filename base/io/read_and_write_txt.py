#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/7/25 9:40
"""
import json


def write_txt():
    with open('../../files/data.txt', 'w') as f:
        f.write("我是txt啊")


def read_txt():
    with open('../../files/data.txt', 'r') as f:
        str = f.read()
        print(str)


if __name__ == '__main__':
    # write_txt()
    read_txt()
