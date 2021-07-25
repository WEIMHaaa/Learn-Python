#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/7/25 9:12
"""


def dict():
    dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    print("dict['Name']: ", dict['Name'])

    dict['Age'] = 8
    print("修改dict", dict['Age'])

    dict['School'] = "霍格沃茨魔法学院"
    print("添加dict", dict['School'])

    # del dict['Name']  # 删除键 'Name'
    # dict.clear()  # 清空字典
    # del dict  # 删除字典

    print("字典长度：", len(dict))
    print("输出字典：", str(dict))


if __name__ == '__main__':
    dict()
