import heapq


# Dijkstra算法
# 基本过程
# 1. 初始化：将起点加入到优先队列中，并标记为已访问。
# 2. 循环：每次从优先队列中取出一个元素，检查它是否是目标节点。如果是，则结束搜索，否则继续执行以下步骤：
#     a. 对于该节点的每个相邻节点，计算到达它的总成本（即当前节点的成本加上边的权重）。
#     b. 如果这个新成本比之前记录的更低，就更新记录，并把这个新节点加入到优先队列中。
# 3. 当优先队列为空时，说明没有找到目标节点，返回无穷大值。
def dijkstra(graph, start, end):
    # graph: dict，邻接表形式，格式 {节点: [(邻居, 权重), ...], ...}
    # start: 起点
    # end: 终点
    # 使用优先队列， 存储 (当前路径距离, 当前节点, 路径列表)
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        distance, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)

        # 如果当前节点是终点，则返回距离和路径
        if node == end:
            return distance, path

        # 遍历当前节点的邻居，并将它们加入优先队列
        for neighbor, weight in graph[node]:
            heapq.heappush(queue, (distance + weight, neighbor, path + [neighbor]))

    return float("inf"), []


# 使用一个额外的数据结构维护每个节点在队列中的最短距离，避免重复入队导致效率低下
def dijkstra2(graph, start, end):
    # graph: dict，邻接表形式，格式 {节点: [(邻居, 权重), ...], ...}
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {}  # 用于记录路径
    queue = [(0, start)]

    while queue:
        current_dist, node = heapq.heappop(queue)
        if current_dist > dist[node]:
            continue
        if node == end:
            break

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(queue, (new_dist, neighbor))

    # 路径回溯构建
    if dist[end] == float('inf'):
        return float('inf'), []

    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = prev[cur]
    path.append(start)
    path.reverse()

    return dist[end], path


if __name__ == '__main__':
    graph_example = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }

    distance, path = dijkstra2(graph_example, 'A', 'D')
    print(f"最短路径长度: {distance}")
    print(f"最短路径: {path}")
