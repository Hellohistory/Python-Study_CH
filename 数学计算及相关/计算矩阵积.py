# 输入两个矩阵：

# 矩阵1：

rows = int(input("输入矩阵1的行数"))
columns = int(input("输入矩阵1的列数"))
matrix1 = []
row = []

for i in range(0, rows):
    for j in range(0, columns):
        element = int(input("输入元素"))
        row.append(element)
    print("一行输入完成")
    matrix1.append(row)
    row = []

print("矩阵1为：\n")
for row in matrix1:
    print(row)
A = matrix1

# 矩阵2：

rows_ = columns
columns_ = int(input("输入矩阵2的列数"))
row = []
matrix2 = []

for i in range(0, rows_):
    for j in range(0, columns_):
        element = int(input("输入元素"))
        row.append(element)
    print("一行输入完成")
    matrix2.append(row)
    row = []

print("矩阵2为：\n")
for row in matrix2:
    print(row)

B = matrix2

# 创建空的结果矩阵：

result = []
for i in range(0, rows):
    for j in range(0, columns_):
        row.append(0)
    result.append(row)
    row = []
print("\n")
print("结果矩阵的结构：")
for row in result:
    print(row)

# 两个矩阵的乘法：

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("\n")
print("两个矩阵的乘积为：\n")

for row in result:
    print(row)
