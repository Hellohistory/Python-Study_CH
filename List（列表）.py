List = []
# List是可变的
# 意味着值可以改变

# 在索引0处插入5
List.insert(0, 5) 
# 在索引1处插入10
List.insert(1, 10) 
# 在索引0处插入6
List.insert(0, 6)
print(List)

# 移除第一个值为6的元素
List.remove(6) 

# 在列表末尾添加9
List.append(9) 
# 在列表末尾添加1
List.append(1)

# 将列表元素按升序排列
List.sort()    
print(List)

# 移除并返回最后一个元素
List.pop()
# 将列表元素反转
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

# 定义一个新列表
list2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]

# 遍历列表中的每个元素
for i in list2:
    # 如果元素是偶数
    if i % 2 == 0:
        # 输出该元素
        print(i)
"""
期望输出：
2
10
12
4
"""
