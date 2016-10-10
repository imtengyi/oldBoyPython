# -*- coding:utf-8 -*-
# Author:YEAR

salary = input("Input your salary:")

if salary.isdigit():
    salary = int(salary)
else:
    exit("Invaild data type...")

welcome_msg = 'Welcome to Alex Shopping mall'.center(50, '-')
product_list = [
    ('iphone', 5999),
    ('chuizi', 2999),
    ('mac', 8000)
]
print(welcome_msg)

exit_flag = False
shop_car = []
while not exit_flag:
    for item in (product_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(p_name, p_price)

    user_choic = input("[q=quit,c=check]What do you want to buy?:")
    if user_choic.isdigit():  # 肯定是选商品
        user_choic = int(user_choic)
        if user_choic < len(product_list):
            p_item = product_list[user_choic]
            if p_item[1] <= salary:  # 买得起
                shop_car.append(p_item)
                salary -= p_item[1]
                print("Added [%s] into shop car, you current balance is [%s]" % (p_item, salary))
            else:
                print("Your balance is [%s],cannot afford this ..." % salary)
        else:
            pass
    else:
        if user_choic == 'q' or user_choic == 'quit':
            print("purchased product as below".center(40, '*'))
            for item in shop_car:
                print(item)
            print("Goodbye!".center(40, '*'))
            print("Your balance is [%s]" % salary)
            exit_flag = True
        elif user_choic == 'c' or user_choic == 'check':
            print("purchased product as below".center(40, '*'))
            for item in shop_car:
                print(item)
            #命令行上色 \033[31;1m[%s]\033[0m     32绿色 31红色 42背景绿色 41背景红色
            print("Goodbye!".center(40, '*'))
