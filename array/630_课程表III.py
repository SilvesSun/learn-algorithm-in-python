# 这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDay
# i] 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。
#
#  你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。
#
#  返回你最多可以修读的课程数目。
#
#
#
#  示例 1：
#
#
# 输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# 输出：3
# 解释：
# 这里一共有 4 门课程，但是你最多可以修 3 门：
# 首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
# 第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
# 第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
# 第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。
#
#  示例 2：
#
#
# 输入：courses = [[1,2]]
# 输出：1
#
#
#  示例 3：
#
#
# 输入：courses = [[3,2],[4,3]]
# 输出：0
#
#
#
#
#  提示:
#
#
#  1 <= courses.length <= 104
#  1 <= durationi, lastDayi <= 104
#
#  Related Topics 贪心 数组 堆（优先队列）
#  👍 229 👎 0
import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        对所有课程按照ddl升序排列，那我们就可以通过遍历尝试优先修读最早截止的课程
        每门课修读所需要的时长又是不一样的，所以在肯定有课已经要超过ddl的时候，那我们就会选择修读时间更短的课程优先修读；这样我们修读下一门课的时候就会有更多的时间了


        """
        courses.sort(key=lambda x: x[1])
        q = []
        total = 0
        for ti, di in courses:
            if total + ti <= di:
                total += ti
                heapq.heappush(q, -ti)
            elif q and -q[0] > ti:
                total -= -q[0] - ti
                heapq.heappop(q)
                heapq.heappush(q, -ti)
        return len(q)