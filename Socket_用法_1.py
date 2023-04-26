# 使用Python中的socket模块连接到本地计算机的特定端口，并接收从该端口发送的数据。

import socket

# 创建一个socket对象
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 使用socket对象连接到本地计算机的特定端口
soc.connect((socket.gethostname(), 2905))

# 从该端口接收数据
recmsg = soc.recv(1024)

# 关闭socket连接
soc.close()

# 输出接收到的数据
print("从服务器获取的时间是 %s" % recmsg.decode("ascii"))