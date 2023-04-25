# 从 sys 模块中导入 maxsize，用于在栈为空时返回 -infinite
from sys import maxsize

# 创建一个空栈
def createStack():
    stack = []
    return stack

# 判断栈是否为空
def isEmpty(stack):
    return len(stack) == 0

# 向栈中添加元素
def push(stack, item):
    stack.append(item)
    print(item + " 推送到堆栈 ")

# 从栈中删除元素
def pop(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)  # 返回 -infinite
    return stack.pop()

# 查看栈顶元素
def peek(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)  # 返回 -infinite
    return stack[len(stack) - 1]

# 测试代码
stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " 推送到堆栈")
