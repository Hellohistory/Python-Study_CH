from time import sleep

txt = input("请输入要展示的文本:")

ap = ""  # 初始化一个空字符串，用来逐渐累加输入的文本

for let in range(len(txt) - 1):  # 循环次数为文本长度减 1，因为最后一个字符要在外面直接输出
    ap += txt[let]  # 将当前字符加入 ap 字符串中
    print(ap, end="\r")  # 输出 ap 字符串，加上 \r 可以使得下一个字符覆盖上一个字符，从而实现打字机效果
    sleep(0.1)  # 等待一段时间，让打字机效果更加真实

print(txt, end="")  # 输出最后一个字符，注意不要换行
