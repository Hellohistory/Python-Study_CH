a = (1, 2, 3, 4, 5)
print('元组中的单个元素为:')  # 输出元组中的单个元素
for i in a:
    print(i, end='  ')
print()
print('索引为3的元素值为:', a[3])  # 输出索引为3的元素值
print('从索引2开始的元素值为:', a[2:])  # 输出从索引2开始的元素值
print('元组的长度为:', len(a))  # 输出元组的长度
print('元组中的最大值为:', max(a))  # 输出元组中的最大值
print('元组中的最小值为:', min(a))  # 输出元组中的最小值
del a  # 删除整个元组