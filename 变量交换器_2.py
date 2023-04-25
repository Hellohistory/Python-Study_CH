# 定义变量 x 和 y
x = 5
y = 10

# 如果需要从用户那里获取输入，可以使用下面两行代码，并将上面的 x 和 y 赋值注释掉
# x = input('请输入 x 的值：')
# y = input('请输入 y 的值：')

# 创建一个临时变量并交换 x 和 y 的值
temp = x
x = y
y = temp

# 在 Python 中我们也可以不使用第三个变量就进行交换
x, y = y, x

# 输出交换后的 x 和 y 的值
print(x, y)
# 输出结果是 10, 5

print('交换后，x 的值为：{}'.format(x))
print('交换后，y 的值为：{}'.format(y))