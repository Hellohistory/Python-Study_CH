class Node:
    def __init__(self, data):
        self.data = data  # 节点存储的数据
        self.next = None  # 下一个节点的引用


class Linked_List:
    def __init__(self):
        self.head = None  # 链表的头节点

    def Insert_At_End(self, new_data):
        new_node = Node(new_data)  # 创建一个新节点
        if self.head is None:
            self.head = new_node  # 如果链表为空，将新节点设置为头节点
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node  # 找到链表末尾，将新节点链接到末尾

    def Delete(self, key):
        temp = self.head
        if temp is None:
            return "无法删除！"
        else:
            if temp.data == key:
                self.head = temp.next
                temp = None
        while temp is not None:
            prev = temp
            temp = temp.next
            if temp is None:
                return
            curr = temp.next
            if temp.data == key:
                prev.next = curr
                return

    def Display(self):
        temp = self.head
        while temp:
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    L_list = Linked_List()
    L_list.Insert_At_End(1)
    L_list.Insert_At_End(2)
    L_list.Insert_At_End(3)
    L_list.Insert_At_End(4)
    L_list.Insert_At_End(5)
    L_list.Insert_At_End(6)
    L_list.Insert_At_End(7)
    print("链表内容：")
    L_list.Display()
    print("删除后的链表内容：")
    L_list.Delete(3)
    L_list.Display()