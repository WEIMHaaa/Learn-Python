#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/7/25 16:53
"""


def recur_fibo(n):
    """递归函数
    输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


if __name__ == '__main__':

    # 获取用户输入
    nterms = int(input("您要输出几项? "))

    # 检查输入的数字是否正确
    if nterms <= 0:
        print("输入正数")
    else:
        print("斐波那契数列:")
        for i in range(nterms):
            print(recur_fibo(i))