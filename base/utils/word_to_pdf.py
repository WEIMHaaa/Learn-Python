import os

from win32com import client

from base.utils import path


def doc2pdf(wordpath, pdfpath):
    for root, dirs, files in os.walk(wordpath, topdown=False):  # 遍历文件夹
        for name in files:
            doc_name = os.path.join(root, name)
            # pdf_name = doc_name.split('.docx',)[0] + '.pdf'
            (filename, extension) = os.path.splitext(name)  # filename文件名，extension后缀名
            # pdf_name为pdf文件名，此处不加.pdf也可以，但是word名中有‘.’的时候会发生转化失败
            pdf_name = os.path.join(pdfpath, filename) + '.pdf'
            print(pdf_name)
            try:
                word = client.DispatchEx('Word.Application')
                if os.path.exists(pdf_name):
                    os.remove(pdf_name)
                worddoc = word.Documents.Open(doc_name, ReadOnly=1)
                worddoc.SaveAs(pdf_name, FileFormat=17)
                worddoc.Close(True)
                word.Quit()  # 切记，这步必须加，要不然线程不会杀死，电脑会卡死
                print("success")
            except Exception as e:
                print(e)
                print("error")
                return 1


if __name__ == '__main__':
    print("当前路径：", path.get_pwd())

    filespath = os.path.abspath('../../files');
    print(filespath);
    doc2pdf(filespath, filespath)
