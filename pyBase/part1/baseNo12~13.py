# -*- coding:utf-8 -*-
# Author:YEAR


name = input("input your name:")
age = int(input("input your age:"))
job = input("input your job:")

msg = '''
Information of yourself:
------------------------
Your name:   %s
Your age:    %d
Your job:    %s
------------------------
''' % (name, age, job)

print(msg)

# print("user input message:", user_input)
# print('user input message: {usermessage}'.format(usermessage=user_input))
