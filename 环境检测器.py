#  此脚本将检查所需的所有环境变量是否已设置
import os

confdir = os.getenv("my_config")  # 从操作系统环境变量中获取变量 confdir
conffile = "env_check.conf"  # 设置变量 conffile
conffilename = os.path.join(confdir, conffile)  # 将 confdir 和 conffile 连接起来，设置变量 conffilename

for env_check in open(conffilename):  # 打开配置文件并读取所有设置
    env_check = (env_check.strip())  # 将变量本身设置为去除额外文本后的值
    print("[{}]".format(env_check))  # 格式化输出为方括号形式
    newenv = os.getenv(env_check)  # 将变量 newenv 设置为从操作系统获取的当前设置为配置文件中的设置

    if newenv is None:  # 如果变量不存在
        print(env_check, "未设置")  # 打印未设置的信息
    else:  # 如果变量存在
        print("当前设置 for {}={}\n".format(env_check, newenv))  # 打印详细信息
