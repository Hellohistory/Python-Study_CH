"""
虽然Python中有函数可以找到最大公约数，但这是一个接受两个输入并打印两个数的最大公约数的代码。
"""
a = int(input("输入数字1（a）:"))
b = int(input("输入数字2（b）:"))

i = 1
while i <= a and i <= b: # 循环直到i大于a和b
    if a % i == 0 and b % i == 0: # 如果a和b都能被i整除
        gcd = i # 将i赋值给gcd
    i = i + 1 # i加1

print("\n{0}和{1}的最大公约数为{2}".format(a, b, gcd)) # 打印结果