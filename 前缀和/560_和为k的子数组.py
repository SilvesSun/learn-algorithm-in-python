# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
#
#
#  示例 2：
#
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2 * 10⁴
#  -1000 <= nums[i] <= 1000
#  -10⁷ <= k <= 10⁷
#
#  Related Topics 数组 哈希表 前缀和 👍 1341 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        简单前缀和解决, 超时
        """
        pre_sum = list(accumulate(nums))
        pre_sum.insert(0, 0)
        n = len(nums)
        cnt = 0
        for left in range(0, n):
            for r in range(left, n):
                if pre_sum[r + 1] - pre_sum[left] == k:
                    cnt += 1
        return cnt

    def subarraySum2(self, nums: List[int], k: int) -> int:
        """
        借助哈希表保存累加和sumsum及出现的次数。若累加和sum-ksum−k在哈希表中存在，则说明存在连续序列使得和为kk。则之前的累加和中，sum-ksum−k出现的次数即为有多少种子序列使得累加和为sum-ksum−k

        """
        d = {0: 1}
        pre_sum = 0
        count = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if (pre_sum - k) in d:
                count += d[pre_sum - k]
            if pre_sum in d:
                d[pre_sum] += 1
            else:
                d[pre_sum] = 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
