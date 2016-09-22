# -*- coding:utf-8 -*-
# Author:YEAR

user = 'YEAR'
passwd = 'year93926'
age = 23

username = input("username:")
password = input("password")

# if user == username:
#     print("username is correct...")
#     if password == passwd:
#         print("Welcome login.....")
#     else:
#         print("Password is invalid!!")
# else:
#     print("用户名都没写对 滚粗!!!")
if user == username and passwd == password:
    print("Welcome login..you have 3 chance")
    counter = 0
    for i in range(10):
        if counter < 3:
            guess_num = int(input("input your guess num:"))
            if guess_num == age:
                print("You are right")
                break
            elif guess_num > age:
                print("bigger")
            else:
                print("smaller")
        else:
            # print("You have try too many time!!")
            # break
            continue_confirm = input("Do you want to continue bescause you are stupid:")
            if continue_confirm == 'y':
                counter = 0
                continue
            else:
                break
        counter += 1

else:
    print("给你个飞天大草!!!")
