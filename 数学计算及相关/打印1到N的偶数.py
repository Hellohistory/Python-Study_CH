# Python程序：打印1到N的偶数

maximum = int(input("请输入最大值: ")) # 询问用户输入最大值

number = 1 # 初始化计数器

while number <= maximum: # 当计数器小于等于最大值时
    if number % 2 == 0: # 如果计数器是偶数
        print("{0}".format(number)) # 打印计数器
    number = number + 1 # 计数器加1
