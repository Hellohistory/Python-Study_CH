import turtle

# 创建一个Turtle对象
t = turtle.Turtle()

# 设置窗口标题和背景颜色
turtle.title("我爱你")
screen = turtle.Screen()
screen.bgcolor("white")

# 设置Turtle的颜色和填充
t.color("red")
t.begin_fill()
t.fillcolor("red")

# 绘制爱心形状
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)  # t.left
t.circle(-90, 200)
t.forward(180)

t.end_fill()

# 隐藏Turtle
t.hideturtle()

# 显示绘图
turtle.done()
