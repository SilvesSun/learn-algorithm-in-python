# coding:utf-8
__date__ = '2018/5/16 9:33'


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dp = [1 for _ in range(l)]
        for i in range(1, l):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


s = Solution()
nums = [10, 9, 2, 5, 3, 4]
s.lengthOfLIS(nums)
