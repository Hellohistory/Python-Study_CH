# 脚本名称：create_dir_if_not_there.py
# 作者：Craig Richards
# 创建时间：2012年1月9日
# 上次修改：2015年10月22日
# 版本：1.0.1
# 修改：添加异常
# 1.0.1 整理注释和语法
# 描述：检查用户主目录中是否存在目录，如果不存在则创建它

import os  # 导入OS模块

MESSAGE = "该目录已经存在。"
TESTDIR = "testdir"
try:
    home = os.path.expanduser(
        "~"
    )  # 通过扩展用户设置的主目录来设置变量home
    print(home)  # 打印位置

    if not os.path.exists(
        os.path.join(home, TESTDIR)
    ):  # os.path.join()用于安全地创建完整路径
        os.makedirs(
            os.path.join(home, TESTDIR)
        )  # 如果不存在，则在其主目录中创建目录
    else:
        print(MESSAGE)
except Exception as e:
    print(e)