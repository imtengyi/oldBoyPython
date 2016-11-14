# -*- coding:utf-8 -*-
# Author:YEAR

import getpass
import os

# username = input("username:")
# password = getpass.getpass("password:")
# print(username, password)
# cmdBack = os.system("df -h") #拿到命令执行后的返回code
cmdBack = os.popen("df -h").read()
# os.mkdir('biubiubiu')
print(cmdBack)
