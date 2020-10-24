"""
@Author  : weimenghua
@Time    : 2020/9/19 12:29
"""
import sys

list = [1, 2, 3, 4, 5]

# 创建迭代器对象
it = iter(list)

# 输出迭代器的下一个元素
# print(next(it))
#
# for x in it:
#     print(x, end=" ")

while True:
    try:
        print(next(it))
    # 异常用于标识迭代的完成，防止出现无限循环的情况
    except StopIteration:
        sys.exit()


"""
知识点1：
迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器。

知识点2：
将iter(list)写成了iter[list]
TypeError: 'builtin_function_or_method' object is not subscriptable
TypeError：“ builtin_function_or_method”对象不可下标

知识点:3：
（）是函数引入参数
｛｝是字典
［］是列表key
"""
