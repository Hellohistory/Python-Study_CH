import matplotlib.pyplot as plt
import numpy as np


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

    print("接下来，程序将进行500次迭代，并输出每次迭代的结果:")
    xs = []
    ys = []
    for i in range(500):
        xs.append(i)
        ys.append(x)
        x = 3.9 * x * (1 - x)  # 混沌函数的计算公式
        print(x)  # 输出每次迭代的结果

    plt.imshow(np.array([ys]), cmap='viridis', aspect='auto', extent=[0, 500, 0, 1])
    plt.xlabel('迭代次数')
    plt.ylabel('结果')
    plt.title('混沌函数演示')
    plt.show()


if __name__ == "__main__":
    main()
