import matplotlib.pyplot as plt

def main():
    print("本程序演示一个混沌函数的相图。")

    while True:
        try:
            x0 = float((input("请输入初始 x 值(0到1之间):")))
            y0 = float((input("请输入初始 y 值(0到1之间):")))
            if 0 < x0 and x0 < 1 and 0 < y0 and y0 < 1:
                break
            else:
                print("请输入正确的数字。")
        except Exception as e:
            print("请输入正确的数字。")

    print("接下来，程序将进行1000次迭代，并绘制相图:")

    x = x0
    y = y0

    xs = []
    ys = []

    for i in range(1000):
        xs.append(x)
        ys.append(y)
        x, y = 3.9 * x * (1 - x), 3.9 * y * (1 - y) # 混沌系统的计算公式

    plt.scatter(xs, ys, s=0.1, c='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('混沌系统相图')
    plt.show()

if __name__ == "__main__":
    main()