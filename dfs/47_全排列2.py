class Solution(object):
    def permuteUnique(self, nums):
        if not nums:
            return
        res = []
        nums.sort()
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path[:])
            return
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]: continue
            path.append(nums[i])
            self.backtrack(nums[:i] + nums[i+1:], path, res)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
