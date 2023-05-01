# 在给定的数组arr中返回x的位置
# 如果存在，则返回位置，否则返回-1
def binary_search(arr, l, r, x):
    # 基本情况：如果左索引大于右索引，则元素不存在
    if l > r:
        return -1

    # 计算中间索引
    mid = (l + r) // 2

    # 如果元素正好在中间
    if arr[mid] == x:
        return mid

    # 如果元素小于中间值，则它只能存在于左子数组中
    elif arr[mid] > x:
        return binary_search(arr, l, mid - 1, x)

    # 否则元素只能存在于右子数组中
    else:
        return binary_search(arr, mid + 1, r, x)


# 主函数
if __name__ == "__main__":
    # 用户输入数组
    arr = [int(x) for x in input("输入由逗号分隔的元素组成的数组: ").split(",")]

    # 用户输入要搜索的元素
    x = int(input("输入要搜索的元素: "))

    # 调用函数
    result = binary_search(arr, 0, len(arr) - 1, x)

    # 打印输出
    if result != -1:
        print("元素在索引{}处".format(result))
    else:
        print("元素不在数组中")