import turtle

# 定义颜色列表
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

# 设置海龟画笔
t = turtle.Pen()

# 改变海龟画笔的速度
t.speed(10)

# 改变背景颜色
turtle.bgcolor("black")

# 绘制螺旋形图案
for x in range(200):
    t.pencolor(colors[x % 6])  # setting color
    # 设置画笔颜色，取余数使得颜色可以循环
    t.width(x / 100 + 1)  # setting width
    # 设置画笔宽度，每次递增
    t.forward(x)  # moving forward
    # 向前移动，移动距离递增
    t.left(59)  # moving left
    # 左转 59 度，改变海龟画笔的角度，绘制出螺旋形

turtle.done()
