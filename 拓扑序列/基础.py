"""
拓扑排序是对DAG的顶点进行排序，使得对每一条有向边(u, v)，均有u（在排序记录中）比v先出现。亦可理解为对某点v而言，只有当v的所有源点均出现了，v才能出现。
拓扑排序的实现算法有两种：入度表、DFS，其时间复杂度均为O(V+E)

# 邻接表
对于DAG的拓扑排序，显而易见的办法：

找出图中0入度的顶点；
依次在图中删除这些顶点，删除后再找出0入度的顶点；
然后再删除……再找出……
直至删除所有顶点，即完成拓扑排序
为了保存0入度的顶点，我们采用数据结构栈（亦可用队列）

# DFS

在DFS中，依次打印所遍历到的顶点；而在拓扑排序时，顶点必须比其邻接点先出现。
在DFS实现拓扑排序时，用栈来保存拓扑排序的顶点序列；并且保证在某顶点入栈前，其所有邻接点已入栈
"""