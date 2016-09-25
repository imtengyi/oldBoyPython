# Author:YEAR

import os

user = ['YEAR']
passwd = {'YEAR': 'year93926'}
errorUser = ''
counter = 0
lockUserfile=os.getcwd()+'HW1_lockUser.txt'
lockflag=0

while True:
    username = input("Please input your user name:")
    password = input("Please input your password:")
    #先判断用户是否被锁
    if os.path.exists(lockUserfile):
        with open(lockUserfile, 'r') as f:
            for line in f.readlines():
                if line.strip() == username:
                    print("This username has been locked!!")
                    lockflag=1
                    break
        if lockflag==1:
            lockflag=0
            continue

    else:
        pass
    if username in user:
        if password == passwd[username]:
            print("Good you login success!!")
            break
        else:
            if errorUser == username:
                counter += 1
                if counter == 3:
                    # 用户名加入锁死账号文件 errorUser和counter清空
                    with open(lockUserfile,'a') as f:
                        f.write(username)
                        f.write("\n")
                    errorUser = ''
                    counter = 0
                    print("Your input username has be locked!!")
                    continue
                else:
                    print("If you lianxu input error 3 times your username will be locked!!")
                    continue
            else:
                errorUser = ''
                counter = 0
                print("If you lianxu input error 3 times your username will be locked!!")
                continue
    else:
        if errorUser == username:
            counter +=1
            if counter==3:
                #用户名加入锁死账号文件 errorUser和counter清空
                with open(lockUserfile, 'a') as f:
                    f.write(username)
                    f.write("\n")
                errorUser = ''
                counter = 0
                print("Your input username has be locked!!")
                continue
            else:
                print("If you lianxu input error 3 times your username will be locked!!")
        else:
            errorUser=''
            counter=0
            print("If you lianxu input error 3 times your username will be locked!!")
