"""
@Author  : weimenghua
@Time    : 2020/7/12 8:30
"""


# 定义Car类
class Car:
    # 初始化函数，用来完成一些默认的设定
    def __init__(self):
        self.wheelNum = 4
        self.color = '蓝色'

    def move(self):
        print('车在跑，目标：夏威夷')


# 创建对象
BWM = Car()

print('车的颜色为：%s' % BWM.color)
print('车的轮胎数量为：%s' % BWM.wheelNum)
