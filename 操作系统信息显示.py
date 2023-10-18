# 脚本名称    ：osinfo.py
# 作者        ：{'geekcomputers': 'Craig Richards', 'dmahugh': 'Doug Mahugh','rutvik1010':'Rutvik Narayana Nadimpally','y12uc231': 'Satyapriya Krishna', 'minto4644':'Mohit Kumar'}
# 创建时间    ：2012年4月5日
# 上次修改时间：2016年7月19日
# 版本号      ：1.0

# 修改1      ：再次将配置文件更改为列表。顺序很重要。每次运行脚本时，我们不希望看到不同的排序。
# 修改2      ：修复了检查所有属性的AttributeError。使用hasttr（）。
# 修改3      ：从配置文件中删除了“：”后面的属性。

# 描述        ：显示有关运行此脚本的操作系统的一些信息
"""
architecture: 系统的处理器架构（如x86或者x64）
linux_distribution: 在Linux上运行时，发行版的信息（如Ubuntu或者CentOS）
mac_ver: 在Mac OS上运行时，版本信息（如10.15.2）
machine: 系统的硬件架构（如x86_64）
node: 系统的网络主机名（如果有）
platform: 系统的平台标识符（如Windows或者Linux）
processor: 处理器的名称（如Intel Core i5）
python_build: Python的构建信息
python_compiler: Python的编译器信息
python_version: Python的版本号
release: 系统的版本号
system: 系统的名称（如Windows或者Linux）
uname: 包含系统信息的元组（如('Linux', 'ubuntu', '5.4.0-42-generic', '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020', 'x86_64')）
version: 系统的版本号
"""
import platform as pl

profile = [
    "architecture",
    "linux_distribution",
    "mac_ver",
    "machine",
    "node",
    "platform",
    "processor",
    "python_build",
    "python_compiler",
    "python_version",
    "release",
    "system",
    "uname",
    "version",
]


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


print("这个脚本可以显示有关运行此脚本的操作系统的一些信息。\n")
print("以下是您的操作系统信息:\n")

for key in profile:
    if hasattr(pl, key):
        print(key + bcolors.BOLD + ":" + str(getattr(pl, key)()) + bcolors.ENDC)

print("\n谢谢使用！")
