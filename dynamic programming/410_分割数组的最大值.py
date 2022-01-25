# 给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。
#
#  设计一个算法使得这 m 个子数组各自和的最大值最小。
#
#
#
#  示例 1：
#
#
# 输入：nums = [7,2,5,10,8], m = 2
# 输出：18
# 解释：
# 一共有四种方法将 nums 分割为 2 个子数组。
# 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
#
#  示例 2：
#
#
# 输入：nums = [1,2,3,4,5], m = 2
# 输出：9
#
#
#  示例 3：
#
#
# 输入：nums = [1,4,4], m = 3
# 输出：4
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 1000
#  0 <= nums[i] <= 10⁶
#  1 <= m <= min(50, nums.length)
#
#  Related Topics 贪心 数组 二分查找 动态规划 👍 607 👎 0

from typing import List
from itertools import accumulate


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # time limit 时间复杂度：O(n^2×m)
        # dp[i][j] 表示将数组的前i个数分为j段能得到的最大连续数组和的最小值
        n = len(nums)
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        pre_sum = list(accumulate(nums))
        # 分割数为 1 ，即不分割的情况，所有的前缀和就是依次的状态值
        for i in range(0, n):
            dp[i][1] = pre_sum[i]

        for k in range(2, m + 1):
            for i in range(k - 1, n):
                for j in range(k - 2, i):
                    dp[i][k] = min(dp[i][k], max(dp[j][k - 1], pre_sum[i] - pre_sum[j]))

        return dp[n - 1][m]

    def bin_split_array(self, nums: List[int], m: int):
        def check(x):
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().bin_split_array(nums=[7, 2, 5, 10, 8], m=2))
# leetcode submit region end(Prohibit modification and deletion)
