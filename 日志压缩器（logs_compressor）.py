# 脚本名称：logs.py
# 作者：Craig Richards
# 创建日期：2011年10月13日
# 上次修改日期：2016年2月14日
# 版本：1.2
#
# 修改：1.1-添加变量zip_program，以便您可以为任何操作系统设置zip程序，因此要在不同的操作系统上运行，只需更改这两个变量的位置。
#      1.2-整理注释和语法
#
# 描述：此脚本将在给定目录中搜索所有*.log文件，使用您指定的程序将它们压缩，然后对它们进行日期时间戳。

import os  # 加载库模块
from time import strftime  # 从时间中仅加载strftime模块

logsdir = "c:\puttylogs"  # 设置变量logsdir
zip_program = "zip.exe"  # 设置变量zip_program-1.1

for files in os.listdir(logsdir):  # 查找目录中的所有文件
    if files.endswith(".log"):  # 检查目录中的文件是否以.log结尾
        files1 = (
                files + "." + strftime("%Y-%m-%d") + ".zip"
        )  # 创建变量files1，这是目录中的文件，然后我们添加一个带有日期和zip扩展名的后缀
        os.chdir(logsdir)  # 更改目录到logsdir
        os.system(
            zip_program + " " + files1 + " " + files
        )  # 将日志压缩为每个服务器的日期zip文件。-1.1
        os.remove(files)  # 删除原始日志文件
