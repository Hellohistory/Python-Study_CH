"""
将待排序序列分为已排序和未排序两部分，每次将未排序序列中的一个元素插入到已排序序列的适当位置。
假设我们有一个包含多个学生信息的列表，每个学生都是一个字典，包含了学生姓名、年龄、成绩等信息。
我们可以使用插入排序对学生列表进行排序，使得成绩较高的学生排在前面，成绩较低的学生排在后面。
"""
students = [
    {'姓名': '张三', '年龄': 20, '成绩': 85},
    {'姓名': '李四', '年龄': 22, '成绩': 90},
    {'姓名': '王五', '年龄': 19, '成绩': 92},
    {'姓名': '赵六', '年龄': 21, '成绩': 88},
    {'姓名': '田七', '年龄': 20, '成绩': 80},
]

def insertion_sort_students(student_list):
    for i in range(1, len(student_list)):
        current_student = student_list[i]
        j = i - 1
        while j >= 0 and student_list[j]['成绩'] < current_student['成绩']: #根据成绩来进行排序
            student_list[j+1] = student_list[j]
            j -= 1
        student_list[j+1] = current_student
    return student_list

sorted_students = insertion_sort_students(students)
print(sorted_students)