# 我们定义 arr 是 山形数组 当且仅当它满足：
#
#
#  arr.length >= 3
#  存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且：
#
#  arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#  arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#
#
#  给你整数数组 nums ，请你返回将 nums 变成 山形状数组 的 最少 删除次数。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,3,1]
# 输出：0
# 解释：数组本身就是山形数组，所以我们不需要删除任何元素。
#
#
#  示例 2：
#
#
# 输入：nums = [2,1,1,5,6,2,3,1]
# 输出：3
# 解释：一种方法是将下标为 0，1 和 5 的元素删除，剩余元素为 [1,5,6,3,1] ，是山形数组。
#
#
#
#
#  提示：
#
#
#  3 <= nums.length <= 1000
#  1 <= nums[i] <= 10⁹
#  题目保证 nums 删除一些元素后一定能得到山形数组。
#
#
#  Related Topics 贪心 数组 二分查找 动态规划 👍 144 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # left[i] 表示以 nums[i] 结尾的 lis
        # right[i] 表示以 nums[i] 开头的最长递减字符串
        # 对每个 i，如果 left[i] > 1 且 right[i] > 1，说明 i 可以作为山峰。
        # 计算山形子序列长度为 left[i] + right[i] - 1
        # 取所有 i 的最大山形子序列长度 maxLen，最少删除数为 len(nums) - maxLen
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] > nums[i]:
                    left[i] = max(left[i], left[j] + 1)

        # lds
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[j] < nums[i]:
                    right[i] = max(right[i], right[j] + 1)

        max_len = 0
        for i in range(1, n):
            if left[i] > 1 and right[i] > 1:
                max_len = max(max_len, left[i] + right[i] - 1)
        return n - max_len

# leetcode submit region end(Prohibit modification and deletion)
