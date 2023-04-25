"""
这是用Python 3实现的“cat”程序

Unix的“cat”实用程序通过stdin读取文件的内容，
并将其“连接”到stdout。如果没有给出任何文件名，
则程序会从标准输入读取，这意味着它只是将stdin复制到stdout。

在Python中实现这样的程序非常容易，
因此在线上存在无数的示例。这个特定的实现
专注于cat实用程序的基本功能。与Python 3.6或更高版本兼容。

语法：
python3 cat.py [filename1] [filename2] etc...
使用空格分隔文件名。

David Costello（GitHub上的DontEatThemCookies）

v2-2022年3月12日
"""
import sys

def with_files(files):
    """当文件被指定时执行。"""
    try:
        # 读取每个文件的内容并存储它们
        file_contents = [contents for contents in [open(file, encoding='utf-8').read() for file in files]]
    except OSError as err:
        # 当出现错误时执行（例如FileNotFoundError）
        exit(print(f"cat: 读取文件时出错 ({err})"))

    # 将所有文件内容写入标准输出流
    for contents in file_contents:
        sys.stdout.write(contents)

def no_files():
    """当没有文件被指定时执行。"""
    try:
        # 获取输入，输出输入，重复
        while True:
            print(input())
    # Ctrl + C，Ctrl + D的优雅退出
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()

def main():
    """cat程序的入口点。"""
    # 读取传递给程序的参数
    if not sys.argv[1:]:
        no_files()
    else:
        with_files(sys.argv[1:])

if __name__ == "__main__":
    main()