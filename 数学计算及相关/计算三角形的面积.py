while True:
    a = float(input('输入第一条边长:'))
    b = float(input('输入第二条边长:'))
    c = float(input('输入第三条边长:'))

    # 判断三条边是否能组成三角形
    if a + b > c and a + c > b and b + c > a:
        # 计算半周长
        s = (a + b + c) / 2

        # 计算面积
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("三角形的面积为 %0.2f" % area)

        choice = input('是否继续计算？(y/n): ')
        if choice.lower() != 'y':
            break
    else:
        print('这三条边无法组成三角形，请重新输入！')