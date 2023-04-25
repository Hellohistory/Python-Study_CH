a = int(input("请输入一个数字: "))
if a & (a - 1) == 0:
    print("该数字是二的幂次方")
else:
    print("该数字不是二的幂次方")