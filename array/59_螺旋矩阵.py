# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
#
#
#
#  示例 1：
#
#
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：[[1]]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 20
#
#  Related Topics 数组 矩阵 模拟
#  👍 557 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = 0
        bottom = n - 1
        l = 0
        r = n - 1
        ans = [[-1] * n for _ in range(n)]
        cur = 0
        while 1:
            for i in range(l, r + 1):
                cur += 1
                ans[top][i] = cur
            top += 1
            if top > bottom: break
            for i in range(top, bottom + 1):
                cur += 1
                ans[i][r] = cur
            r -= 1
            if r <l: break
            for i in range(r, l - 1, -1):
                cur += 1
                ans[bottom][i] = cur
            bottom -= 1
            if bottom < top: break

            for i in range(bottom, top - 1, -1):
                cur += 1
                ans[i][l] = cur
            l += 1
            if l > r: break
        return ans


if __name__ == '__main__':
    print(Solution().generateMatrix(3))
