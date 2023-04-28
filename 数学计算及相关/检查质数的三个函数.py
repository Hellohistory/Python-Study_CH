# 作者：Tan Duc Mai
# 电子邮件：tan.duc.work@gmail.com
# 描述：三个不同的函数用于检查给定数字是否为质数。
# 如果是质数，则返回True，否则返回False。
# 这三个函数的效率从a到c递减（需要更长的时间）。

from math import sqrt


def is_prime_a(n):  # 第一个函数
    if n < 2:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True


def is_prime_b(n):  # 第二个函数
    if n > 1:
        if n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
    return False


def is_prime_c(n):  # 第三个函数
    divisible = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisible += 1
    if divisible == 2:
        return True
    return False