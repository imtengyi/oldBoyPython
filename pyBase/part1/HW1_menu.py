# Author: YEAR

fristMenu = ['biubiubiu', 'diudiudiu', 'jiujiujiu']
secondMenu = {'biubiubiu': ['haha'], 'diudiudiu': ['haha'], 'jiujiujiu': ['haha']}
thridMenu = {'biubiubiu_haha': 'diaoni', 'diudiudiu_haha': 'diaoni', 'jiujiujiu_haha': 'diaoni'}

while True:
    counter = 1
    for fristChoose in fristMenu:
        print(counter, fristChoose)
        counter += 1
    userchoose = input("Please input your choose!!")
    if userchoose == '1':
        counter = 0
        for secondChoose in secondMenu['biubiubiu']:
            print(counter, secondChoose)
            counter += 1
        userchoose = input("Please input your choose!!")
        # .....
        pass
    elif userchoose == '2':
        pass
    elif userchoose == '3':
        pass
    elif userchoose == 'q':
        break
    else:
        continue
