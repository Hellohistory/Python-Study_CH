"""
通过交换相邻元素的位置，将较大的元素逐渐“冒泡”到最后的位置，实现排序。
假设有一个公司有100名员工，他们每年的绩效评定分为A、B、C、D四个等级。
现在要将员工按照绩效从高到低进行排名。这时候可以使用冒泡排序来实现。
首先，将每个员工的绩效评定等级转换为数字，比如A为4，B为3，C为2，D为1。
然后，将每个员工的绩效评定分数作为一个元素存储在一个列表中，列表中的每个元素包括员工的姓名、绩效评定等级对应的数字和绩效评定分数。
最后，使用冒泡排序对这个列表按照绩效评定分数进行排序，从高到低排名。排名前几的员工就是公司的高绩效员工。
"""
def bubble_sort_employees(employees):
    n = len(employees)
    # 外层循环控制排序次数
    for i in range(n):
        # 内层循环控制每次排序中的比较次数
        for j in range(n-i-1):
            # 如果前面的元素的绩效评定分数小于后面的元素的绩效评定分数，则交换它们的位置
            if employees[j][2] < employees[j+1][2]:
                employees[j], employees[j+1] = employees[j+1], employees[j]
    return employees

# 员工列表，每个元素包括员工的姓名、绩效评定等级对应的数字和绩效评定分数
employees = [('张三', 4, 80), ('李四', 3, 90), ('王五', 2, 70), ('赵六', 4, 95), ('钱七', 1, 60)]

# 对员工按照绩效评定分数进行排序
sorted_employees = bubble_sort_employees(employees)

# 输出排序后的结果
for i, employee in enumerate(sorted_employees):
    print(f"{i+1}. {employee[0]}，绩效评定分数：{employee[2]}")