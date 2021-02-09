import os
import re
import time

"""对指定目录下的所有文件进行有选择的修改名称"""
def ReFileName(dirPath,pattern):
    """
    :param dirPath: 文件夹路径
    :param pattern: 正则匹配模式
    :return:
    """
    # 对目录下的文件进行遍历
    for file in os.listdir(dirPath):
        # 判断是否是文件
        if os.path.isfile(os.path.join(dirPath, file)) == True:
            # 用正则匹配，去掉不需要的词
            newName = re.sub(pattern, "", file)
            # 设置新文件名
            newFilename = file.replace(file, newName)
            # 重命名
            os.rename(os.path.join(dirPath, file), os.path.join(dirPath, newFilename))
    print("文件名已统一修改成功")


if __name__ == '__main__':
    timeStart = time.time()
    dirPath = r"C:\Users\wmh\Desktop\新建文件夹"
    pattern = re.compile(r'\[{1}(.+)]\.')
    ReFileName(dirPath,pattern)
    timeEnd = time.time()
    print("程序走了%d秒"%(timeEnd-timeStart))