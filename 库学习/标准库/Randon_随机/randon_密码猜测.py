from random import * # 导入随机数模块

user_pass = input("请输入密码: ") # 获取用户输入的密码
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v','w','x','y' 'z','0','1','2','3','4','5','6','7','8','9'] # 生成密码可能包含的字符列表

guess = "" # 初始化猜测密码
while (guess != user_pass): # 当猜测密码不等于用户输入的密码时
    guess = "" # 重置猜测密码
    for letter in range(len(user_pass)): # 遍历用户输入的密码
        guess_letter = password[randint(0, 35)] # 从密码字符列表中随机选取一个字符
        guess = str(guess_letter) + str(guess) # 将生成的字符加入猜测密码中
    print(guess) # 输出猜测密码
print("您的密码是",guess) # 输出用户密码