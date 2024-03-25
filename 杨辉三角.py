def generate_pascals_triangle(num_rows):
    """
    生成杨辉三角

    参数:
    num_rows (int): 杨辉三角的行数

    返回:
    list: 杨辉三角的列表
    """
    if num_rows == 0:
        return []

    triangle = [[1]]
    for i in range(1, num_rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

# 示例:
triangle = generate_pascals_triangle(5)
for row in triangle:
    print(row)

