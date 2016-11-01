# -*- coding:utf-8 -*-
# Author:YEAR
# 反射
# 利用字符串形式 去(模块)对象中操作(寻找/检查/删除/设置)成员, 这就叫反射 django这种框架就会用到
# hasattr(模块名,成员名) 判断模块中是否有该成员
# getattr(模块名,成员名) 取得模块中的成员
# setattr(模块名,) 设置模块中的成员 在内存中操作
# delattr() 删除模块中的成员 在内存中操作
# 利用反射动态的导入模块 obj=__import__("time") obj.  obj=__import__("lib.cccc",fromlist=True)
