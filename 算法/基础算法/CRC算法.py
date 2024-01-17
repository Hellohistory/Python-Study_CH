"""
CRC（Cyclic Redundancy Check，循环冗余校验）算法是一种常用的数据校验方法，
主要用于检测在数字通信或存储传输过程中的数据传输错误。
CRC算法通过将数据进行一定的处理，得到一个校验码，将该校验码附加到数据后面传输。
接收方同样对传输过来的数据进行一定的处理，得到一个新的校验码。
如果接收方计算得到的校验码与传输过来的校验码一致，则说明数据在传输过程中没有发生错误；
反之，如果校验码不一致，则说明数据在传输过程中出现了错误，需要进行重传或其他处理。
CRC算法具有高效、简单、可靠的特点，被广泛应用于数字通信、存储、处理等领域。
"""


def crc_check(data, div):
    l = len(div)  # 获取除数的长度
    ct = 0  # 初始化计数器
    data = [int(i) for i in data]  # 将数据转换为整数列表
    div = [int(i) for i in div]  # 将除数转换为整数列表
    zero = [0 for i in range(l)]  # 初始化零列表
    temp_data = [data[i] for i in range(l)]  # 获取数据的前l位
    result = []  # 初始化商列表
    for j in range(len(data) - len(div) + 1):
        print("被除数: ", temp_data)  # 输出被除数
        msb = temp_data[0]  # 获取被除数的最高位
        if msb == 0:
            result.append(0)  # 如果最高位为0，则商为0
            for i in range(l - 1, -1, -1):
                temp_data[i] = temp_data[i] ^ zero[i]  # 异或操作
        else:
            result.append(1)  # 如果最高位为1，则商为1
            for i in range(l - 1, -1, -1):
                temp_data[i] = temp_data[i] ^ div[i]  # 异或操作
        temp_data.pop(0)  # 弹出最高位
        if l + j < len(data):
            temp_data.append(data[l + j])  # 添加下一位数据
    crc = temp_data  # 获取余数
    print("商: ", result, "余数: ", crc)  # 输出商和余数
    return crc


# 计算 CRC 校验值
while True:
    print("请输入数据: ")
    data = input()  # 可以使用 int(input()) 来将输入的字符串转换为整数
    print("请输入除数: ")
    div = input()  # 可以使用 int(input()) 来将输入的字符串转换为整数
    try:
        original_data = data
        data = data + ("0" * (len(div) - 1))  # 在数据末尾添加0
        crc = crc_check(data, div)  # 计算CRC校验值
        crc_str = ""
        for c in crc:
            crc_str += c
        print("发送的数据: ", original_data + crc_str)  # 输出发送的数据
        sent_data = original_data + crc_str
        print("如果 CRC 校验无误，那么再次应用 CRC 算法得到的余数/校验值应该为零")
        crc = crc_check(sent_data, div)  # 再次计算CRC校验值
        remainder = crc
        print("接收方得到的余数/校验值为: ", remainder)  # 输出接收方得到的余数/校验值
        ch = input("是否继续？（Y/N）：")
        if ch == "N" or ch == "n":
            break
        else:
            continue
    except ValueError:
        print("输入的除数必须为数字，请重新输入！")
    except ZeroDivisionError:
        print("除数不能为零，请重新输入！")
