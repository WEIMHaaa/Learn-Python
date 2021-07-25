"""
@Author  : weimenghua
@Time    : 2020/7/12 16:27
"""


class Test(object):
    def __init__(self, switch):
        self.switch = switch  # 开关

    def calc(self, a, b):
        try:
            return a / b
        except Exception as result:
            if self.switch:
                print("捕获开启，已经捕获到了异常，信息如下:")
                print(result)
            else:
                # 重新抛出这个异常，此时就不会被这个异常处理给捕获到，从而触发默认的异常处理
                raise


if __name__ == '__main__':
    a = Test(True)
    a.calc(11, 0)

    print("----------------------华丽的分割线----------------")

    a.switch = False
    a.calc(11, 0)
