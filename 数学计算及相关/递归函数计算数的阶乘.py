# 定义一个递归函数来计算阶乘
def factorial(n):
    # 基本情况：如果 n 为 0，则阶乘为 1
    if n == 0:
        return 1
    else:
        # 递归情况：计算 n * (n-1) 的阶乘
        return n * factorial(n - 1)

# 获取用户输入的整数
n = int(input("请输入一个数以计算阶乘："))

# 调用函数计算阶乘并打印结果
print("结果：", factorial(n))