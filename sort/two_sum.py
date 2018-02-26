class Solution(object):
    def two_sum(self, nums, target):
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            tmp = nums[left] + nums[right]
            if tmp > target:
                right -= 1
            elif tmp < target:
                left += 1
            else:
                return [left+1, right+1]