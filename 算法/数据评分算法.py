def score(source_data: list, weights: list, *args) -> list:
    """分析数据集并使用基于范围的百分比接近算法计算得分。
    同时计算线性最大似然估计。

    参数:
        source_data (list): 要处理的数据集。
        weights (list): 与数据集中每列对应的权重。
            如果较低的值在数据集中更重要，则为0，
            如果较高的值在数据集中更重要，则为1。
    可选参数:
        "score_lists" (str): 返回包含每列分数的列表。
        "scores" (str): 只返回最终得分。

    抛出:
        ValueError: 权重只能为0或1（int类型）。

    返回:
        list: 在数据集最后附加得分后的源数据集。
    """

    # 获取数据
    data_lists = []
    for item in source_data:
        for i, val in enumerate(item):
            try:
                data_lists[i].append(float(val))
            except IndexError:
                data_lists.append([])
                data_lists[i].append(float(val))

    # 计算分数
    score_lists = []
    for dlist, weight in zip(data_lists, weights):
        mind = min(dlist)
        maxd = max(dlist)

        score = []
        if weight == 0:
            for item in dlist:
                try:
                    score.append(1 - ((item - mind) / (maxd - mind)))
                except ZeroDivisionError:
                    score.append(1)

        elif weight == 1:
            for item in dlist:
                try:
                    score.append((item - mind) / (maxd - mind))
                except ZeroDivisionError:
                    score.append(0)

        else:
            raise ValueError("提供了无效的权重值 %f" % (weight))

        score_lists.append(score)

    # 返回分数列表
    if "score_lists" in args:
        return score_lists

    # 初始化最终得分
    final_scores = [0 for i in range(len(score_lists[0]))]

    # 生成最终得分
    for i, slist in enumerate(score_lists):
        for j, ele in enumerate(slist):
            final_scores[j] = final_scores[j] + ele

    # 只返回得分
    if "scores" in args:
        return final_scores

    # 将得分附加到源数据集
    for i, ele in enumerate(final_scores):
        source_data[i].append(ele)

    return source_data


def score_columns(source_data: list, columns: list, weights: list) -> list:
    """使用基于范围的百分比接近算法分析数据文件，并计算线性最大似然估计。

    参数:
        source_data (list): 要处理的数据集。
        columns (list): 要评分的数据集列的索引。
        weights (list): 与数据集中每一列对应的权重。
            如果较低的值在数据集中更重要，则为0，
            如果较高的值在数据集中更重要，则为1。

    抛出:
        ValueError: 权重只能为0或1（int类型）。

    返回:
        list: 在数据集最后附加得分后的源数据集。
    """

    temp_data = []
    for item in source_data:
        temp_data.append([item[c] for c in columns])

    if len(weights) > len(columns):
        weights = [weights[item] for item in columns]

    for i, sc in enumerate(score(temp_data, weights, "scores")):
        source_data[i].append(sc)

    return source_data


# 示例数据集
data_set = [
    [20, 60, 2012],
    [22, 50, 2011],
    [23, 90, 2015],
    [16, 210, 2010]
]

# 示例权重
Weights = [0, 0, 1]

# 使用score函数计算得分并将结果打印出来
print(score(data_set, Weights))
# 输出：
# [[20, 60, 2012, 1.7660714285714287], [22, 50, 2011, 1.3428571428571427], [23, 90, 2015, 1.75], [16, 210, 2010, 1.0]]

# 使用score函数只返回最终得分并将结果打印出来
print(score(data_set, Weights, "scores"))
# 输出：
# [1.7660714285714287, 1.3428571428571427, 1.75, 1.0]

# 使用score_columns函数计算得分并将结果打印出来
print(score_columns(data_set, [0, 2], Weights))
# 输出：
# [[20, 60, 2012, 1.7660714285714287, 0.8285714285714286],
# [22, 50, 2011, 1.3428571428571427, 0.3428571428571429], [23, 90, 2015, 1.75, 1.0], [16, 210, 2010, 1.0, 1.0]]
