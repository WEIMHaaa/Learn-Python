import traceback


def zero1():
    try:
        a = 1/0
        print(a)
    except:
        print('1/0,发生异常了')

def zero2():
    try:
        a = 1/0
        print(a)
    except Exception:
        print('traceback：1/0,发生异常了')
        traceback.print_exc()

def zero3():
    try:
        raise Exception('raise主动抛出异常，异常后的代码不再执行')
        a = 1 / 0
        print(a)
    except Exception as e:
        print(e)

def zero4():
    try:
        raise Exception('raise主动抛出异常，异常后的代码不再执行')
        a = 1 / 0
        print(a)
    except Exception as e:
        print(e)
    finally:
        print('一定要打印出来！')


if __name__ == '__main__':
    zero1()
    zero2()
    zero3()
    zero4()