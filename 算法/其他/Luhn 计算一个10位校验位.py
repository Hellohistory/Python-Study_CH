"""
使用 Luhn 算法的 Python 程序

此程序使用 Luhn 算法（以其创建者 Hans Peter Luhn 命名）来计算一个 10 位“有效负载”数字的校验位，并输出最终的 11 位数字。

为了证明这个程序正确地计算了校验位，输入 7992739871 应该返回：

所有数字的和：67
校验位：3
完整有效数字（11 位）：79927398713

11/15/2021
David Costell（在 GitHub 上称为 DontEatThemCookies）
"""

# 输入
CC = input("输入要验证的数字（例如 7992739871）：")
if len(CC) != 10:
    input("数字必须为 10 位！")
    exit()

# 使用列表推导将数字拆分为单独的数字
split = [int(split) for split in str(CC)]

# 要进行双倍计算的数字列表
tobedoubled = [split[1], split[3], split[5], split[7], split[9]]
# 不进行双倍计算的剩余数字列表
remaining = [split[0], split[2], split[4], split[6], split[8]]

# 步骤 1
# 对 tobedoubled 列表中的所有值进行双倍计算
# 将新计算的双倍值放入一个新的列表
newdoubled = []
for i in tobedoubled:
    i = i * 2
    newdoubled.append(i)
tobedoubled = newdoubled

# 检查 tobedoubled 列表中是否有任何双位数字项
# 将所有双位数字项拆分为两个单个数字项
newdoubled = []
for i in tobedoubled:
    if i > 9:
        splitdigit = str(i)
        for index in range(0, len(splitdigit), 1):
            newdoubled.append(splitdigit[index : index + 1])
        tobedoubled.remove(i)
newdoubled = [int(i) for i in newdoubled]

# 将所有列表合并为一个列表（luhnsum）
luhnsum = []
luhnsum.extend(tobedoubled)
luhnsum.extend(newdoubled)
luhnsum.extend(remaining)

# 输出
print("最终数字列表：", luhnsum)
print("所有数字的和：", sum(luhnsum))
checkdigit = 10 - sum(luhnsum) % 10
print("校验位：", checkdigit)
finalcc = str(CC) + str(checkdigit)
print("完整有效数字（11 位）：", finalcc)
input()
