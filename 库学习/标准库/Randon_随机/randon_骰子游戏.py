# 脚本名称：dice.py
# 作者：Craig Richards
# 创建时间：2017年2月5日
# 上次修改时间：
# 版本：1.0

# 修改：

# 描述：这将随机选择两个数字，就像掷骰子一样，如果您愿意，可以更改骰子的面数

import random


class Die(object):
    # 骰子有一个特性，即在建立时有多少面，例如6。
    def __init__(self):
        self.sides = 6

    """因为骰子至少包含4个面。
    因此，当您需要更改实例属性时，请使用此方法进行判断。
    """

    def set_sides(self, sides_change):
        if sides_change >= 4:
            if sides_change != 6:
                print("将面数从6更改为", sides_change, "！")
            else:
                # 添加else子句以打印消息，指示将面设置为6
                print("面设置为6")
            self.sides = sides_change
        else:
            print("错误的面数！面设置为6")

    def roll(self):
        return random.randint(1, self.sides)


d = Die()
d1 = Die()
d.set_sides(4)
d1.set_sides(4)
print(d.roll(), d1.roll())