# -*- coding:utf-8 -*-
# Author:YEAR
# python模块 其实就是其他语言的类库 先导入后使用
import sys

print(sys.argv)

for item in sys.path:
    print(item)
# 内置模块 自定义模块 第三方模块  代码分类
# 模块名字很重要 导入模块的依据 sys.path
# 导入的方式 import 和 from ... import ... as ...
# 单模块 import 嵌套在文件夹中的 from import as

# 第三方模块安装 pip3安装 源码安装
# pip3  pip3 install ...
# 源码安装  先下载源代码 按照文档安装 一般是解压然后进入目录 运行python3 setup.py install
