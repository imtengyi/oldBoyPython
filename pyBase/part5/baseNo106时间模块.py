# -*- coding:utf-8 -*-
# Author:YEAR
# time模块
import time

# 时间戳 从1970年一月一日到现在的秒数
print(time.time())

# 当前时间 字符串格式 可以给时间戳参数将时间戳转换成字符串格式
print(time.ctime())
print(time.ctime(time.time() - 86400))

# 将时间的每一个值分开并取出 返回时间对象 和ctime一样可以转换时间戳
time_obj = time.gmtime()
print(time_obj)
print(time_obj.tm_year, time_obj.tm_mon)
# 注意当前时间是格林威治时间

# 获取本地时间
print(time.localtime())

# 将structtime转换成时间戳
print(time.mktime(time.gmtime()))

# 延时 用来做阻塞
time.sleep(4)
print("---")

# 将时间对象转换成你想要的时间格式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
# 将字符串按照给定格式转换成时间对象
print(time.strptime("2016-01-28", "%Y-%m-%d"))

# datetime模块
import datetime

# 输出当前时期
print(datetime.date.today())
# 将时间戳转换成日期格式
print(datetime.date.fromtimestamp(time.time()))
# 当前准确时期时间
print(datetime.datetime.now())
# 返回时间对象
print(datetime.datetime.now().timetuple())

# 时间的加减
print(datetime.datetime.now() + datetime.timedelta(days=10))
print(datetime.datetime.now() + datetime.timedelta(days=-10))
print(datetime.datetime.now() - datetime.timedelta(days=10))
print(datetime.datetime.now() + datetime.timedelta(hours=10))

# 字符串时间替换
print(datetime.datetime.now().replace(2014, 9, 26))

# 将字符串按照给定格式转换成时间对象
print(datetime.datetime.strptime("2016-01-28", "%Y-%m-%d"))

# 时间对象之间可以相互比较
