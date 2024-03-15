class Node:  # 定义节点类
    def __init__(self, data):  # 定义节点类的初始化函数
        self.data = data  # 节点数据
        self.next = None  # 节点指针


class Linked_List:  # 定义链表类
    def __init__(self):  # 定义链表类的初始化函数
        self.head = None  # 链表头指针

    def Insert_At_Beginning(self, new_data):  # 定义链表类的插入函数
        new_node = Node(new_data)  # 创建新节点
        if self.head is None:  # 如果链表为空
            self.head = new_node  # 新节点为头节点
            return
        new_node.next = self.head  # 新节点指向头节点
        self.head = new_node  # 新节点为头节点

    def Add_two_no(self, First, Second):  # 定义链表类的加法函数
        prev = None  # 定义前一个节点
        temp = None  # 定义当前节点
        carry = 0  # 定义进位
        while First is not None or Second is not None:  # 如果两个链表都不为空
            first_data = 0 if First is None else First.data  # 如果第一个链表为空，则第一个链表的数据为0
            second_data = 0 if Second is None else Second.data  # 如果第二个链表为空，则第二个链表的数据为0
            Sum = carry + first_data + second_data  # 计算两个节点的和
            carry = 1 if Sum >= 10 else 0  # 如果和大于等于10，则进位为1，否则为0
            Sum = Sum if Sum < 10 else Sum % 10  # 如果和小于10，则和为Sum，否则和为Sum%10
            temp = Node(Sum)  # 创建新节点
            if self.head is None:  # 如果链表为空
                self.head = temp  # 新节点为头节点
            else:
                prev.next = temp  # 前一个节点指向当前节点
            prev = temp  # 前一个节点为当前节点
            if First is not None:  # 如果第一个链表不为空
                First = First.next  # 第一个链表指向下一个节点
            if Second is not None:  # 如果第二个链表不为空
                Second = Second.next  # 第二个链表指向下一个节点
        if carry > 0:  # 如果进位大于0
            temp.next = Node(carry)  # 创建新节点

    def Display(self):  # 定义链表类的展示函数
        temp = self.head  # 定义当前节点
        while temp:  # 如果当前节点不为空
            print(temp.data, "->", end=" ")  # 输出当前节点的数据
            temp = temp.next  # 当前节点指向下一个节点
        print("None")  # 输出None

if __name__ == "__main__":
    First = Linked_List()  # 创建第一个链表
    Second = Linked_List()  # 创建第二个链表
    First.Insert_At_Beginning(6)  # 在第一个链表的头部插入6
    First.Insert_At_Beginning(4)  # 在第一个链表的头部插入4
    First.Insert_At_Beginning(9)  # 在第一个链表的头部插入9

    Second.Insert_At_Beginning(2)  # 在第二个链表的头部插入2
    Second.Insert_At_Beginning(2)  # 在第二个链表的头部插入2

    print("第一个链表: ")  # 输出第一个链表
    First.Display()  # 展示第一个链表
    print("第二个链表: ")  # 输出第二个链表
    Second.Display()  # 展示第二个链表

    Result = Linked_List()  # 创建结果链表
    Result.Add_two_no(First.head, Second.head)  # 将第一个链表和第二个链表相加
    print("最终结果: ")  # 输出最终结果
    Result.Display()  # 展示最终结果
