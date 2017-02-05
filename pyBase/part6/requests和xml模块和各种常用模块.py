# -*- coding:utf-8 -*-
# Author:YEAR
import requests

response = requests.get("http://www.baidu.com")
response.encoding = "utf-8"
result = response.text
print(result)

from xml.etree import ElementTree as ET

r = requests.get('biubiuiu')
result = r.text
root = ET.XML(result)

for node in root.iter('biubiubiu'):
    print(node.tag, node.attrib)
    print(node.find('biubiu').text)

tree = ET.parse('baba.xml')
root = tree.getroot()
# 修改root
root.write('output.xml')

import configparser

# 配置文件中所有的值都是字符串所以不需要加引号
con = configparser.ConfigParser()
# con对象的read功能 打开文件读取文件 放进内容
con.read("ini", encoding="utf-8")
# con对象的sections,内存中寻找所有的[xxx]
result = con.sections()
print(result)
# options获取所有指定节点下的所有值
ret = con.options("kaixin")
print(ret)
# get直接获取指定节点指定key的值
baba = con.get('kaixin', 'age')
# 是否有该节点
has_sec = con.has_section('babab')
# 添加节点
con.add_section("babab")
# 删除节点
con.remove_section("babab")
# 检查是否有该key
con.has_option('bababa', 'age')
# 删除键值对
con.remove_option('babab', 'age')
# 修改键值对 有会修改 没有会创建
con.set('babab', 'age', '123')
# 写入文件
con.write(open('ini', 'w'))

import shutil

# 将一个文件内容拷贝到另一个文件, 前一个读往后面写, a自然就是添加
shutil.copyfileobj(open('old', 'r'), open('new', 'a'))
# 拷贝文件
shutil.copyfile('f1', 'f2')
# 仅仅拷贝全向,内组用户都不变
shutil.copymode('f1', 'f2')
# 拷贝状态信息
shutil.copystat('f1', 'f2')
# 拷贝文件和权限
shutil.copy('f1', 'f2')
# 拷贝文件和状态信息
shutil.copy2('f1', 'f2')

# 递归拷贝文件夹
shutil.copytree('folder1', 'folder', ignore=shutil.ignore_patterns('*pyc', 'tmp*'))
shutil.copytree('folder1', 'folder', symlinks=True, ignore=shutil.ignore_patterns('*pyc', 'tmp*'))
# 递归删除文件夹
shutil.rmtree('folder1')
# 递归移动文件夹
shutil.move('folder1', 'folder2')

# 操作压缩文件
ret = shutil.make_archive('wwwww', 'gztar', root_dir='/bbb/asdf')

# shutil模块对压缩包的处理是用的zipfile和tarfile两个模块来玩的
import zipfile

z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall()
# 解压指定文件
z.namelist()
z.extract("babab")
z.close()

import tarfile

tar = tarfile.open('laxi.tar', 'w')
tar.add('asdasdf.log', arcname='bbb.log')
tar.close()
tar = tarfile.open('laxi.tar', 'r')
tar.extractall()
tar.getmembers()
tar.extract('aasdf.log')
tar.close()

# 和终端命令执行有关的模块
import subprocess

# 直接执行命令 返回返回码
ret = subprocess.call('ipconfig')
# check_call 状态码非0抛出异常
# check_output 可以拿到返回结果 错误抛出异常
ret = subprocess.check_output('ipconfig')
print(ret)
# shell为true 想怎么写怎么写
ret = subprocess.call('ls -al', shell=True)
# 复杂的命令 例如交互命令
subprocess.Popen('ls -al', shell=True, cwd='/a/a/')
obj = subprocess.Popen('python', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)\n")
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
# 简单方式
out_error_list = obj.communicate('print(1)')
