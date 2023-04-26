class Stack:
    def __init__(self):
        self.items = []  # 初始化一个空列表

    def push(self, item):
        self.items.append(item)  # 添加元素到列表末尾

    def pop(self):
        return self.items.pop()  # 弹出并返回列表末尾元素

    def is_empty(self):
        return self.items == []  # 判断列表是否为空

    def peek(self):
        return self.items[-1]  # 返回列表末尾元素

    def display(self):
        return self.items  # 返回列表所有元素

# 判断两个括号是否匹配
def is_same(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False

# 判断括号是否平衡
def is_balanced(check_string):
    s = Stack()  # 创建一个栈
    index = 0
    is_bal = True
    while index < len(check_string) and is_bal:
        paren = check_string[index]  # 获取字符串中的字符
        if paren in "{[(":  # 如果是左括号，入栈
            s.push(paren)
        else:
            if s.is_empty():  # 如果是右括号，判断栈是否为空
                is_bal = False
            else:
                top = s.pop()  # 弹出栈顶元素
                if not is_same(top, paren):  # 判断栈顶元素和当前元素是否匹配
                    is_bal = False
        index += 1

    if s.is_empty() and is_bal:  # 判断栈是否为空且括号是否匹配
        return True
    else:
        return False


print(is_balanced("[((())})]"))  # 输出 False，因为括号不平衡