def fib(n: int) -> int:
    # 创建一个列表来存储计算结果
    fib_list = [-1] * (n + 1)

    def _fib(n: int) -> int:
        if n <= 1:
            return n

        # 检查结果是否已经计算
        if fib_list[n] != -1:
            return fib_list[n]

        # 计算并存储结果
        fib_list[n] = _fib(n-1) + _fib(n-2)

        return fib_list[n]

    return _fib(n)


# 测试函数
number_of_terms = int(input())
for i in range(number_of_terms):
    print(fib(i))
