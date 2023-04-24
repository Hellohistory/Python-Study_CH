from time import *
import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

random.shuffle(deck)

print(f'{"*"*58} \n 欢迎来到赌场 - 二十一点 ! \n{"*"*58}')
sleep(2)
print("终于等到你了")
sleep(2)
print("我是说你的运气")
sleep(2)
print("让我们看看你有多幸运")
sleep(2)
print("加载中---")
sleep(2)

print("还在加载中---")
sleep(2)
print(
    "你还在这里，没走？我给你机会了，没关系，也许你非常相信自己的运气\n那么让我们开始吧"
)
sleep(2)
d_cards = []  # 初始化庄家的牌
p_cards = []  # 初始化玩家的牌
sleep(2)
while len(d_cards) != 2:
    random.shuffle(deck)
    d_cards.append(deck.pop())
    if len(d_cards) == 2:
        print("庄家的牌是 X ", d_cards[1])

# 显示玩家的牌
while len(p_cards) != 2:
    random.shuffle(deck)
    p_cards.append(deck.pop())
    if len(p_cards) == 2:
        print("玩家的总分是 ", sum(p_cards))
        print("玩家的牌是 ", p_cards)

if sum(p_cards) > 21:
    print(f"你炸了！\n  {'*'*14}庄家赢了!!{'*'*14}\n")
    exit()

if sum(d_cards) > 21:
    print(f"庄家炸了！\n   {'*'*14} 你赢了!!{'*'*18}\n")
    exit()

if sum(d_cards) == 21:
    print(f"{'*'*24}庄家赢了!!{'*'*14}")
    exit()

if sum(d_cards) == 21 and sum(p_cards) == 21:
    print(f"{'*'*17}平局!!{'*'*25}")
    exit()


# 显示庄家的选择
def dealer_choice():
    if sum(d_cards) < 17:
        while sum(d_cards) < 17:
            random.shuffle(deck)
            d_cards.append(deck.pop())

    print("庄家的总分是 " + str(sum(d_cards)) + "，牌是 ", d_cards)

    if sum(p_cards) == sum(d_cards):
        print(f"{'*'*15}平局!!{'*'*15}")
        exit()

    if sum(d_cards) == 21:
        if sum(p_cards) < 21:
            print(f"{'*'*23}庄家赢了!!{'*'*18}")
        elif sum(p_cards) == 21:
            print(f"{'*'*20}平局!!{'*'*26}")
        else:
            print(f"{'*'*23}庄家赢了!!{'*'*18}")

    elif sum(d_cards) < 21:
        if sum(p_cards) < 21 and sum(p_cards) < sum(d_cards):
            print(f"{'*'*23}庄家赢了!!{'*'*18}")
        if sum(p_cards) == 21:
            print(f"{'*'*22}玩家赢了!!{'*'*22}")
        if 21 > sum(p_cards) > sum(d_cards):
            print(f"{'*'*22}玩家赢了!!{'*'*22}")

    else:
        if sum(p_cards) < 21:
            print(f"{'*'*22}玩家赢了!!{'*'*22}")
        elif sum(p_cards) == 21:
            print(f"{'*'*22}玩家赢了!!{'*'*22}")
        else:
            print(f"{'*'*23}庄家赢了!!{'*'*18}")


while sum(p_cards) < 21:

    # 继续游戏！
    k = input("要继续吗？按1要牌，按0停牌 ")
    if k == 1:
        random.shuffle(deck)
        p_cards.append(deck.pop())
        print("你的总分是 " + str(sum(p_cards)) + "，牌是 ", p_cards)
        if sum(p_cards) > 21:
            print(f'{"*"*13}你爆了！{"*"*13}\n 庄家赢了!!')
        if sum(p_cards) == 21:
            print(f'{"*"*19}你赢了!!{"*"*29}')

    else:
        dealer_choice()
        break
