# 定义函数 rotate，用于对输入字符串进行逐个字母的循环移位
def rotate(n):
    a = list(n)
    if len(a) == 0:
        return print([])
    l = []
    for i in range(1, len(a) + 1):
        a = [a[(i + 1) % (len(a))] for i in range(0, len(a))]
        l += ["".join(a)]
    print(l)

# 获取用户输入的字符串，并进行循环移位操作
string = str(input('请输入您想要移位的字符串:'))
print("您输入的字符串是:", string)
print("循环移位后的结果是:")
rotate(string)

# 示例输入: Python
# 输出结果:
# 循环移位后的结果是:
# ['ythonp', 'thonpy', 'honpyt', 'onpyth', 'npytho', 'python']
