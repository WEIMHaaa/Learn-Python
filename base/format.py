"""
@Author  : weimenghua
@Time    : 2020/11/1 8:55
"""


# 总占位50个字符空间，不足部分以“-”来填充
# 居中显示，且有千位分隔符
# 小数部分只保留2位，还进行了四舍五入
# 最终返回浮点数的类型

def formate():
    a = 123456.7890
    print("{0:-^50,.5f}".format(a))


if __name__ == '__main__':
    formate()
