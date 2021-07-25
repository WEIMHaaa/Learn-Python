import json


def str_to_json():
    # json中内部数据需要用双引号来包围，不能使用单引号
    str = '{"name": "张艺兴" , "job": "歌手"}'
    j = json.loads(str)
    print("类型：", type(j), j)


def json_to_str():
    # json.dumps序列化时对中文默认使用的ascii编码，ensure_ascii=False（默认为true），将启用原来的编码形式
    str = {'name': '张艺兴', 'job': '歌手'}
    str = json.dumps(str, ensure_ascii=False)
    print("类型：", type(str), str)


if __name__ == '__main__':
    str_to_json()
    json_to_str()
