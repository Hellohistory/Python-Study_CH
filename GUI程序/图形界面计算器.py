from tkinter import *

# 创建主窗口
w = Tk()
w.geometry("500x500")
w.title("计算器ax")
w.configure(bg="#03befc")


# 函数定义（数字按钮）
def calc1():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn1["text"]
    txt1.insert(0, b1)


def calc2():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn2["text"]
    txt1.insert(0, b1)


def calc3():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn3["text"]
    txt1.insert(0, b1)


def calc4():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn4["text"]
    txt1.insert(0, b1)


def calc5():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn5["text"]
    txt1.insert(0, b1)


def calc6():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn6["text"]
    txt1.insert(0, b1)


def calc7():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn7["text"]
    txt1.insert(0, b1)


def calc8():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn8["text"]
    txt1.insert(0, b1)


def calc9():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn9["text"]
    txt1.insert(0, b1)


def calc0():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn0["text"]
    txt1.insert(0, b1)


# 函数定义（运算符按钮）
x = 0


def add():
    global x
    add.b = eval(txt1.get())
    txt1.delete(0, END)
    x = x + 1


def subtract():
    global x
    subtract.b = eval(txt1.get())
    txt1.delete(0, END)
    x = x + 2


def get():
    b = txt1.get()


def equals():
    global x
    if x == 1:
        c = (eval(txt1.get())) + add.b
        cls()
        txt1.insert(0, c)

    elif x == 2:
        c = subtract.b - (eval(txt1.get()))
        cls()
        txt1.insert(0, c)

    elif x == 3:
        c = multiply.b * (eval(txt1.get()))
        cls()
        txt1.insert(0, c)
    elif x == 4:
        c = divide.b / (eval(txt1.get()))
        cls()
        txt1.insert(0, c)


def cls():
    global x
    x = 0
    txt1.delete(0, END)


def multiply():
    global x
    multiply.b = eval(txt1.get())
    txt1.delete(0, END)
    x = x + 3


def divide():
    global x
    divide.b = eval(txt1.get())
    txt1.delete(0, END)
    x = x + 4


# 创建标签
lbl1 = Label(
    w, text="计算器ax", font=("Times New Roman", 35), fg="#232226", bg="#fc9d03"
)

# 创建输入框
txt1 = Entry(w, width=80, font=30)

# 创建数字按钮
btn1 = Button(w, text="1", font=("Unispace", 25), command=calc1, bg="#c3c6d9")
btn2 = Button(w, text="2", font=("Unispace", 25), command=calc2, bg="#c3c6d9")
btn3 = Button(w, text="3", font=("Unispace", 25), command=calc3, bg="#c3c6d9")
btn4 = Button(w, text="4", font=("Unispace", 25), command=calc4, bg="#c3c6d9")
btn5 = Button(w, text="5", font=("Unispace", 25), command=calc5, bg="#c3c6d9")
btn6 = Button(w, text="6", font=("Unispace", 25), command=calc6, bg="#c3c6d9")
btn7 = Button(w, text="7", font=("Unispace", 25), command=calc7, bg="#c3c6d9")
btn8 = Button(w, text="8", font=("Unispace", 25), command=calc8, bg="#c3c6d9")
btn9 = Button(w, text="9", font=("Unispace", 25), command=calc9, bg="#c3c6d9")
btn0 = Button(w, text="0", font=("Unispace", 25), command=calc0, bg="#c3c6d9")

# 创建运算符按钮
btn_addition = Button(w, text="+", font=("Unispace", 26), command=add, bg="#3954ed")
btn_equals = Button(
    w, text="计算", font=("Unispace", 24), command=equals, bg="#e876e6"
)
btn_clear = Button(
    w, text="清除", font=("Unispace", 24), command=cls, bg="#e876e6"
)
btn_subtract = Button(
    w, text="-", font=("Unispace", 26), command=subtract, bg="#3954ed"
)
btn_multiplication = Button(
    w, text="x", font=("Unispace", 26), command=multiply, bg="#3954ed"
)
btn_division = Button(
    w, text="÷", font=("Unispace", 26), command=divide, bg="#3954ed"
)

# 安排界面元素的位置
lbl1.place(x=120, y=0)
txt1.place(x=7, y=50, height=35)
btn1.place(x=50, y=100)
btn2.place(x=120, y=100)
btn3.place(x=190, y=100)
btn4.place(x=50, y=200)
btn5.place(x=120, y=200)
btn6.place(x=190, y=200)
btn7.place(x=50, y=300)
btn8.place(x=120, y=300)
btn9.place(x=190, y=300)
btn0.place(x=120, y=400)
btn_addition.place(x=290, y=100)
btn_equals.place(x=260, y=420)
btn_clear.place(x=290, y=350)
btn_subtract.place(x=360, y=100)
btn_multiplication.place(x=290, y=200)
btn_division.place(x=360, y=200)

# 启动主循环
w.mainloop()
