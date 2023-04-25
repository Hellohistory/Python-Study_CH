# 阿姆斯特朗数是指一个n位数（n≥3），它的每个数字的n次幂之和等于它本身
# 这个程序就是用来判断一个数是否为阿姆斯特朗数
def is_armstrong_number(number):
    total = 0

    # 计算每个数字的立方和
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10

    # 返回结果
    if number == total:
        return True
    else:
        return False


# 主程序
while True:
    try:
        number = int(input("请输入一个数字:"))
        break
    except ValueError:
        print("输入的不是整数，请重新输入！")

if is_armstrong_number(number):
    print(number, "是阿姆斯特朗数")
else:
    print(number, "不是阿姆斯特朗数")