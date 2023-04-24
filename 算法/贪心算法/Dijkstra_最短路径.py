import heapq

"""
贪心算法在最短路径上的运用是Dijkstra算法。
Dijkstra算法用于解决从一个起点到其他所有节点的最短路径问题。
算法维护一个集合S，表示已经找到最短路径的节点集合，以及一个集合Q，表示还未找到最短路径的节点集合。
算法从起点开始，每次选择Q中离起点最近的节点，将该节点加入S集合，并更新Q中节点的距离。
这个距离是指从起点到该节点的距离加上该节点到目标节点的距离，也就是所谓的“松弛”操作。重复执行这个过程，直到Q集合为空。
这个算法的贪心策略在于每次选择离起点最近的节点，这样每次找到的路径都是当前最优的。
虽然这个算法并不一定能够找到全局最优解，但在实际应用中表现良好，被广泛应用于路由算法、图像处理和机器学习等领域。
"""

def dijkstra(graph, start, end):
    """
    Dijkstra算法求解最短路径
    :param graph: 加权有向图
    :param start: 起点
    :param end: 终点
    :return: 最短路径的长度以及路径上的节点
    """
    # 初始化起点到各个节点的距离为无穷大
    distance = {node: float('inf') for node in graph}
    # 起点到起点的距离为0
    distance[start] = 0
    # 用于记录节点的父节点，从而得到最短路径
    parent = {node: None for node in graph}

    # 使用堆优化，每次选取距离最短的节点进行扩展
    heap = [(0, start)]
    while heap:
        (dist, current_node) = heapq.heappop(heap)

        # 如果当前节点已经被访问过，则跳过
        if distance[current_node] < dist:
            continue

        # 扩展当前节点
        for neighbor, weight in graph[current_node].items():
            new_distance = dist + weight
            # 如果当前路径更短，则更新distance和parent
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current_node
                heapq.heappush(heap, (new_distance, neighbor))

        # 如果当前节点是终点，表示已经找到了最短路径，可以退出循环
        if current_node == end:
            break

    # 从终点向前遍历，得到最短路径上的节点
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    # 返回最短路径的长度和路径上的节点
    return distance[end], path


if __name__ == '__main__':
    # 定义有向加权图
    graph = {
        'A': {'B': 6, 'D': 1},
        'B': {'C': 5},
        'C': {'F': 2},
        'D': {'B': 2, 'E': 1},
        'E': {'C': 5, 'F': 4},
        'F': {}
    }

    # 求解最短路径
    start_node = 'A'
    end_node = 'F'
    distance, path = dijkstra(graph, start_node, end_node)

    # 输出结果
    print(f'从节点{start_node}到节点{end_node}的最短路径为{path}，长度为{distance}')