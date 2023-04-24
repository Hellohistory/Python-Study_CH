"""
Kruskal算法是一种贪心算法，用于求解最小生成树问题，它的时间复杂度为O(E log E)，其中E表示边的数量。
最小生成树问题是指在一个加权无向连通图中，找出一棵生成树，使得所有边的权值之和最小。

Kruskal算法的基本思想是从小到大遍历图中的边，并且只选择不会导致环形成的边。
具体来说，它首先将图中的所有边按照权值从小到大排序，然后依次遍历每条边，如果当前边的两个端点不在同一个连通块中，就将它们合并，
直到生成的图形成一个连通块为止。这样，最终得到的图就是原图的一棵最小生成树。

为了实现Kruskal算法，我们可以使用并查集来维护节点之间的连通关系。
具体来说，我们可以将每个节点看成一个集合，将它们初始化为互不相交的集合，然后按照顺序处理每个边。
对于每个边，我们判断它所连接的两个节点是否在同一个集合中，如果不在同一个集合中，就将它们合并。
在合并的过程中，我们需要使用并查集的“查找”操作来判断两个节点是否在同一个集合中，并且需要使用并查集的“合并”操作来将它们合并成一个集合。

由于Kruskal算法的时间复杂度与边的数量有关，因此它适用于边比较少的稀疏图。
"""

def prim(adjacency_matrix):
    n = len(adjacency_matrix)
    visited = [False] * n
    distances = [float('inf')] * n
    parent = [None] * n

    distances[0] = 0

    # 选择n次，每次选择一个最小的点
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or distances[i] < distances[u]):
                u = i
        visited[u] = True

        # 更新与u相邻的点的距离
        for v in range(n):
            if not visited[v] and adjacency_matrix[u][v] < distances[v]:
                distances[v] = adjacency_matrix[u][v]
                parent[v] = u

    # 检查图是否连通
    if None in parent[1:]:
        raise ValueError("图不连通.")

    edges = []
    for i in range(1, n):
        edges.append((parent[i], i, adjacency_matrix[parent[i]][i]))

    return edges


if __name__ == "__main__":
    # 将边列表转换为邻接矩阵
    n = 6
    edges = [(1, 2, 3), (1, 3, 1), (2, 3, 1), (2, 4, 5), (2, 5, 4), (3, 5, 6), (3, 6, 4), (4, 5, 2), (5, 6, 6)]
    adjacency_matrix = [[float('inf')] * n for _ in range(n)]
    for u, v, weight in edges:
        adjacency_matrix[u-1][v-1] = weight
        adjacency_matrix[v-1][u-1] = weight

    # 运行Prim算法查找最小生成树
    try:
        minimum_spanning_tree = prim(adjacency_matrix)
        print(minimum_spanning_tree)
    except ValueError as e:
        print(e)

