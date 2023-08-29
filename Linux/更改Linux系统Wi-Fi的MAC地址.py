# 作者- RIZWAN AHMAD

# 简单的Python脚本，用于更改Linux系统上网络接口（Wi-Fi）的MAC地址
import random
from subprocess import PIPE, Popen

# 用于返回终端命令结果的函数
def cret(command):
    process = Popen(args=command, stdout=PIPE, shell=True)
    return process.communicate()[0]

# 生成随机MAC地址的函数
def randmac():
    return [
        0x00,
        0x16,
        0x3E,
        random.randint(0x00, 0x7F),
        random.randint(0x00, 0xFF),
        random.randint(0x00, 0xFF),
    ]

# 将MAC地址转换为字符串形式
def retrandmac(mac):
    return ":".join(map(lambda x: "%02x" % x, mac))

print("                                             +-+-+-+ +-+-+-+-+-+-+-+")
print("                                             |M|A|C| |c|h|a|n|g|e|r|")
print("                                             +-+-+-+ +-+-+-+-+-+-+-+")

# 查找以wl开头的无线接口名，例如-wlan0，wlp3s0
infname = cret('ifconfig -a  | egrep "^[wl-wl]+" | sed "s/: .*//" | grep -v "lo"')
# 只取接口名的最后6个字符
infname = infname[:6]
infname = infname.decode("utf-8")

# 从/sys/class/net/wlan0/address目录获取当前MAC地址
cmdgetmac = "cat /sys/class/net/" + infname + "/address"
crrntmac = cret("cat /sys/class/net/" + infname + "/address")
crrntmac = crrntmac.decode("utf-8")
print(
    "您当前的MAC地址 = "
    + crrntmac
    + "\n请选择更改MAC的选项：\n1. 手动输入MAC地址 \n2. 自动生成随机MAC地址"
)
opt = int(input())

if opt == 1:
    print("请输入您的新MAC地址：\n示例：46:d2:f4:0c:2a:50")

    newmac = input()
    print("请稍候，正在更改MAC地址..................")

    # 首先关闭WiFi
    cret("nmcli radio wifi off")

    changemaccmd = "sudo ip link set dev " + infname + " address " + newmac
    # 使用新的MAC地址执行命令
    cret(changemaccmd)
    # 打开WiFi
    cret("nmcli radio wifi on")
    # 从/sys/class/net/wlan0/address目录获取新的MAC地址
    cr = cret("cat /sys/class/net/" + infname + "/address")
    cr = cr.decode("utf-8")

    print("\n现在您的MAC地址已更改为：" + cr)

elif opt == 2:
    genmac = retrandmac(randmac())
    print("请稍候，正在生成新的MAC地址.....................")
    cret("nmcli radio wifi off")
    changemaccmd = "sudo ip link set dev " + infname + " address " + genmac
    cret(changemaccmd)
    cret("nmcli radio wifi on")
    cr = cret("cat /sys/class/net/" + infname + "/address")
    cr = cr.decode("utf-8")
    print("现在您的MAC地址已更改为：" + cr)

else:
    print("您选择了错误的选项")
