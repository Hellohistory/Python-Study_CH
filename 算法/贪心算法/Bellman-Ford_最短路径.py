"""
Bellman-Ford算法是一种用于求解图中单源最短路径问题的算法。该算法可以处理负权边，且可以检测负权回路。
Bellman-Ford算法的时间复杂度为O(VE)，其中V是节点数，E是边数。

Bellman-Ford算法基于动态规划思想，其核心思想是：假设从起点s到节点v的最短路径所经过的边数不超过k条，
则从s到v的最短路径可以表示为s到一个中间节点u的最短路径，加上u到v的一条边。其中，k为当前的轮数，
起点到中间节点u的最短路径经过的边数不超过k-1条。

具体实现时，可以通过对所有的边进行k轮松弛操作，来逐步更新每个节点到起点的最短距离。
每轮松弛操作会对每条边进行检查，如果发现可以通过该边使得某个节点的最短路径得到改善，则更新该节点的最短路径。
如果在第V轮松弛操作后，仍然存在某个节点的最短路径可以被改善，则说明图中存在负权回路。
"""


# 边的数据结构，包括起点、终点和边的权值
class Edge:
    def __init__(self, src, dst, weight):
        self.src = src  # 边的起点
        self.dst = dst  # 边的终点
        self.weight = weight  # 边的权重


# 图的数据结构，包括节点数目和边的集合
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices  # 节点数目
        self.edges = []  # 边的集合

    # 添加一条边
    def add_edge(self, src, dst, weight):
        self.edges.append(Edge(src, dst, weight))  # 添加一条边


# Bellman-Ford算法，求解起点到所有点的最短路径
def bellman_ford(graph, start):
    # 初始化距离数组
    dist = [float('inf')] * graph.num_vertices  # 初始化距离数组
    dist[start] = 0  # 起点到自身的距离为0

    # 进行|V|-1轮松弛操作
    for i in range(graph.num_vertices - 1):
        for edge in graph.edges:
            # 对每一条边进行松弛操作
            if dist[edge.src] + edge.weight < dist[edge.dst]:
                dist[edge.dst] = dist[edge.src] + edge.weight  # 更新距离数组

    # 检查是否存在负权回路
    for edge in graph.edges:
        if dist[edge.src] + edge.weight < dist[edge.dst]:
            raise Exception("图中存在负权回路")  # 存在负权回路

    return dist  # 返回距离数组


# 初始化图
graph = Graph(6)
graph.add_edge(0, 1, 7)
graph.add_edge(0, 2, 9)
graph.add_edge(0, 5, 14)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 11)
graph.add_edge(2, 5, 2)
graph.add_edge(3, 4, 6)
graph.add_edge(4, 5, 9)

# 计算最短路径
start = 0  # 起点
try:
    dist = bellman_ford(graph, start)  # 计算最短路径
    print(dist)  # 输出距离数组
except Exception as e:
    print(e)  # 输出异常信息
