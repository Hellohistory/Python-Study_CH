import matplotlib.pyplot as plt


def main():
    print("本程序演示 Rossler 混沌系统的特性。")

    # 初始化变量
    x = 0.1
    y = 0.0
    z = 0.0

    # 设置参数
    a = 0.2
    b = 0.2
    c = 5.7

    # 创建空列表，用于保存每次迭代的结果
    xs = []
    ys = []
    zs = []

    # 迭代 10000 次，并保存每次迭代的结果
    for i in range(10000):
        xs.append(x)
        ys.append(y)
        zs.append(z)

        dx = -y - z
        dy = x + a * y
        dz = b + z * (x - c)
        x += 0.01 * dx
        y += 0.01 * dy
        z += 0.01 * dz

    # 绘制三维图形
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Rossler System')
    plt.show()

if __name__ == "__main__":
    main()