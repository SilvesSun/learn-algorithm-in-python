#
#
#  有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连
# 。
#
#
#
#  省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
#
#  给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而
# isConnected[i][j] = 0 表示二者不直接相连。
#
#  返回矩阵中 省份 的数量。
#
#
#
#  示例 1：
#
#
# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
#
#
#  示例 2：
#
#
# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
#
#
#
#
#  提示：
#
#
#  1 <= n <= 200
#  n == isConnected.length
#  n == isConnected[i].length
#  isConnected[i][j] 为 1 或 0
#  isConnected[i][i] == 1
#  isConnected[i][j] == isConnected[j][i]
#
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 1232 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findCircleNum_dfs(self, isConnected: List[List[int]]) -> int:
        # 深度优先搜索, 从每个节点开始遍历， 如果节点没有被访问过，则省份数量加1, 同时将该节点加入到访问过的节点集中， 最终的结果为省份数量

        n = len(isConnected)
        visited = set()

        def dfs(i: int):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))