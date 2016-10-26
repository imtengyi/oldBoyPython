# -*- coding:utf-8 -*-
# Author:YEAR
# 序列化和反序列化 jason 和 pickle
import json
import requests
import pickle

dic = {'haha': 'asdf', 'age': 12}
print(dic, type(dic))
# 将python的基本数据类型转换成字符串类型
result = json.dumps(dic)
print(result, type(result))

s1 = '{"k1":123}'
print(type(json.loads(s1)))

# 举例
response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=广州')
response.encoding = 'utf-8'

dic = json.loads(response)
print(type(dic))

# 注意 单引号和双引号的问题 由于python语言特殊单双引号一样 但别的语言不是 所以在内容中一定要用双引号
li = '["year":123,"age":123]'
ret = json.loads(li)

# dump和load操作 写入文件 从文件读
json.dump(li, open('db', 'w'))
li = json.load(open('db', 'w'))

# pickle 只能python用的序列化
import pickle

li = [11, 22, 33]
r = pickle.dumps(li)
print(r)

result = pickle.loads(r)
print(result)

pickle.dump(li, open('db', 'wb'))
li = pickle.load(open('db', 'rb'))


# 注意jason只能处理基本数据类型,,pickle都可以 但是pickle只能python之间用
# jason 更加适合跨语言 pickle适用于复杂类型
