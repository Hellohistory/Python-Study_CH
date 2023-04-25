# 定义创建一个空栈的函数
def createStack():
    stack = []
    return stack


# 定义获取栈大小的函数
def size(stack):
    return len(stack)


# 当栈的大小为 0 时，判断栈是否为空
def isEmpty(stack):
    if size(stack) == 0:
        return True


# 将元素添加到栈中
def push(stack, item):
    stack.append(item)


# 从栈中移除元素
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()


# 使用栈来反转字符串
def reverse(string):
    n = len(string)

    # 创建一个空栈
    stack = createStack()

    # 将字符串的每个字符入栈
    for i in range(0, n, 1):
        push(stack, string[i])

    # 由于所有字符都被保存在栈中，所以将字符串置为空
    string = ""

    # 将栈中的元素依次弹出并添加到字符串中
    for i in range(0, n, 1):
        string += pop(stack)

    return string


# 主程序，用于测试以上函数
string = "GeeksQuiz"
string = reverse(string)
print("反转后的字符串为：" + string)

# 代码作者：Yash
