while True:
    try:
        c = input("请输入您需要查询的字符:")
        if len(c) != 1:
            raise ValueError #当输入的不是一个字符的时候程序会报ValueError错误，因此在这里加上一个错误处理机制
        break
    except ValueError:
        print("输入的不是一个字符，请重新输入！")

try:
    ascii_value = ord(c) #ord()函数是用来返回字符ASCII值的函数
    print("字符 '" + c + "' 的ASCII值为", ascii_value)
except TypeError:
    print("无法获取字符 '" + c + "' 的ASCII值")