class Solution(object):
    def combine(self, n, k):
        nums = list(range(1, n+1))
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
    print(s.combine(4, 2))
