#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/7/25 9:40
"""
import json


def write_json():
    data = {"name": "张艺兴", "job": "歌手"}
    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def read_json():
    with open('data.json', 'r') as f:
        data = json.loads(f)
        print(data)


if __name__ == '__main__':
    write_json()
    read_json()
