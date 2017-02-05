# -*- coding:utf-8 -*-
# Author:YEAR
import socket
import os

obj = socket.socket()
obj.connect(('127.0.0.1', 9999,))

# 发送当前文件大小
size = os.stat('').st_size
obj.sendall(bytes(str(size), encoding='utf-8'))

obj.recv(1024)#接收确认包
with open('', 'rb') as f:
    for line in f:
        obj.sendall(line)

obj.close()
