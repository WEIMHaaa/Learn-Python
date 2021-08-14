#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author : weimenghua
@Time   : 2021/7/28 16:10
"""

import requests
import pytest

"""
.py 测试文件必须以test_开头（或者以_test结尾） 
测试类必须以Test开头，并且不能有init方法
测试方法必须以test_开头（或者以_test结尾） 
断言必须使用assert

重试机制：
pip3 install pytest-rerunfailures
使用装饰器 @pytest.mark.flaky(reruns=5, reruns_delay=2) 
reruns ：最大重试次数
reruns_delay ：重试间隔时间，单位是秒
"""

class TestCase:

    @pytest.fixture()
    def before(self):
        print("------->before哈哈")

    @pytest.mark.flaky(reruns=5, reruns_delay=2)
    def test_retry(self):
        assert 0 == 1
        print("重试机制")

    def test_success(self):
        print("断言成功")
        assert 1

    def test_fail(self):
        print("断言失败")
        assert 0

    def test_demo(self):
        url = "http://www.baidu.com"
        resp = requests.get(url=url)
        print(resp.text, resp.status_code)

    def test_result(self):
        url = "https://xna-apitest1.jiuliyuntech.com/b2b-front-oms/apiv2/loan/result"
        json = {
            "assetOrgNo": "360JR",
            "assetOrgName": "360金融",
            "fbOrgNo": "xna",
            "loanReqNo": "loan20210728a268",
            "sourceCode": "QH"
        }
        headers = {
            "Content-Type": "application/json",
            "isTest": "True"
        }
        resp = requests.post(url=url, json=json, headers=headers)
        print(resp.text, resp.status_code)
        assert 200 == resp.status_code, "该状态不等于200,报错"


if __name__ == '__main__':
    # -s表示输出详细响应信息,如果不加-s则成功接口信息不会打印出来,失败接口信息才会打印出来
    pytest.main(['test_case.py'])
    # pytest.main(['test_case.py', '-s'])
