# 给你一个下标从 0 开始的整数数组 nums ，你必须将数组划分为一个或多个 连续 子数组。
#
#  如果获得的这些子数组中每个都能满足下述条件 之一 ，则可以称其为数组的一种 有效 划分：
#
#
#  子数组 恰 由 2 个相等元素组成，例如，子数组 [2,2] 。
#  子数组 恰 由 3 个相等元素组成，例如，子数组 [4,4,4] 。
#  子数组 恰 由 3 个连续递增元素组成，并且相邻元素之间的差值为 1 。例如，子数组 [3,4,5] ，但是子数组 [1,3,5] 不符合要求。
#
#
#  如果数组 至少 存在一种有效划分，返回 true ，否则，返回 false 。
#
#
#
#  示例 1：
#
#
# 输入：nums = [4,4,4,5,6]
# 输出：true
# 解释：数组可以划分成子数组 [4,4] 和 [4,5,6] 。
# 这是一种有效划分，所以返回 true 。
#
#
#  示例 2：
#
#
# 输入：nums = [1,1,1,2]
# 输出：false
# 解释：该数组不存在有效划分。
#
#
#
#
#  提示：
#
#
#  2 <= nums.length <= 10⁵
#  1 <= nums[i] <= 10⁶
#
#
#  Related Topics 数组 动态规划 👍 114 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # 参考爬楼梯的思路, 假设当前位置为i, 到达当前位置可以分为走两步或者三步
        # 两步必须 nums[i] == nums[i-1] && dp[i-2] = true
        # 三步分为 nums[i] == nums[i-1] == nums[i-2] && dp[i-3] = true or nums[i] == nums[i-1] + 1 == nums[i-2] + 2 && dp[i-3] = true
        n = len(nums)
        dp = [False] * (n)

        if n == 1:
            return False
        if n == 2:
            return nums[0] == nums[1]
        # 初始化
        dp[1] = nums[0] == nums[1]
        dp[2] = (nums[0] == nums[1] and nums[1] == nums[2]) or (nums[0] == nums[1] - 1 and nums[1] == nums[2] - 1)

        for i in range(3, n):
            dp[i] = (nums[i] == nums[i - 1] and dp[i - 2]) or (nums[i] == nums[i - 1] + 1 and nums[i - 1] == nums[i - 2] + 1 and dp[i - 3]) or (
                        nums[i] == nums[i - 1] and nums[i - 1] == nums[i - 2] and dp[i - 3])
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    a = Solution()
    print(a.validPartition([1,2,3]))