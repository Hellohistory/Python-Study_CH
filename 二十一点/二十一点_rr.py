import random


class Colour:
    BLACK = "\033[30m"
    RED = "\033[91m"
    GREEN = "\033[32m"
    END = "\033[0m"


suits = (
    Colour.RED + "红桃" + Colour.END,
    Colour.RED + "方块" + Colour.END,
    Colour.BLACK + "黑桃" + Colour.END,
    Colour.BLACK + "梅花" + Colour.END,
)
ranks = (
    "二",
    "三",
    "四",
    "五",
    "六",
    "七",
    "八",
    "九",
    "十",
    "杰克",
    "皇后",
    "国王",
    "A",
)
values = {
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
    "杰克": 10,
    "皇后": 10,
    "国王": 10,
    "A": 11,
}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # 花色
        self.rank = rank  # 点数

    def __str__(self):
        return self.suit + self.rank  # 返回牌的点数和花色


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n " + card.__str__()
        return "Deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # 手牌
        self.value = 0  # 手牌点数
        self.aces = 0  # 记录A的数量

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "A":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100  # 初始筹码
        self.bet = 0  # 下注筹码

    def win_bet(self):
        self.total += self.bet  # 赢了加上下注筹码

    def lose_bet(self):
        self.total -= self.bet  # 输了减去下注筹码


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("请下注："))  # 输入下注筹码
        except ValueError:
            print("下注必须是整数，请重新输入！")
        else:
            if chips.bet > chips.total or chips.bet <= 0:
                print("下注不能超过余额且必须是正数！您当前的余额为：", chips.total)
            else:
                break


# 定义 hit 函数，用于抽取一张牌并加入手牌
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# 定义 hit_or_stand 函数，用于判断是否继续抽牌
def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("是否要继续抽牌？输入 '1' 继续抽牌，输入 '0' 停止抽牌 ")

        if x.lower() == "1":
            hit(deck, hand)

        elif x.lower() == "0":
            print("您选择停止抽牌，庄家将继续抽牌。")
            playing = False

        else:
            print("输入错误，请重新输入。")
            continue
        break


# 定义 show_some 函数，用于展示玩家和庄家的手牌
def show_some(player, dealer):
    print("\n庄家的手牌:")
    print(" { 隐藏的牌 }")
    print("", dealer.cards[1])
    print("\n您的手牌:", *player.cards, sep="\n ")


# 定义 show_all 函数，用于展示玩家和庄家的所有手牌
def show_all(player, dealer):
    print("\n庄家的手牌:", *dealer.cards, sep="\n ")
    print("庄家的点数 =", dealer.value)
    print("\n您的手牌:", *player.cards, sep="\n ")
    print("您的点数 =", player.value)


# 定义 player_busts 函数，用于处理玩家爆牌的情况
def player_busts(player, dealer, chips):
    print("您爆牌了！")
    chips.lose_bet()


# 定义 player_wins 函数，用于处理玩家胜利的情况
def player_wins(player, dealer, chips):
    print("您赢了！")
    chips.win_bet()


# 定义 dealer_busts 函数，用于处理庄家爆牌的情况
def dealer_busts(player, dealer, chips):
    print("庄家爆牌了！")
    chips.win_bet()


# 定义 dealer_wins 函数，用于处理庄家胜利的情况
def dealer_wins(player, dealer, chips):
    print("庄家赢了！")
    chips.lose_bet()


# 定义 push 函数，用于处理平局的情况
def push(player, dealer):
    print("平局！")


# GAMEPLAY
player_chips = Chips()

while True:

    print("\t              **********************************************************")
    print(
        "\t                                   欢迎来到赌场 - 二十一点 !                                                     "
    )
    print("\t              **********************************************************")
    print(Colour.BLACK + "\t                                   ***************")
    print("\t                                   * A           *")
    print("\t                                   *             *")
    print("\t                                   *      *      *")
    print("\t                                   *     ***     *")
    print("\t                                   *    *****    *")
    print("\t                                   *     ***     *")
    print("\t                                   *      *      *")
    print("\t                                   *             *")
    print("\t                                   *             *")
    print("\t                                   ***************" + Colour.END)

    print(
        "\n规则：尽可能接近21点，但如果超过21点，您将输！\n  A计为1或11。"
    )

    deck = Deck()  # 创建一副牌
    deck.shuffle()  # 洗牌

    player_hand = Hand()  # 创建玩家手牌
    player_hand.add_card(deck.deal())  # 玩家摸一张牌
    player_hand.add_card(deck.deal())  # 玩家再摸一张牌

    dealer_hand = Hand()  # 创建庄家手牌
    dealer_hand.add_card(deck.deal())  # 庄家摸一张牌
    dealer_hand.add_card(deck.deal())  # 庄家再摸一张牌

    take_bet(player_chips)  # 玩家下注

    show_some(player_hand, dealer_hand)  # 显示玩家手牌和庄家手牌

    while playing:

        hit_or_stand(deck, player_hand)  # 玩家选择是否继续摸牌
        show_some(player_hand, dealer_hand)  # 显示玩家手牌和庄家手牌

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)  # 玩家爆牌
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)  # 庄家摸牌

        show_all(player_hand, dealer_hand)  # 显示玩家手牌和庄家手牌

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)  # 庄家爆牌

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)  # 庄家胜利

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)  # 玩家胜利

        else:
            push(player_hand, dealer_hand)  # 平局

    print("\n您当前的余额为", player_chips.total)

    if player_chips.total > 0:
        new_game = input("您想再玩一局吗？输入'1'或'0' ")
        if new_game.lower() == "1":
            playing = True
            continue
        else:
            print(
                "感谢您的游玩！\n"
                + Colour.GREEN
                + "\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n \t      恭喜您赢得了 "
                + str(player_chips.total)
                + " 个硬币！\n\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n "
                + Colour.END
            )
            break
    else:
        print(
            "糟糕！您已经下注了所有的筹码，我们很抱歉您不能再玩了。\n感谢您的游玩！再见！"
        )
        break
