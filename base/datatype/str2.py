"""
@Author  : weimenghua
@Time    : 2020/7/11 21:18
"""

mystr = 'hello world itcast and itcastcpp'

def test1():
    # 1、find，检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
    # mystr.find(str, start=0, end=len(mystr))
    mystr.find('hello')
    print(mystr.find('hello'))  # 返回0
    print(mystr.find('xx'))  # 返回-1


def test2():
    # 2、index，跟find()方法一样，只不过如果str不在mystr中会报一个异常.
    # mystr.index(str, start=0, end=len(mystr))
    mystr.index('hello')
    print(mystr.index('hello')) # 返回0
    # print(mystr.index('xx')) #报错


def test3():
    # 3、count，返回str在start和end之间在mystr里面出现的次数
    # mystr.count(str, start=0, end=len(mystr))
    mystr.count('hello')
    print(mystr.count('hello'))


def test4():
    # 4、replace，把mystr中的str1替换成str2,如果count指定，则替换不超过count次
    mystr.replace('hello', 'hello2',  mystr.count('hello'))
    print(mystr)


def test5():
    # 5、split，以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
    mystr.split(',')
    print(mystr)


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()