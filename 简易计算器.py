# 简易计算器程序

# 定义加法函数
def add(x, y):
    return x + y


# 定义减法函数
def subtract(x, y):
    return x - y


# 定义乘法函数
def multiply(x, y):
    return x * y


# 定义除法函数
def divide(x, y):
    return x / y


# 输出可选操作
print("选择操作：")
print("1.加法")
print("2.减法")
print("3.乘法")
print("4.除法")

while True:
    # 从用户获取输入
    choice = input("输入选择（1/2/3/4）：")

    # 检查选择是否为四个选项之一
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("输入第一个数字："))
        num2 = float(input("输入第二个数字："))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("无效输入")
