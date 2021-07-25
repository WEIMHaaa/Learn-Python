import urllib

url = "http://www.baidu.com/s"
word = {"wd": "传智播客"}
word = urllib.parse.urlencode(word)  # 转换成url编码格式（字符串）
newurl = url + "?" + word  # url首个分隔符就是 ?

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib.request.Request(newurl, headers=headers)

response = urllib.request.urlopen(request)

print(response.read())
