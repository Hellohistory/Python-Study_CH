import math

print("输入一个整数，将输出它的所有因数")
a = int(input("请输入 // "))
b = 1
while b <= math.sqrt(a):
    if a % b == 0:
        print("这个数的一个因数是 ", b)
        print("这个数的一个因数是 ", int(a / b))
    b += 1