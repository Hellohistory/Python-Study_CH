def generate(A, k):
    # 如果只有一个元素，直接输出
    if k == 1:
        print(A)
        return
    else:
        # 递归调用generate函数
        for i in range(k):
            generate(A, k - 1)
            # 如果i小于k-1
            if (i < k - 1):
                # 如果k是偶数
                if k % 2 == 0:
                    # 交换A[i]和A[k-1]
                    A[i], A[k - 1] = A[k - 1], A[i]
                else:
                    # 否则交换A[0]和A[k-1]
                    A[0], A[k - 1] = A[k - 1], A[0]


# 测试用例
A = [1, 2, 3, 4]
x = len(A)
generate(A, x)
