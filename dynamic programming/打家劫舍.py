# coding=utf-8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])

        last_max = nums[0]  # 上次最大收益

        cur_max = max(nums[0], nums[1])
        for i in range(2, length):
            last_max, cur_max = cur_max, max(last_max+nums[i], cur_max)

        return cur_max