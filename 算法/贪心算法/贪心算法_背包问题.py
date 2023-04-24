def fractional_knapsack(items, capacity):
    # 对物品按照性价比排序，性价比高的优先选取
    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0
    for item in items:
        if capacity == 0:
            break
        # 如果当前物品可以全部装入背包，则全部装入
        if item.weight <= capacity:
            total_value += item.value
            capacity -= item.weight
        # 否则将当前物品按照容量比例装入背包
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = int(capacity - (item.weight * fraction))
    return total_value


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


items = [Item(10, 60), Item(20, 100), Item(30, 120)]
capacity = 50

print("最大价值为:", fractional_knapsack(items, capacity))
