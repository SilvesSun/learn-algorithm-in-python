# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
#  在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
#
#
#
#
#  示例 1:
#
#
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#
#  示例 2:
#
#
# 输入: numRows = 1
# 输出: [[1]]
#
#
#
#
#  提示:
#
#
#  1 <= numRows <= 30
#
#  Related Topics 数组 动态规划
#  👍 649 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from pprint import pprint
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[0] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            res[i][0] = 1
            res[i][i] = 1
        if numRows < 3:
            return res
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res

if __name__ == '__main__':
    print(Solution().generate(5))
