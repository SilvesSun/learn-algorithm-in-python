"""
给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。

 你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。在每一步移动中，你可以向上、向左或者左上方移
动，可以移动的前提是到达的格子没有障碍。

 一条路径的 「得分」 定义为：路径上所有数字的和。

 请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。

 如果没有任何路径可以到达终点，请返回 [0, 0] 。



 示例 1：


输入：board = ["E23","2X2","12S"]
输出：[7,1]


 示例 2：


输入：board = ["E12","1X1","21S"]
输出：[4,2]


 示例 3：


输入：board = ["E11","XXX","11S"]
输出：[0,0]




 提示：


 2 <= board.length == board[i].length <= 100


 Related Topics 数组 动态规划 矩阵 👍 94 👎 0

"""
from math import inf
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board[0])
        dp = [[-inf for _ in range(n + 1)] for _ in range(n + 1)]
        p = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        board = list(list(x)[::-1] for x in board)[::-1]  # 翻转，从左上角到右下角
        board[0][0] = board[n - 1][n - 1] = '0'
        dp[0][0] = 0
        p[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if board[i - 1][j - 1] == 'X':
                    continue
                maxv = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                dp[i][j] = maxv + int(board[i - 1][j - 1])

                if maxv == dp[i - 1][j]: p[i][j] += p[i - 1][j]
                if maxv == dp[i][j - 1]: p[i][j] += p[i][j - 1]
                if maxv == dp[i - 1][j - 1]: p[i][j] += p[i - 1][j - 1]
        mod = 10 ** 9 + 7
        if dp[n][n] < 0:
            return [0, 0]
        return [dp[n][n], p[n][n] % mod]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().pathsWithMaxScore(["E23", "2X2", "12S"]))
