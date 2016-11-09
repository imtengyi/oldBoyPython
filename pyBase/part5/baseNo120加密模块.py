# -*- coding:utf-8 -*-
# Author:YEAR
# 加密模块 md5加密
import hashlib

obj = hashlib.md5()
obj.update(bytes('123', encoding='utf-8'))
result = obj.hexdigest()
print(result)

# 为了防止撞库 可以加一个自己的key

obj = hashlib.md5(bytes('asdfasdfasdf', encoding='utf-8'))
obj.update(bytes('123', encoding='utf-8'))
result = obj.hexdigest()
print(result)
