def get_user_input(start, end):
    """
    输入：两个整数值
           下限 'start' 和最大值 'end'
           参数不包括在内。

    输出：如果读取成功，则返回读取的整数。

    目的：从命令行读取给定范围内的整数。
             在输入无效时再次询问用户
    """

    loop = True  # 控制while循环

    while loop:

        try:

            # 从控制台读取并转换输入。
            user_input = int(input("请输入您的选择:"))

            # 检查输入是否在给定范围内。
            if user_input > end or user_input < start:

                # 错误情况
                print("请重试。不在有效范围内。")

            else:

                # 有效情况
                loop = False  # 中止while循环

        except ValueError:

            # 错误情况
            print("请重试。只能输入数字")

    return user_input


x = get_user_input(1, 6)
print(x)
# 要求用户输入一些内容，即菜单中的数字选项。
# 当类型！= interger，并且不在给定范围内时，
# 程序会给出错误消息并要求输入新内容。