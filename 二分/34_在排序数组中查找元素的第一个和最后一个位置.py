class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

            # find the index of the rightmost appearance of `target` (by reverse
            # iteration). it is guaranteed to appear.
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]

    def searchRange2(self, nums, target):
        left = 0
        right = len(nums) - 1
        mid = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                break
            if nums[mid] > target:
                right -= 1
            if nums[mid] < target:
                left += 1
        if mid == -1: return [-1, -1]
        if nums[mid] != target: return [-1, -1]
        l = mid
        r = mid

        while l -1 >= 0:
            if nums[l-1] == target:
                l -= 1
            else:
                break

        while r  <= len(nums)-2:
            if nums[r+1] == target:
                r += 1
            else:
                break
        return [l, r]


s = Solution()
print(s.searchRange2([2, 2], 2))
