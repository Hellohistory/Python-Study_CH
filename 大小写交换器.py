# 定义函数 swap_case，将字符串中的大小写字母进行交换
def swap_case(s):
    return s.swapcase()

# 如果该脚本作为主程序运行，则获取用户输入的字符串，交换大小写字母，并输出结果
if __name__ == "__main__":
    s = input('请输入需要转换的字符串:')
    result = swap_case(s)
    print(result)