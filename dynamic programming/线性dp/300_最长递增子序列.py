# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
#  子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序
# 列。
#
#
#  示例 1：
#
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#
#
#  示例 2：
#
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#
#
#  示例 3：
#
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2500
#  -10⁴ <= nums[i] <= 10⁴
#
#
#
#
#  进阶：
#
#
#  你可以设计时间复杂度为 O(n²) 的解决方案吗？
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗?
#
#  Related Topics 数组 二分查找 动态规划 👍 2144 👎 0


from typing import List


class Solution:
    def lengthOfLIS_Dynamic(self, nums: List[int]) -> int:
        # 经典动态规划解法（时间复杂度 O(n²)）
        # 定义 dp[i] 表示以第 i 个元素结尾的最长递增子序列的长度。
        # 初始时，所有 dp[i] = 1，因为每个元素自身都可作为长度为1的递增子序列。
        #
        # 状态转移：
        # 对于每个 i，遍历 j 从 0 到 i-1：
        # 如果 nums[i] > nums[j]，则 dp[i] = max(dp[i], dp[j] + 1)。
        #
        # 最终答案是 dp 数组中的最大值。

        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            # 对于以当前nums[i]结尾的子序列, 查看在(0, i)是否存在比当前元素小的数字
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        # 新建数组, 用于保存最长上升子序列, 在数组中尽量存较小的元素, 维持单调递增
        tails = [0] * len(nums)
        res = 0
        for num in nums:
            i, j = 0, res
            while i < j:
                mid = (i + j) > 1
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = num
            if j == res: res += 1
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLIS_Dynamic([10, 9, 2, 5, 3, 7, 101, 18]))
