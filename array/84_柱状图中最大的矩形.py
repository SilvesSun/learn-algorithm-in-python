# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#  示例 1:
#
#
#
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#
#
#  示例 2：
#
#
#
#
# 输入： heights = [2,4]
# 输出： 4
#
#
#
#  提示：
#
#
#  1 <= heights.length <=10⁵
#  0 <= heights[i] <= 10⁴
#
#  Related Topics 栈 数组 单调栈 👍 1699 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        c_heights = [0] + heights + [0]
        res = 0
        stack = []
        for i in range(len(c_heights)):
            while stack and heights[stack[-1]] > c_heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


if __name__ == '__main__':
    print(Solution().largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
