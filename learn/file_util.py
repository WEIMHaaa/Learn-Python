import os
import shutil
import re

import fitz  # pip install PyMuPDF
from PIL import Image


def copy_to_src(file_path, file_name, save_path):
    """
    把文件复制到处理文件的文件夹，使用复制的文件，防止原文件丢失
    :param file_path: 原文件路径
    :param file_name: file_name为None时，文件不进行重命名
    :param save_path: 存放处理后的文件的文件夹路径
    :return: 复制后的文件路径
    """
    # 非法字符转换成'_'
    fil = re.compile(u'[^0-9a-zA-Z\u4e00-\u9fa5]+', re.UNICODE)
    new_file_name = fil.sub('_', file_name)
    base_name = os.path.basename(file_path)
    base_name_suffix = os.path.basename(file_path).split(".")[1]
    shutil.copyfile(file_path, save_path + base_name)
    if file_name is not None:
        if not os.path.exists(save_path + new_file_name + "." + base_name_suffix):
            os.rename(save_path + base_name, save_path + new_file_name + "." + base_name_suffix)
        else:
            # 替换
            os.remove(save_path + new_file_name + "." + base_name_suffix)
            os.rename(save_path + base_name, save_path + new_file_name + "." + base_name_suffix)
        return save_path + new_file_name + "." + base_name_suffix
    else:
        return save_path + base_name


def pdf_to_image(flag, file_path):
    """
    pdf转图片
    :param flag: flag是否需要分页，false直接取第一页
    :param file_path: 文件路径
    :return:
    """
    file_name = file_path.split(".")[0]
    doc = fitz.open(file_path)  # 打开一个PDF文件，doc为Document类型，是一个包含每一页PDF文件的列表
    rotate = int(0)  # 设置图片的旋转角度
    zoom_x = 2.0  # 设置图片相对于PDF文件在X轴上的缩放比例
    zoom_y = 2.0  # 设置图片相对于PDF文件在Y轴上的缩放比例
    trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    file_array = []
    if flag:
        for pg in range(doc.pageCount):
            page = doc[pg]  # 获得第pg页
            pm = page.getPixmap(matrix=trans, alpha=False)  # 将其转化为光栅文件（位数）
            new_file_name = "%s_%s.jpg" % (file_name, pg)  # 保证输出的文件名不变
            pm.writeImage(new_file_name)  # 将其输入为相应的图片格式，可以为位图，也可以为矢量图
            file_array = get_file_array(new_file_name, file_array)
    else:
        page = doc[0]
        pm = page.getPixmap(matrix=trans, alpha=False)
        new_file_name = "%s_%s.jpg" % (file_name, 0)  # 保证输出的文件名不变
        pm.writeImage(new_file_name)  # 将其输入为相应的图片格式，可以为位图，也可以为矢量图
        file_array = get_file_array(new_file_name, file_array)
    return file_array


def get_file_array(new_file_name, file_array):
    """
    获取图片地址,多个,本方法只支持图片格式
    """
    file_array.append(get_file(new_file_name))
    return file_array


def get_file(new_file_name):
    """
    获取图片地址,单个,本方法只支持图片格式
    """
    # 转换图片格式
    trans_file_name = transimg(new_file_name)
    # 压缩图片
    compress_file_name = compress_image(trans_file_name)
    # 成功压缩
    if compress_file_name != new_file_name:
        # 把转换格式后的文件替换为压缩文件
        os.rename(compress_file_name, trans_file_name)
    # 返回处理后的图片路径
    return trans_file_name


def transimg(img_path):
    """
    通用图片格式转化为jpg
    jpg转jpg会保持原文件不变
    """
    str = img_path.rsplit(".", 1)
    output_img_path = str[0] + ".jpg"
    im = Image.open(img_path)
    rgb_im = im.convert('RGB')
    rgb_im.save(output_img_path)
    return output_img_path


def compress_image(infile, outfile='', mb=8 * 1024 * 1024, step=10, quality=80):
    """
    不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，字节
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    o_size = os.path.getsize(infile)
    if o_size <= mb:
        return infile
    outfile = get_outfile(infile, outfile)
    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = os.path.getsize(outfile)
    return outfile


def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '%s_out%s' % (dir, suffix)
    return outfile


if __name__ == '__main__':
    path_array = []
    path = 'D:\\software\\PyCharm 2019.3.2\\PythonProjects\\learn-python\\files\神奇的PDF.pdf'
    save_image_path = "C:\\Users\\wmh\\Desktop\\"
    base_name = os.path.basename(path)
    shutil.copyfile(path, save_image_path + base_name)
    if os.path.basename(save_image_path + base_name).split(".")[1] == 'pdf':
        path_array = pdf_to_image(True, save_image_path + base_name)
    else:
        path_array = get_file_array(save_image_path + base_name, path_array)
    for path in path_array:
        print(str(path))
