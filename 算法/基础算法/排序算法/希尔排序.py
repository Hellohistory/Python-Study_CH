"""
插入排序的一种改进版本，通过比较相隔一定距离的元素，以逐渐减小这个距离，最终使整个序列有序。
"""
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 初始间隔数
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j-gap] > arr[j]:
                arr[j-gap], arr[j] = arr[j], arr[j-gap] # 交换元素
                j -= gap
        gap //= 2 # 缩小间隔数
    return arr
