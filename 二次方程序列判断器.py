# GGearing
# 2017年10月2日
# 简单的脚本用于计算一系列数字的二次方程，并判断该序列是否为二次方程

def findLinear(numbers):  # 寻找线性序列的a和b值
    a = numbers[1] - numbers[0]
    a1 = numbers[2] - numbers[1]
    if a1 == a:
        b = numbers[0] - a
        return (a, b)
    else:
        print("序列不是线性的")


sequence = []
first_difference = []
second_difference = []
for i in range(4):  # 输入
    term = str(i + 1)
    inp = int(input("输入第" + term + "项: "))
    sequence.append(inp)

for i in range(3):
    gradient = sequence[i + 1] - sequence[i]
    first_difference.append(gradient)
for i in range(2):
    gradient = first_difference[i + 1] - first_difference[i]
    second_difference.append(gradient)

if second_difference[0] == second_difference[1]:  # 检查是否一致
    a = second_difference[0] / 2
    subs_diff = []
    for i in range(4):
        n = i + 1
        num = a * (n * n)
        subs_diff.append((sequence[i]) - num)
    b, c = findLinear(subs_diff)
    print(
        "第n项公式: " + str(a) + "n^2 + " + str(b) + "n + " + str(c)
    )  # 输出第n项公式
else:
    print("序列不是二次方程")