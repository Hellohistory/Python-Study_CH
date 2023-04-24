from tkinter import *
from platform import system

# 判断系统类型，导入不同的语音库
if system() == "Windows" or "nt":

    import win32com.client as wincl
else:
    print("抱歉，本程序不支持Linux或MacOS系统")
    exit()


def text2Speech():
    text = e.get()
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)


# 窗口配置
tts = Tk()
tts.wm_title("文本转语音")
tts.geometry("225x105")
tts.config(background="#708090")

f = Frame(tts, height=280, width=500, bg="#bebebe")
f.grid(row=0, column=0, padx=10, pady=5)

# 标签
lbl = Label(f, text="请输入要转换的文本：")
lbl.grid(row=1, column=0, padx=10, pady=2)

# 输入框
e = Entry(f, width=30)
e.grid(row=2, column=0, padx=10, pady=2)

# 播放按钮
btn = Button(f, text="播放", command=text2Speech)
btn.grid(row=3, column=0, padx=20, pady=10)

# 运行窗口
tts.mainloop()
