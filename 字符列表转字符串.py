# Python程序，将字符列表转换为字符串

def convert(s):
    # 初始化字符串为""
    new = ""

    # 遍历字符串
    for x in s:
        new += x

        # 返回字符串
    return new


# 主函数
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))