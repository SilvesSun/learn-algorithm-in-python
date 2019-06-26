class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if nums[0] >= target:
            return 0
        if nums[n-1] <= target:
            return n

        for i in range(len(nums)):
            if nums[i] >= target:
                return i

    def searchInsert2(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) >> 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left



s = Solution()
print(s.searchInsert([1,3,5,6], 5))


