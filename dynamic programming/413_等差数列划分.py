from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) < 3: return 0
        # dp 以nums[i]结尾的等差数列的个数
        dp = [0] * n
        diff = nums[1] - nums[0]
        for i in range(2, n):
            if nums[i] - nums[i - 1] == diff:
                dp[i] = dp[i - 1] + 1
            else:
                diff = nums[i] - nums[i - 1]
        return sum(dp)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 6, 8, 10]
    print(Solution().numberOfArithmeticSlices(nums))
