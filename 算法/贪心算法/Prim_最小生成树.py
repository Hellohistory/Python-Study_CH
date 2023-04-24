def prim(adjacency_matrix):
    n = len(adjacency_matrix)
    visited = [False] * n      # 记录节点是否已经被访问
    distances = [float('inf')] * n   # 记录节点到生成树的最小距离
    parent = [None] * n       # 记录节点在最小生成树中的父节点

    # 任选一个节点作为起点
    distances[0] = 0

    for _ in range(n):
        # 找到距离最小的未访问节点
        u = min((distances[i], i) for i in range(n) if not visited[i])[1]
        visited[u] = True

        # 更新与 u 相邻的节点的距离和父节点
        for v in range(n):
            if not visited[v] and adjacency_matrix[u][v] < distances[v]:
                distances[v] = adjacency_matrix[u][v]
                parent[v] = u

    # 将结果保存为边的列表
    edges = []
    for i in range(1, n):
        edges.append((parent[i], i, adjacency_matrix[parent[i]][i]))

    return edges


# 将边列表转化为邻接矩阵
n = 8
edges = [(1, 4, 2), (5, 3, 2), (1, 2, 6), (4, 5, 6), (4, 3, 7), (2, 4, 8), (4, 1, 9), (3, 5, 9)]
adjacency_matrix = [[float('inf')] * n for _ in range(n)]
for u, v, weight in edges:
    adjacency_matrix[u-1][v-1] = weight
    adjacency_matrix[v-1][u-1] = weight

# 使用 Prim 算法求解最小生成树
minimum_spanning_tree = prim(adjacency_matrix)

# 输出最小生成树的边列表
print(minimum_spanning_tree)
