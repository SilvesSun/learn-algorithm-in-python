# coding=utf-8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        rob_start = [0 for x in range(n)]
        rob_end = [0 for x in range(n)]

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        else:
            rob_start[0] = nums[0]
            rob_start[1] = max(nums[0], nums[1])

            rob_end[1] = nums[1]
            rob_end[2] = max(nums[1], nums[2])

            for i in range(2, n - 1):
                rob_start[i] = max(rob_start[i - 2] + nums[i], rob_start[i - 1])
                rob_end[i + 1] = max(rob_end[i - 1] + nums[i + 1], rob_end[i])
        return max(rob_start[n - 2], rob_end[n - 1])


s = Solution()
print(s.rob([2,1,1,2]))