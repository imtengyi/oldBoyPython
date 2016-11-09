# -*- coding:utf-8 -*-
# Author:YEAR
import sys
import os

# 模块中的特殊变量
# 查看模块中的变量
print(vars(sys))
# __doc__获取文件的注释 就是在文件的开头 用三引号框起来的内容
# __cached__模块的字节码所在路径
# __file__ 获得模块所在路径 可能会得到一个相对路径
os.path.abspath(__file__)  # 获取绝对路径
os.path.dirname(__file__)  # 找上级目录
# __package__ 当前文件在哪个包里
# __name__ 执行哪个文件 哪个文件的 __name__==“__main__”
