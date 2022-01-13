# 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
#
#  如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回
# true ；否则，返回 false 。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3,4,5]
# 输出：true
# 解释：任何 i < j < k 的三元组都满足题意
#
#
#  示例 2：
#
#
# 输入：nums = [5,4,3,2,1]
# 输出：false
# 解释：不存在满足题意的三元组
#
#  示例 3：
#
#
# 输入：nums = [2,1,5,0,4,6]
# 输出：true
# 解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 5 * 10⁵
#  -2³¹ <= nums[i] <= 2³¹ - 1
#
#
#
#
#  进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？
#  Related Topics 贪心 数组 👍 428 👎 0


from typing import List


class Solution:
    def increasingTriplet1(self, nums: List[int]) -> bool:
        """
        时间复杂度为 O(n) ，空间复杂度为 O(n)
        """
        n = len(nums)
        left_min = [0] * n
        right_max = [0] * n
        left_min[0] = nums[0]
        right_max[-1] = nums[-1]
        for i in range(1, n):
            left_min[i] = min(left_min[i-1], nums[i])
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])
        for i in range(1, n-1):
            if left_min[i-1] < nums[i] < right_max[i + 1]:
                return True
        return False

    def increasingTriplet2(self, nums: List[int]) -> bool:
        a = nums[0]
        b = float('inf')
        for n in nums:
            if n > b:
                return True
            if n < a:
                a = n
            elif n > a:
                b = n
        return False