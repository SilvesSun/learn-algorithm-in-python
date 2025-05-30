# 给你一个整数数组 nums 。nums 的每个元素是 1，2 或 3。在每次操作中，你可以删除 nums 中的一个元素。返回使 nums 成为 非递减 顺序
# 所需操作数的 最小值。
#
#
#
#  示例 1：
#
#
# 输入：nums = [2,1,3,2,1]
# 输出：3
# 解释：
# 其中一个最优方案是删除 nums[0]，nums[2] 和 nums[3]。
#
#
#  示例 2：
#
#
# 输入：nums = [1,3,2,1,3,3]
# 输出：2
# 解释：
# 其中一个最优方案是删除 nums[1] 和 nums[2]。
#
#
#  示例 3：
#
#
# 输入：nums = [2,2,2,2,3,3]
# 输出：0
# 解释：
# nums 已是非递减顺序的。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 100
#  1 <= nums[i] <= 3
#
#
#  进阶：你可以使用 O(n) 时间复杂度以内的算法解决吗？
#
#  Related Topics 数组 二分查找 动态规划 👍 32 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  要获取最小的操作数, 也就是最后留下的最长子序列最长. 参考lis的操作过程
        # 定义 dp[i] 表示以第 i 个元素结尾的最长递增子序列的长度。
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] >= nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return n - max(dp)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [2, 2, 2, 2, 3, 3]
    print(Solution().minimumOperations(nums))