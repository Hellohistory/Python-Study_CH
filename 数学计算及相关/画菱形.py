def draw_diamond(n):
    if n % 2 != 0:
        k = 1
        while k <= n:
            print(" " * int((n - k) / 2) + "*" * k + " " * int((n - k) / 2)) # 打印一行
            k += 2

        j = 1
        while (n - 2 * j) >= 1:
            print(" " * j + "*" * (n - 2 * j) + " " * (j)) # 打印一行
            j += 1
    else:
        print("不是奇数。不能画出菱形 :(") # 打印错误信息


n = int(input("输入一个奇数: "))
draw_diamond(n) # 调用函数