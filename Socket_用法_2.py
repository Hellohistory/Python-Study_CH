# 使用Python中的socket模块监听指定的端口，一旦有客户端连接，它会发送当前时间信息给客户端，然后关闭连接。

import socket
import time

# 创建一个socket对象并绑定到指定端口
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((socket.gethostname(), 2905))

# 开始监听
soc.listen(5)

while True:
    # 等待客户端连接
    clientsocket, addr = soc.accept()

    print("来自 %s 的连接已建立" % str(addr))

    # 获取当前时间
    currentTime = time.ctime(time.time()) + "\r\n"

    # 向客户端发送当前时间信息
    clientsocket.send(currentTime.encode("ascii"))

    # 关闭连接
    clientsocket.close()