class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        tips: dfs
        """
        if len(nums) <= 1: return [nums]
        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i + 1:]
            for y in self.permute(n):
                ans.append([num] + y)
        return ans

    def permute2(self, nums):
        from itertools import permutations
        res = []
        for i in permutations(nums):
            res.append(i)
        return res


nums = [1, 2, 3]

s = Solution()
s.permute2(nums)