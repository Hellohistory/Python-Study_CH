# 作者：PrajaktaSathe
# 计算正方形、矩形、圆形和三角形的面积的程序
import math as m


def main():
    # 形状：1表示正方形，2表示矩形，3表示圆形，4表示三角形，5表示圆柱体，6表示圆锥体，7表示球体
    shape = int(
        input(
            "1.正方形\n2.矩形\n3.圆形\n4.三角形\n5.圆柱体\n6.圆锥体\n7.球体\n请输入您想要计算的形状编号:"
        )
    )
    if shape == 1:
        side = float(input("请输入边长:"))
        print("正方形的面积 = " + str(side ** 2))
    elif shape == 2:
        l = float(input("请输入长度:"))
        b = float(input("请输入宽度:"))
        print("矩形的面积 = " + str(l * b))
    elif shape == 3:
        r = float(input("请输入半径:"))
        print("圆形的面积 = " + str(m.pi * r * r))
    elif shape == 4:
        base = float(input("请输入底边长:"))
        h = float(input("请输入高:"))
        print("三角形的面积 = " + str(0.5 * base * h))
    elif shape == 5:
        r = float(input("请输入半径:"))
        h = float(input("请输入高:"))
        print("圆柱体的面积 = " + str(m.pow(r, 2) * h * m.pi))
    elif shape == 6:
        r = float(input("请输入半径:"))
        h = float(input("请输入高:"))
        print("圆锥体的面积 = " + str(m.pow(r, 2) * h * 1 / 3 * m.pi))
    elif shape == 7:
        r = float(input("请输入半径:"))
        print("球体的面积 = " + str(m.pow(r, 3) * 4 / 3 * m.pi))
    else:
        print("您选择了错误的选项。")

    restart = input("您是否想计算另一个图形的面积？Y/N:")

    if restart.lower().startswith("y"):
        main()
    elif restart.lower().startswith("n"):
        quit()


main()