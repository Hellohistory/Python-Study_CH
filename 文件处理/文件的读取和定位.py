from sys import argv

# 从命令行参数获取脚本名和输入文件名
script, input_file = argv

# 打印整个文件内容
def print_all(f):
    print(f.read())

# 将文件指针定位到文件开头
def rewind(f):
    f.seek(0)

# 打印文件中特定行的内容
def print_a_line(line_count, f):
    print(line_count, f.readline())

# 打开指定的输入文件
current_file = open(input_file)

print("首先让我们打印整个文件内容：\n")
print_all(current_file)

print("现在让我们倒回去，有点像磁带倒带。")
rewind(current_file)

print("让我们打印三行：")
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_file.close()
