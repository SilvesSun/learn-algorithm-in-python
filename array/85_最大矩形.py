# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#
#
#  示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#
#
#  示例 2：
#
#
# 输入：matrix = []
# 输出：0
#
#
#  示例 3：
#
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
#  示例 4：
#
#
# 输入：matrix = [["1"]]
# 输出：1
#
#
#  示例 5：
#
#
# 输入：matrix = [["0","0"]]
# 输出：0
#
#
#
#
#  提示：
#
#
#  rows == matrix.length
#  cols == matrix[0].length
#  1 <= row, cols <= 200
#  matrix[i][j] 为 '0' 或 '1'
#
#  Related Topics 栈 数组 动态规划 矩阵 单调栈 👍 1148 👎 0
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        将每一层看成柱状图, 转换为84求柱状图最大的矩形
        """
        m = len(matrix)
        n = len(matrix[0])
        heights = [0] * (n + 2)
        max_area = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == '1':
                    heights[col + 1] += 1
                else:
                    heights[col + 1] = 0

            max_area = max(max_area, self.find_max(heights))

    def find_max(self, heights: List[int]) -> int:
        res = 0
        stack = []
        n = len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                t = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[t])
            stack.append(i)
        return res