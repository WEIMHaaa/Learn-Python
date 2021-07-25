"""
@Author  : weimenghua
@Time    : 2020/8/24 21:54
"""
import os


def get_cur_filename():
    # 获取当前文件的全路径名
    file_path = os.path.realpath(__file__)
    return file_path


def get_pwd():
    return os.getcwd()


if __name__ == '__main__':
    print("获取当前文件的全路径名：" + get_cur_filename())
    print("当前路径：", get_pwd())