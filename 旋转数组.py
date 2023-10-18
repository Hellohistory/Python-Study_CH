# 旋转整数列表
N = int(input("请输入数组大小："))

# 获取输入列表
num_list = []
while len(num_list) < N:
    temp = input("请输入整数：")
    while not temp.isdigit():  # 对输入进行有效性检查
        temp = input("请重新输入整数：")
    num_list.append(int(temp))

# 获取旋转次数
d = int(input("请输入要旋转的次数："))

# 处理旋转次数为0或列表为空的情况
if d == 0 or N == 0:
    final_list = num_list
else:
    final_list = []
    # 遍历列表，将旋转后的元素添加到新列表中
    for i in range(N):
        final_list.append(num_list[(i + d) % N])

# 输出旋转后的列表
print("旋转后的列表为：", final_list)
