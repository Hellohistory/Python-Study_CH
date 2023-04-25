"""
这段代码的作用是实现对输入的整数列表进行循环左移（旋转）指定次数后输出旋转后的列表。
其中，代码实现的核心是通过遍历列表，将旋转后的元素添加到新列表中，并使用取模运算确保旋转后的元素不越界。最后输出旋转后的列表。
"""
N = int(input("请输入数组大小:"))
list = []
for i in range(0, N):
    temp = int(input("请输入整数:"))
    list.append(temp)



# 使用最佳方法旋转数组：
# 列表的左旋转。
# 假设我们想要在旋转d次后打印列表。


finalList = []
d = int(input("请输入要旋转的次数:"))

# 遍历列表
for i in range(0, N):
    # 将旋转后的元素添加到新列表中
    finalList.append(list[(i + d) % N])

# 输出旋转后的列表
print(finalList)

# 这种方法的时间复杂度为O（N），空间复杂度为O（N）