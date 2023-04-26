def sumOfSeries(n):
    x = n * (n + 1) / 2  # 计算等差数列的和
    return (int)(x * x)  # 返回平方值


# 驱动函数
n = 5
print(sumOfSeries(n))  # 打印结果
