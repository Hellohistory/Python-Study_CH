# 打印程序名称和说明
print("\n### 元音字母计数器 ###\n")

# 要求用户输入一个字符串
string = input("请输入一个字符串:").lower()

# 创建一个包含元音字母的列表
vowels = ["a", "e", "i", "o", "u"]

# 初始化元音字母计数器
vowelscounter = 0

# 创建一个函数用于检查字符是否为元音字母
def checkVowels(letter):
    for i in range(len(vowels)):
        if letter == vowels[i]:
            return True
    return False

# 对输入的字符串进行遍历，检查其中的每个字符是否为元音字母，并统计元音字母的数量
for i in range(len(string)):
    if checkVowels(string[i]):
        vowelscounter = vowelscounter + 1

# 输出统计结果
print(f"\n### 在字符串中找到了 {vowelscounter} 个元音字母。###")
