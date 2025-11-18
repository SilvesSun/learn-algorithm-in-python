class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for i in range(1, len(nums)+1):
            t = self.combine(nums, i)
            res.extend(t)
        return res

    def combine(self, nums, k):
        res = []
        self.backtrack(nums, k, [], res)
        return res

    def backtrack(self, nums, k, path, res):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(len(nums)):
            path.append(nums[i])
            self.backtrack(nums[i + 1:], k, path, res)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2]))