import json

# 1、str To json
# json中内部数据需要用双引号来包围，不能使用单引号
str1 = '{"name": "张艺兴" , "job": "歌手"}'
j = json.loads(str1)
print(j)
print(type(j))


# 2、json To str
# json.dumps序列化时对中文默认使用的ascii编码，ensure_ascii=False（默认为true），将启用原来的编码形式
str2 = {'name': '张艺兴', 'job': '歌手'}
str2 = json.dumps(str2, ensure_ascii=False)
print(str2)
