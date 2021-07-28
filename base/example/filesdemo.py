#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/7/28 14:33
"""
import os


def list_dir():
    # os.scandir()则获取当前路径
    for item in os.scandir("D:\\"):
        print(item.name, item.is_dir(), item.stat(), item.path)


def mkdir():
    os.mkdir("新文件夹名称")  # 创建单层文件夹；
    os.makedirs("第一层/第二层/第三层") #创建多层文件夹；
    list1 = ["文件夹{}".format(i) for i in range(5)]
    for i in list1:
        os.mkdir(i)


if __name__ == '__main__':
    list_dir()
    # mkdir()