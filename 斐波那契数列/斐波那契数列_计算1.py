# Fibonacci 工具
# 本脚本仅适用于 Python3！

import time


def getFibonacciIterative(n: int) -> int:
    """
    迭代计算第 n 个斐波那契数
    """

    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a


def getFibonacciRecursive(n: int) -> int:
    """
    递归计算第 n 个斐波那契数
    """

    a = 0
    b = 1

    def step(n: int) -> int:
        nonlocal a, b
        if n <= 0:
            return a
        a, b = b, a + b
        return step(n - 1)

    return step(n)


def getFibonacciDynamic(n: int, fib: list) -> int:
    """
    使用动态规划计算第 n 个斐波那契数以提高运行时间
    """

    if n == 0 or n == 1:
        return n
    if fib[n] != -1:
        return fib[n]
    fib[n] = getFibonacciDynamic(n - 1, fib) + getFibonacciDynamic(n - 2, fib)
    return fib[n]


def main():
    n = int(input())
    fib = [-1] * n
    getFibonacciDynamic(n, fib)


def compareFibonacciCalculators(n: int) -> None:
    """
    交互式比较两个斐波那契数生成器
    """

    startI = time.clock()
    resultI = getFibonacciIterative(n)
    endI = time.clock()

    startR = time.clock()
    resultR = getFibonacciRecursive(n)
    endR = time.clock()

    s = "{} 计算 {} => {} 用时 {} 秒"
    print(s.format("迭代", n, resultI, endI - startI))
    print(s.format("递归", n, resultR, endR - startR))