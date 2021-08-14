"""
@Author  : weimenghua
@Time    : 2020/12/10 21:42
"""

import pandas


def wirte_to_csv():
    # data为需要写入的数据,使用字典格式，key为列名，values为每一行的内容
    data = {
        "name": "张艺兴",  # string直接写入即可
        "age": [123],     # int类型需要使用[]括起来
        "sex": "男",
        "other": "其它信息"
    }

    # 写入csv
    # 转换为dataframe格式
    dataCSV = pandas.DataFrame(data)
    # mode = "a"，追加模式，如果不使用这个模式，会把前面的内容覆盖。
    # header = False：不写入头部信息，即字典中的key值不写入。
    # encoding = "GBK"：编码格式为GBK，即中文编码，默认为utf - 8，如果数据有中文时则可能会报错(encoding为GBK格式的时候中文会乱码)
    dataCSV.to_csv("../../files/csvdemo.csv", index=False, mode="a", header=False, encoding="UTF-8")


if __name__ == '__main__':
    wirte_to_csv()
