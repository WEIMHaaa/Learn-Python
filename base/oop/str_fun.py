"""
@Author  : weimenghua
@Time    : 2020/7/12 8:52
"""


# 在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
# 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

class Car():
    # 初始化函数，用来完成一些默认的设定
    def __init__(self, newWhellNum, newColor):
        self.wheelNum = newWhellNum
        self.color = newColor

    def __str__(self):
        msg = "嘿。。。我的颜色是" + self.color + "，我有" + str(self.wheelNum) + "个轮胎..."
        return msg

    def move(self):
        print('车在跑，目标：夏威夷')


if __name__ == '__main__':
    BWM = Car(666, '绿色')
    print(BWM)
