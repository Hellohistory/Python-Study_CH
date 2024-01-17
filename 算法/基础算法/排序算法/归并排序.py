"""
归并排序通常适用于需要稳定排序算法的场景，如对于一些包含多个字段的数据记录进行排序时，需要保证各个字段的稳定性，这时可以采用归并排序。
假设我们有一个在线商城，需要根据用户对商品的评价进行排序，以便展示给其他用户参考。
具体地，我们可以定义每个评价包含三个字段：评价人姓名、评价时间和评价星级（1~5），并且我们将所有评价存储在一个包含多个评价的列表中。
"""


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i]['评价'] > right[j]['评价']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


# 测试数据
reviews = [
    {'姓名': '张三', '时间': '2022-04-01', '评价': 5},
    {'姓名': '李四', '时间': '2022-03-15', '评价': 4},
    {'姓名': '王五', '时间': '2022-03-20', '评价': 3},
    {'姓名': '赵六', '时间': '2022-04-05', '评价': 5},
    {'姓名': '田七', '时间': '2022-04-02', '评价': 2},
]

# 对评价进行排序
sorted_reviews = merge_sort(reviews)

# 输出排序结果
for review in sorted_reviews:
    print(f"{review['姓名']} 于 {review['时间']} 评价了 {review['评价']} 分")
