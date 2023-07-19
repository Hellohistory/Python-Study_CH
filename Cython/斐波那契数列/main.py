import time
from fibonacci import fibonacci_cython

n = int(input("输入要计算的数:"))  # 要计算的斐波那契数列的索引

start_time = time.time()
result = fibonacci_cython(n)
end_time = time.time()

execution_time = end_time - start_time

print(f"第 {n} 个斐波那契数是: {result}")
print(f"代码执行时间: {execution_time} 秒")