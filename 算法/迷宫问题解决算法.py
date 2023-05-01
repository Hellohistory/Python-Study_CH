"""
这段代码是一个简单的迷宫寻路算法。使用了 BFS（广度优先搜索）的方法，从起点开始搜索，并在搜索的过程中判断障碍物和边界等条件，以找到到达终点的最短路径。
其中，taken 列表表示障碍物坐标，visited 列表用来记录是否访问过某个点，queue 则用于存储待访问的点的坐标和步数。最后，输出迷宫和最短路径的步数。
"""
start = [0, 0] # 起点坐标
end = [7, 7] # 终点坐标
taken = [[1, 0], [1, 1], [1, 2], [1, 3]] # 障碍物坐标
queue = [[start[0], start[1], -1]]  # 队列
visited = [] # 记录是否访问过
maze = [] # 迷宫
for i in range(8):
    maze.append([".", ".", ".", ".", ".", ".", ".", "."])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0])
maze[start[0]][start[1]] = "S" # 起点
maze[end[0]][end[1]] = "E" # 终点
for i in taken:
    maze[i[0]][i[1]] = "X" # 障碍物
while len(queue) > 0:
    point = queue.pop(0) # 取出队首元素
    if end[0] == point[0] and end[1] == point[1]: # 到达终点
        print(point[2] + 1) # 输出步数
        break
    current = point[2] + 1 # 当前步数
    if point not in taken and visited[point[0]][point[1]] == 0: # 如果当前点不是障碍物且未被访问过
        visited[point[0]][point[1]] = current # 标记为已访问
        for i in range(point[0], -1, -1): # 向上搜索
            if [i, point[1]] in taken: # 如果遇到障碍物
                break
            if visited[i][point[1]] == 0: # 如果未被访问过
                queue.append([i, point[1], current]) # 加入队列
        for i in range(point[0], 8): # 向下搜索
            if [i, point[1]] in taken:
                break
            if visited[i][point[1]] == 0:
                queue.append([i, point[1], current])
        for i in range(point[1], -1, -1): # 向左搜索
            if [point[0], i] in taken:
                break
            if visited[point[0]][i] == 0:
                queue.append([point[0], i, current])
        for i in range(point[1], 8): # 向右搜索
            if [point[0], i] in taken:
                break
            if visited[point[0]][i] == 0:
                queue.append([point[0], i, current])

for i in maze: # 输出迷宫
    for j in i:
        print(j, end="   ")
    print()