# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
#
#
#
#  示例 1：
#
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
#  示例 2：
#
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
#
#  提示：
#
#
#  1 <= intervals.length <= 104
#  intervals[i].length == 2
#  0 <= starti <= endi <= 104
#
#  Related Topics 数组 排序
#  👍 1075 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        start = 1
        while start < len(intervals):
            t = intervals[start]
            if t[0] <= res[-1][1]:  # 说明存在重叠
                res[-1] = [min(t[0], res[-1][0]), max(t[1], res[-1][1])]
            else:
                res.append(t)
            start += 1

        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]])
