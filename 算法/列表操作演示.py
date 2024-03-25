List = []  # 创建一个空列表
# List 是可变的
# 这意味着值是可以改变的

List.insert(0, 5)  # 插入操作在指定的索引处进行
List.insert(1, 10)
List.insert(0, 6)
print(List)

List.remove(6)
List.append(9)  # 插入操作在末尾进行
List.append(1)
List.sort()     # 排序操作按升序排列元素
print(List)

List.pop()
List.reverse()
print(List)

"""
List.append(1)
print(List)
List.append(2)
print(List)
List.insert(1 , 3)
print(List)
"""

list2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]
for i in list2:
    if i % 2 == 0:
        print(i)

"""
预期输出:
2
10
12
4
"""
