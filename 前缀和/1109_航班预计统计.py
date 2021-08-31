# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
#
#  有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 fi
# rsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
#
#  请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。
#
#
#
#  示例 1：
#
#
# 输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# 输出：[10,55,45,25,25]
# 解释：
# 航班编号        1   2   3   4   5
# 预订记录 1 ：   10  10
# 预订记录 2 ：       20  20
# 预订记录 3 ：       25  25  25  25
# 总座位数：      10  55  45  25  25
# 因此，answer = [10,55,45,25,25]
#
#
#  示例 2：
#
#
# 输入：bookings = [[1,2,10],[2,2,15]], n = 2
# 输出：[10,25]
# 解释：
# 航班编号        1   2
# 预订记录 1 ：   10  10
# 预订记录 2 ：       15
# 总座位数：      10  25
# 因此，answer = [10,25]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 2 * 104
#  1 <= bookings.length <= 2 * 104
#  bookings[i].length == 3
#  1 <= firsti <= lasti <= n
#  1 <= seatsi <= 104
#
#  Related Topics 数组 前缀和
#  👍 194 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from itertools import accumulate
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 超出时间限制
        m = len(bookings)
        arr = [[0] * n for _ in range(m)]
        for i in range(m):
            start, end, v = bookings[i]
            for j in range(start - 1, end):
                arr[i][j] = v
        ans = list(map(sum, zip(*arr)))
        return ans

    def corpFlightBookings1(self, bookings: List[List[int]], n: int) -> List[int]:
        # 差分数组对应的概念是前缀和数组，对于数组 [1,2,2,4][1,2,2,4]，其差分数组为 [1,1,0,2]，差分数组的第 i 个数即为原数组的第 i-1个元素和第 i 个元素的差值，
        # 也就是说我们对差分数组求前缀和即可得到原数组。
        #
        # 差分数组的性质是，当我们希望对原数组的某一个区间 [l,r] 施加一个增量inc 时，差分数组 d对应的改变是：d[l] 增加inc，d[r+1] 减少 inc。
        # 这样对于区间的修改就变为了对于两个位置的修改。并且这种修改是可以叠加的，即当我们多次对原数组的不同区间施加不同的增量，我们只要按规则修改差分数组即可。
        #
        # 在本题中，我们可以遍历给定的预定记录数组，每次 O(1) 地完成对差分数组的修改即可。当我们完成了差分数组的修改，只需要最后求出差分数组的前缀和即可得到目标数组。
        #

        # 差分数组
        dif = [0] * n
        for start, end, v in bookings:
            dif[start - 1] += v
            if end < n:
                dif[end] -= v

        return list(accumulate(dif))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    print(Solution().corpFlightBookings1(bookings, n))
