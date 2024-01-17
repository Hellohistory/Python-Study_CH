"""
以一个元素为基准（通常是第一个或最后一个元素），将待排序序列分为小于基准值和大于基准值两部分，递归地对两部分进行排序。
这是一个使用快速排序对学生成绩进行排序的示例，
其中学生信息以字典的形式存储在列表中，我们按照学生成绩从高到低的顺序进行排序
"""


def quick_sort(students, left, right):
    if left < right:
        pivot = partition(students, left, right)
        quick_sort(students, left, pivot - 1)
        quick_sort(students, pivot + 1, right)


def partition(students, left, right):
    pivot = students[right]['成绩']
    i = left - 1
    for j in range(left, right):
        if students[j]['成绩'] >= pivot:
            i += 1
            students[i], students[j] = students[j], students[i]
    students[i + 1], students[right] = students[right], students[i + 1]
    return i + 1


students = [
    {'姓名': '张三', '年龄': 20, '成绩': 85},
    {'姓名': '李四', '年龄': 22, '成绩': 90},
    {'姓名': '王五', '年龄': 19, '成绩': 92},
    {'姓名': '赵六', '年龄': 21, '成绩': 88},
    {'姓名': '田七', '年龄': 20, '成绩': 80},
]

quick_sort(students, 0, len(students) - 1)

for student in students:
    print(student)
