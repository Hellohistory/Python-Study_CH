"""
每次找到最小的元素，放到已排序序列的末尾。
假设我们有一个包含多个人的名单，每个人都有一个唯一的身份证号码和一个分数。
现在我们想要按照分数从高到低的顺序对名单进行排序，以便确定分数排名前几位的人员。
"""
name_list = [
    {'id': '1234567890', '成绩': 95},
    {'id': '2345678901', '成绩': 85},
    {'id': '3456789012', '成绩': 92},
    {'id': '4567890123', '成绩': 78},
    {'id': '5678901234', '成绩': 88},
    {'id': '6789012345', '成绩': 90},
    {'id': '7890123456', '成绩': 82},
    {'id': '8901234567', '成绩': 86},
    {'id': '9012345678', '成绩': 91},
    {'id': '0123456789', '成绩': 89}
]

def sort_by_score(name_list):
    n = len(name_list)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if name_list[j]['成绩'] > name_list[max_index]['成绩']:
                max_index = j
        name_list[i], name_list[max_index] = name_list[max_index], name_list[i]
    return name_list

sorted_list = sort_by_score(name_list)
print(sorted_list)