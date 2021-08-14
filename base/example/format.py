"""
@Author  : weimenghua
@Time    : 2020/11/1 8:55
"""


# 总占位50个字符空间，不足部分以“-”来填充
# 居中显示，且有千位分隔符
# 小数部分只保留2位，还进行了四舍五入
# 最终返回浮点数的类型

def formate1():
    a = 123456.7890
    print("{0:-^50,.5f}".format(a))


def formate2():
    print('{}和{}'.format("张三", "李四"))
    print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))


if __name__ == '__main__':
    formate1()
    formate2()
