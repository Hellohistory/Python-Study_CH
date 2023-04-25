def fibonacci_generator(num_terms=None):
    """
    生成斐波那契数列的函数，迭代生成num_terms个数
    参数：
        num_terms：int，要生成的项数，默认为None
    返回：
        int，下一个斐波那契数
    """
    f0, f1 = 0, 1
    yield f0
    if num_terms is None:
        while True:
            fn = f0 + f1
            yield fn
            f0, f1 = f1, fn
    elif num_terms >= 1:
        for _ in range(num_terms - 1):
            fn = f0 + f1
            yield fn
            f0, f1 = f1, fn


def fibonacci(num_terms=None):
    """
    生成斐波那契数列的函数，生成num_terms个数
    参数：
        num_terms：int，要生成的项数，默认为None
    返回：
        int列表，斐波那契数列
    """
    return list(fibonacci_generator(num_terms))


for n_fibo in fibonacci(7):
    print(n_fibo)