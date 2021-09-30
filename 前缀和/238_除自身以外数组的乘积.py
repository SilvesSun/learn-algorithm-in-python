# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之
# 外其余各元素的乘积。
#
#
#
#  示例:
#
#  输入: [1,2,3,4]
# 输出: [24,12,8,6]
#
#
#
#  提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
#
#  说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
#  进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
#  Related Topics 数组 前缀和
#  👍 924 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 用两个数组, left right 分别表示 nums[i] 左边的乘积和右边的乘积
        n = len(nums)
        left = [1] * n
        right = [1] * n
        ans = [1] * n
        for i in range(1, n):
            left[i] = nums[i-1] * left[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i+1]
        for i in range(n):
            ans[i] = left[i] * right[i]
        return ans


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
