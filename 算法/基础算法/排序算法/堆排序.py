# 堆排序是一种高效的排序算法，常用于大数据量的排序场景，比如排序100GB的数据。
# 堆排序的核心是建立一个堆，堆是一种完全二叉树，分为大根堆和小根堆。
# 大根堆的每个节点都大于等于其子节点，小根堆的每个节点都小于等于其子节点。
# 堆排序的过程分为两个步骤：建堆和排序。
# 建堆的过程是将无序的序列构建成一个堆，排序的过程是将堆顶元素与末尾元素交换，然后重新调整堆，直到整个序列有序。

# 下面是一个使用堆排序的例子，对一个列表进行排序。
# 堆排序
def heap_sort(arr):
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一个个取出元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 将当前最大值放到数组末尾
        heapify(arr, i, 0)


# 调整堆
def heapify(arr, n, i):
    largest = i  # 初始化最大值为根节点
    l = 2 * i + 1  # 左子节点
    r = 2 * i + 2  # 右子节点

    # 如果左子节点比根节点大，则更新最大值
    if l < n and arr[l] > arr[largest]:
        largest = l

    # 如果右子节点比根节点大，则更新最大值
    if r < n and arr[r] > arr[largest]:
        largest = r

    # 如果最大值不是根节点，则交换根节点和最大值，并继续调整堆
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # 递归调整堆


# 测试
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)  # [5, 6, 7, 11, 12, 13]
