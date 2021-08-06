from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # dp[i] 表示以下标i结尾的数组的连续递增子序列长度为d[i]
        n = len(nums)
        if n == 1: return 1
        res = 1
        dp = [0] * n
        for i in range(n-1):
            if nums[i+1] > nums[i]: dp[i+1] = dp[i] + 1
            if dp[i+1]> res: res = dp[i+1] + 1
        return res