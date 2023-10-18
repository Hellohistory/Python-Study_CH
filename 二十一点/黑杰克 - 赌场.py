# 黑杰克 - 赌场
import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

random.shuffle(deck)

print(
    "                       **********************************************************                                    "
)
print(
    "                                   欢迎来到赌场 - 黑杰克！                                         "
)
print(
    "                       **********************************************************                                    "
)

d_cards = []  # 初始化庄家的牌
p_cards = []  # 初始化玩家的牌

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
        print("玩家的总数是 ", sum(p_cards))
        print("玩家的牌是 ", p_cards)

if sum(p_cards) > 21:
    print("你爆了！\n  **************庄家赢了！！******************\n")
    exit()

if sum(d_cards) > 21:
    print(
        "庄家爆了！\n   ************** 你赢了！！******************\n"
    )
    exit()

if sum(d_cards) == 21:
    print("***********************庄家赢了！！******************")
    exit()

if sum(d_cards) == 21 and sum(p_cards) == 21:
    print("*****************比赛平局！！*************************")
    exit()


def dealer_choice():
    if sum(d_cards) < 17:
        while sum(d_cards) < 17:
            random.shuffle(deck)
            d_cards.append(deck.pop())

    print("庄家的总数是 " + str(sum(d_cards)) + "，牌是 ", d_cards)

    if sum(p_cards) == sum(d_cards):
        print("***************比赛平局！！****************")
        exit()

    if sum(d_cards) == 21:
        if sum(p_cards) < 21:
            print("***********************庄家赢了！！******************")
        elif sum(p_cards) == 21:
            print("********************平局！！**************************")
        else:
            print("***********************庄家赢了！！******************")

    elif sum(d_cards) < 21:
        if sum(p_cards) < 21 and sum(p_cards) < sum(d_cards):
            print("***********************庄家赢了！！******************")
        if sum(p_cards) == 21:
            print("**********************玩家赢了！！**********************")
        if sum(p_cards) < 21 and sum(p_cards) > sum(d_cards):
            print("**********************玩家赢了！！**********************")

    else:
        if sum(p_cards) < 21:
            print("**********************玩家赢了！！**********************")
        elif sum(p_cards) == 21:
            print("**********************玩家赢了！！**********************")
        else:
            print("***********************庄家赢了！！******************")


while sum(p_cards) < 21:

    k = input("要牌还是不要？\n 按1要牌，按0不要 ")
    if k == 1:
        random.shuffle(deck)
        p_cards.append(deck.pop())
        print("你的总数是 " + str(sum(p_cards)) + "，牌是 ", p_cards)
        if sum(p_cards) > 21:
            print("*************你爆了！*************\n 庄家赢了！！")
        if sum(p_cards) == 21:
            print(
                "*******************你赢了！！*****************************"
            )

    else:
        dealer_choice()
        break
