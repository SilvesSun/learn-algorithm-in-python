# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
#
#
#  示例 1：
#
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
#  示例 2：
#
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
#  限制：
#
#
#  0 <= matrix.length <= 100
#  0 <= matrix[i].length <= 100
#
#
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
#  Related Topics 数组 矩阵 模拟
#  👍 316 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans

        u = 0
        d = len(matrix) - 1
        r = len(matrix[0]) - 1
        l = 0
        while True:
            for i in range(l, r + 1): ans.append(matrix[u][i])
            u += 1
            if u > d: break
            for i in range(u, d + 1): ans.append(matrix[i][r])
            r -= 1
            if r < l: break

            for i in range(r, l - 1, -1): ans.append(matrix[d][i])
            d -= 1
            if d < u: break

            for i in range(d, u - 1, -1):
                ans.append(matrix[i][l])
            l += 1
            if l > r: break
        return ans
# leetcode submit region end(Prohibit modification and deletion)
