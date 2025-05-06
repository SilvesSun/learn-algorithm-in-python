# 给你两个数组 nums1 和 nums2 。
#
#  请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。
#
#  数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5] 是 [1,2,3,4
# ,5] 的一个子序列而 [1,5,3] 不是。
#
#
#
#  示例 1：
#
#
# 输入：nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# 输出：18
# 解释：从 nums1 中得到子序列 [2,-2] ，从 nums2 中得到子序列 [3,-6] 。
# 它们的点积为 (2*3 + (-2)*(-6)) = 18 。
#
#  示例 2：
#
#
# 输入：nums1 = [3,-2], nums2 = [2,-6,7]
# 输出：21
# 解释：从 nums1 中得到子序列 [3] ，从 nums2 中得到子序列 [7] 。
# 它们的点积为 (3*7) = 21 。
#
#  示例 3：
#
#
# 输入：nums1 = [-1,-1], nums2 = [1,1]
# 输出：-1
# 解释：从 nums1 中得到子序列 [-1] ，从 nums2 中得到子序列 [1] 。
# 它们的点积为 -1 。
#
#
#
#  提示：
#
#
#  1 <= nums1.length, nums2.length <= 500
#  -1000 <= nums1[i], nums2[i] <= 100
#
#
#
#
#  点积：
#
#
# 定义 a = [a1, a2,…, an] 和 b = [b1, b2,…, bn] 的点积为：
#
#
#
# 这里的 Σ 指示总和符号。
#
#
#  Related Topics 数组 动态规划 👍 118 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] 表示考虑 nums1 前 i 个元素和 nums2 前 j 个元素时，能够得到的最大点积。
        # 选择当前元素, 则最大点积可能为 max(dp[i-1][j-1] + nums1[i] * nums2[j], nums1[i] * nums2[j])
        # 不选 nums[1], 则最大点积为 dp[i-1][j]
        # 不选 nums2[1], 则最大点积为 dp[i][j-1]
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf') for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cur = nums1[i-1] * nums2[j-1]
                dp[i][j] = max(cur, dp[i - 1][j - 1] + cur, dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6]))