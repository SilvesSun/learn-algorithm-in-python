class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        res[0] = 1
        left = 1
        right = 1

        for i in range(1, len(nums)):
            left = left * nums[i - 1]
            res[i] = left

        for i in range(len(nums) - 2, -1, -1):
            right = right * nums[i + 1]
            res[i] = right * res[i]
        return res


nums = [4, 3, 2, 1, 2]

s = Solution()
s.productExceptSelf(nums)
