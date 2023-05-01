import os
from getpass import getpass

# 由Black_angel开发
# 这是Logo函数
def logo():
    print(" ──────────────────────────────────────────────────────── ")
    print(" |                                                        | ")
    print(" |   ########    ##  #########  ##       ##      ###      | ")
    print(" |   ##     ##   ##  ##         ##       ##    ##   ##    | ")
    print(" |   ##     ###  ##  ##         ##       ##   ##     ##   | ")
    print(" |   ##     ###  ##  #########  ###########  ##########   | ")
    print(" |   ##     ###  ##         ##  ##       ##  ##      ##   | ")
    print(" |   ##     ##   ##         ##  ##       ##  ##      ##   | ")
    print(" |   ########    ##  #########  ##       ##  ##      ##   | ")
    print(" |                                                        | ")
    print(" \033[1;91m|   || 数字信息安全助手 ||  | ")
    print(" |                                                        | ")
    print(" ──────────────────────────────────────────────────────── ")
    print("\033[1;36;49m")


# 这是登录函数
def login():
    # 用于清除屏幕
    os.system("clear")
    print("\033[1;36;49m")
    logo()
    print("\033[1;36;49m")
    print("")
    usr = input("输入您的用户名：")
    # 这是用户名，您可以在此更改
    usr1 = "raj"
    psw = getpass("输入您的密码：")
    # 这是密码，您可以在此更改
    psw1 = "5898"
    if usr == usr1 and psw == psw1:
        print("\033[1;92m登录成功")
        os.system("clear")
        print("\033[1;36;49m")
        logo()
    else:
        print("\033[1;91m 错误")

        login()


# 这是主函数
if __name__ == "__main__":
    login()