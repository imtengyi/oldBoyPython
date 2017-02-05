# -*- coding:utf-8 -*-
# Author:YEAR

url=input('请输入url:')  #模块名/函数名

target_module, target_func=url.split('/')

m=__import__(target_module)

if hasattr(m,target_func):
    target_func = getattr(m,target_func)
    r=target_func()
    print(r)
else:
    print('404')