# 加法函数
def add(num1, num2):
    return num1 + num2


# 减法函数
def subtract(num1, num2):
    return num1 - num2


# 乘法函数
def multiply(num1, num2):
    return num1 * num2


# 除法函数
def divide(num1, num2):
    if num2 == 0:
        return "错误：除数不能为零。"
    else:
        return num1 / num2


# 主程序
if __name__ == "__main__":
    num1 = float(input("请输入第一个数："))
    num2 = float(input("请输入第二个数："))

    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")
