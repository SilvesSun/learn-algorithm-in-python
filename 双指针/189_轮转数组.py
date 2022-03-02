# 给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
#
#
#
#  示例 1:
#
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
#
#
#  示例 2:
#
#
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  -2³¹ <= nums[i] <= 2³¹ - 1
#  0 <= k <= 10⁵
#
#
#
#
#  进阶：
#
#
#  尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
#  你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
#
#
#
#
#
#
#
#  Related Topics 数组 数学 双指针 👍 1360 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        tmp = nums[-k:] + nums[:-k]
        for i in range(n):
            nums[i] = tmp[i]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        当我们将数组的元素向右移动 k 次后，尾部 k mod n个元素会移动至数组头部，其余元素向后移动 k mod n 个位置
        我们可以先将所有元素翻转，这样尾部的 k mod n 个元素就被移至数组头部，然后我们再翻转 [0, k mod n-1] 区间的元素
        和 [k mod n, n-1] 区间的元素即能得到最后的答案。
        时间复杂度 O(n), 空间复杂度 O(1)
        """
        n = len(nums)
        k = k % n

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)


if __name__ == '__main__':
    print(Solution().rotate2(nums = [1, 2, 3, 4, 5, 6, 7], k = 3))
# leetcode submit region end(Prohibit modification and deletion)
