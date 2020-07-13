import urllib.request
import urllib.parse
import json

content = input("请输入翻译的内容:")

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}

data['i'] = content

data['from'] = 'en'
data['to'] = 'zh-CHS'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15934837793668'
data['sign'] = '6c263b05b4511c7c9fc9e540d8cb3b42'
data['ts'] = '1593483779366'
data['bv'] = 'dd0840fad0d96c2e9de5a4f181a39d98'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)

html = response.read().decode('utf-8')

print(html)
target = json.loads(html)
print("翻译的结果是：%s" % (target['translateResult'][0][0]['tgt']))