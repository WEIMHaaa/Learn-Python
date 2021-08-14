#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/8/14 8:50
"""

import socket as f
import json
from urllib.request import urlopen
import ssl

def get_hostname():
    hostn = f.gethostname()
    Laptop = f.gethostbyname(hostn)
    print("你的电脑本地IP地址是：" + Laptop)
    # 全局取消证书验证
    ssl._create_default_https_context = ssl._create_unverified_context
    with urlopen(r'https://jsonip.com') as fp:
        content = fp.read().decode()

    ip = json.loads(content)['ip']
    print("你的电脑公网IP地址是：" + ip)


if __name__ == '__main__':
    get_hostname()