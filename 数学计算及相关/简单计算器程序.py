# 简单计算器程序

# 这个函数用于两个数相加
def add(x, y):
    return x + y

# 这个函数用于两个数相减
def subtract(x, y):
    return x - y

# 这个函数用于两个数相乘
def multiply(x, y):
    return x * y

# 这个函数用于两个数相除
def divide(x, y):
    if(y==0):
        raise Exception("除数不能为零")
    return x / y


print("选择运算.")
print("1.相加")
print("2.相减")
print("3.相乘")
print("4.相除")

while True:
    # 从用户处获取输入
    choice = input("输入你的选择(1/2/3/4): ")

    # 检查选择是否为四个选项之一
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("输入第一个数字: "))
        num2 = float(input("输入第二个数字: "))

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