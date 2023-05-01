# 定义一个字典，用于存储生日信息
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# 无限循环，直到用户退出
while True:
    # 提示用户输入名字
    print('请输入一个名字: (留空退出)')
    name = input()

    # 如果名字为空，则退出循环
    if name == '':
        break

    # 如果名字在字典中，则输出生日信息
    if name in birthdays:
        print(birthdays[name] + ' 是 ' + name + ' 的生日')

    # 如果名字不在字典中，则输出没有找到该名字的生日信息
    else:
        print('我没有 ' + name + ' 的生日信息')

    # 提示用户输入生日信息
    print('请输入他们的生日信息')
    bday = input()

    # 将生日信息添加到字典中
    birthdays[name] = bday

    # 输出更新后的生日信息
    print('生日数据库已更新')
