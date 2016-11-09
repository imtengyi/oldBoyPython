# -*- coding:utf-8 -*-
# Author:YEAR
import sys
import os
import time

# sys模块 跟解释器相关的都在sys里  和系统相关的都在os里
print(sys.argv[0])  # 命令行参数list 第一个元素是程序本身路径
# sys.exit(0)  # 退出程序 正常退出时sys.exit(0)
print(sys.version)  # python解释器版本
print(sys.maxsize)  # 最大int值
print(sys.path)  # 模块搜索路径 初始化时使用PYTHONPATH环境变量的值
print(sys.platform)  # 操作系统平台


# sys.stdin  # 标准输入相关
# sys.stdout  # 标准输出相关
# sys.stderr  # 标准错误相关


# 进度条
def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r%d%%' % (rate_num,)  # \r表示回到当前行的收个首个位置
    r1 = '\r%s>%d%%' % ("=" * num, rate_num)
    # print(r)
    sys.stdout.write(r)  # 不自带换行符
    sys.stdout.flush()


for i in range(0, 101):
    time.sleep(0.1)
    view_bar(1, 100)

# os模块 目录文件操作等等 看文档去吧
os.path.abspath('')  # 返回path的规范化绝对路径
os.path.dirname('')  # 返回path的目录
os.path.join('', '')  # 多个路径拼接 第一个绝对路径之前的参数将被忽略
