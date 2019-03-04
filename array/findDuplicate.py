class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        我们在区间[1, n]中搜索，首先求出中点mid，然后遍历整个数组，统计所有小于等于mid的数的个数，如果个数小于等于mid，
        则说明重复值在[mid+1, n]之间，反之，重复值应在[1, mid-1]之间
        """
        n = len(nums)
        left = 0
        right = n
        while left < right:
            mid = left + int((right - left) / 2)
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return right


s = Solution()
nums = [1, 3, 4, 2, 2]

print(s.findDuplicate(nums))
