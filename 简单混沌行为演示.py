def main():
    print("本程序演示一个混沌函数的特性。")

    while True:
        try:
            x = float((input("请输入一个0到1之间的数字:")))
            if 0 < x and x < 1:
                break
            else:
                print("请输入正确的数字。")
        except Exception as e:
            print("请输入正确的数字。")

    print("接下来，程序将进行10次迭代，并输出每次迭代的结果:")
    for i in range(10):
        x = 3.9 * x * (1 - x) # 混沌函数的计算公式
        print(x) # 输出每次迭代的结果


if __name__ == "__main__":
    main()