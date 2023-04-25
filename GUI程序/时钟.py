import tkinter

# 从time模块中导入strftime函数，用于获取系统时间
from time import strftime

# ------------------主要代码-----------------------
# 初始化主要的UI对象
top = tkinter.Tk()
# 设置应用程序的标题
top.title("时钟")
# 限制应用程序不可调整大小
top.resizable(0, 0)


def time():
    # 获取系统时间
    string = strftime("%H:%M:%S %p")
    # 在UI中显示时间
    clockTime.config(text=string)
    # 每隔1秒更新时间
    clockTime.after(1000, time)


# 创建用于显示时间的标签
clockTime = tkinter.Label(
    top, font=("calibri", 40, "bold"), background="black", foreground="white"
)
# 将标签放置在UI中心
clockTime.pack(anchor="center")
# 开始更新时间
time()


# 启动主循环
top.mainloop()
