"""
@Author  : weimenghua
@Time    : 2020/9/20 8:38
"""

import requests

# get请求
get_resp = requests.get('https://omstest1.tc-lawtech.com/')
# 设置编码
get_resp.encoding = 'utf-8'
print(get_resp.text)

post_resp = requests.post('https://omstest1.tc-lawtech.com/')