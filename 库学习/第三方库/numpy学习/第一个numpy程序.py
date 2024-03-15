import numpy as np

# 一维数组
arr = np.array([1, 2, 3, 4, 5])
print("一维数组:", arr)

# 二维数组
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("二维数组:\n", arr_2d)

# 数组基本操作
print("数组的元素总数:", arr.size)
print("数组的形状:", arr_2d.shape)
print("数组的维数:", arr_2d.ndim)

# 数组切片和索引
print("数组的第一个元素:", arr[0])
print("二维数组的第一行:", arr_2d[0])
