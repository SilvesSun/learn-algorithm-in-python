# 给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，请你判
# 断一个人是否能够参加这里面的全部会议。
#
#
#
#  示例 1：
#
#
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：false
#
#
#  示例 2：
#
#
# 输入：intervals = [[7,10],[2,4]]
# 输出：true
#
#
#
#
#  提示：
#
#
#  0 <= intervals.length <= 10⁴
#  intervals[i].length == 2
#  0 <= starti < endi <= 10⁶
#
#  Related Topics 数组 排序 👍 114 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(0, len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().canAttendMeetings(intervals = [[5,8],[6,8]]))