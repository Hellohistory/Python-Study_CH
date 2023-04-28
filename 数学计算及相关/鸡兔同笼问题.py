"""
作者：Anurag Kumar（mailto：anuragkumarak95@gmail.com）

模块用于解决一个古老的中国谜题：
在农场的鸡和兔子中，我们数了35个头和94条腿。
我们有多少只兔子和多少只鸡？

"""

# 定义函数，解决问题
def solve(num_heads, num_legs):
    ns = "无解！"
    for i in range(num_heads + 1):
        j = num_heads - i
        if 2 * i + 4 * j == num_legs:
            return i, j
    return ns, ns

# 主函数
if __name__ == "__main__":
    # numheads = input('请输入头的数量:') # 头的数量
    # numlegs = input('请输入腿的数量:') # 腿的数量
    numheads = 35
    numlegs = 94

    # 调用函数，输出结果
    solutions = solve(numheads, numlegs)
    print("兔子有", solutions[0], "只，鸡有", solutions[1], "只。")