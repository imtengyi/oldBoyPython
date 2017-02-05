# -*- coding:utf-8 -*-
# Author:YEAR
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9999,))
sk.listen(5)
while True:
    conn, address = sk.accept()
    f = open('', 'wb')
    # 先接收文件大小,再接收文件
    file_size = str(conn.recv(1024), encoding='utf-8')
    total_size = int(file_size)
    has_recv = 0

    conn.sendall(bytes('开始吧', encoding='utf-8')) #发送确认包

    while True:
        if total_size == has_recv:
            break
        data = conn.recv(1024)
        f.write(data)
        has_recv += len(data)
    f.close()
