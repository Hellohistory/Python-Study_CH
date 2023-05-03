import matplotlib.pyplot as plt


def main():
    print("本程序演示一个三维混沌系统的特性。")

    # 初始化变量
    x = 0.1
    y = 0.2
    z = 0.3

    # 设置参数
    a = 10.0
    b = 28.0
    c = 8.0 / 3.0

    # 创建空列表，用于保存每次迭代的结果
    xs = []
    ys = []
    zs = []

    # 迭代 10000 次，并保存每次迭代的结果
    for i in range(10000):
        xs.append(x)
        ys.append(y)
        zs.append(z)

        dx = a * (y - x)
        dy = x * (b - z) - y
        dz = x * y - c * z
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
    ax.set_title('Lorenz System')
    plt.show()

if __name__ == "__main__":
    main()