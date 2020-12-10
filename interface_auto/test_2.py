"""
@Author  : weimenghua
@Time    : 2020/12/10 21:42
"""

import pandas

def ToCsv():
    #data为需要写入的数据,使用字典格式，key为列名，values为每一行的内容
    data={
        "name":"chen", #string直接写入即可
        "age":[123],#int类型需要使用[]括起来
        "sex":"男"
    }

    # 写入csv
    #转换为dataframe格式
    dataCSV = pandas.DataFrame(data)
    dataCSV.to_csv("../files/chen.csv", index=False, mode="a", header=False, encoding="GBK")

ToCsv()