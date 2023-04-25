"""
源注释:
生成随机句子
通过从以下列表中的每个列表中随机选择一个单词来创建句子的不同部分：
'article'（冠词），'noun'（名词），'verb'（动词），'preposition'（介词）和 'article'（冠词）以及 'noun'（名词）。
生成一个短篇小说，其中包含多个这样的随机句子
                                    -- 随机笔记作者!!
为了便于中文语境学习将其替换为了中文
"""

import random

# 原词汇
# article = ["the", "a", "one", "some", "any"]
# noun = ["boy", "girl", "dog", "town", "car"]
# verb = ["drove", "jumped", "ran", "walked", "skipped"]
# preposition = ["to", "from", "over", "under", "on"]

article = ["这个", "一个", "那个", "某些", "任何"]
noun = ["男孩", "女孩", "狗", "城镇", "汽车"]
verb = ["开车", "跳跃", "奔跑", "走路", "跳绳"]
preposition = ["到", "从", "在", "下面", "上面"]


def random_int():
    return random.randint(0, 4)


def random_sentence():
    """创建随机句子并返回"""
    return (
        "{} {} {} {} {} {}".format(
            article[random_int()],
            noun[random_int()],
            verb[random_int()],
            preposition[random_int()],
            article[random_int()],
            noun[random_int()],
        )
    ).capitalize()


# 输出随机句子
for sentence in list(map(lambda x: random_sentence(), range(0, 20))):
    print(sentence)

print("\n")

story = ".".join(list(map(lambda x: random_sentence(), range(0, 20))))

# 输出随机小说
print("{}".format(story))