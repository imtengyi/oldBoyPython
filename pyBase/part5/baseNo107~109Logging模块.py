# -*- coding:utf-8 -*-
# Author:YEAR
# Logging模块
import logging

# 日志级别 DEBUG INFO WARING ERROR CRITICAL
logging.warning('user [year] attemped wrong password more than 3 times')
logging.critical('server is down')

# 将日志写入文件 指定级别 只有比此级别高的才能写入文件 还可以指定具体格式和时间格式
logging.basicConfig(filename='example.log', level=logging.INFO, format='$(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.DEBUG('asdfs')
logging.warning('123123')
logging.critical('asdfdf')

# 同时将log打印到屏幕和写入文件里 logging的几大部分 logger handlers filters formatters

# 创建logger
logger = logging.getLogger('TEST-LOG')  # 先获取logger对象
logger.setLevel(logging.DEBUG)  # 设置全局的日志级别

# 创建屏幕handlers
ch = logging.StreamHandler()  # 获取屏幕handler
ch.setLevel(logging.DEBUG)  # 设计屏幕日志级别

# 创建文件handlers
fh = logging.FileHandler('access.log')  # 同上
fh.setLevel(logging.WARNING)

#  创建foramtter并且将formatter添加到ch和fh
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# 告诉logger将log输出到哪
logger.addHandler(ch)
logger.addHandler(fh)

# 注意 局部级别只能比全局高不能比全局低
