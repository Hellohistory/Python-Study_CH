my_string = input("输入一个字符串以计算辅音字母的数量:")
string_check = [
    "a",
    "e",
    "i",
    "o",
    "u",
    "A",
    "E",
    "I",
    "O",
    "U",
]  # 用于检查元音字母的列表


def count_con(string):
    c = 0
    for i in range(len(string)):
        if (
                string[i] not in string_check
        ):  # 如果字符不是元音字母，就增加计数器的值
            c += 1
    return c


counter = count_con(my_string)
print(f"{my_string}中的辅音字母数量为{counter}。")
