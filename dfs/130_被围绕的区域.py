# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
# 。
#
#
#
#
#  示例 1：
#
#
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O",
# "X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#
#
#  示例 2：
#
#
# 输入：board = [["X"]]
# 输出：[["X"]]
#
#
#
#
#  提示：
#
#
#  m == board.length
#  n == board[i].length
#  1 <= m, n <= 200
#  board[i][j] 为 'X' 或 'O'
#
#
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 775 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from pprint import pprint
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        row, col = len(board), len(board[0])
        for i in range(row):
            # first line
            if board[i][0] == "O":
                self.dfs(board, i, 0)
            # last line
            if board[i][col-1] == 'O':
                self.dfs(board, i, col-1)

        for j in range(col):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[row-1][j]:
                self.dfs(board, row-1, j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            # i, j 已超出边界
            return
        if board[i][j] in ['X', '#']:
            return
        board[i][j] = '#'
        self.dfs(board, i - 1, j)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))