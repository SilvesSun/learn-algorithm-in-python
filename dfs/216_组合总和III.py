class Solution(object):
    def combinationSum3(self, k, n):
        # 从n个数中选k个数, 和为n
        nums = list(range(1, 10))
        res = []
        self.backtrack(nums, k, [], res, n)
        return res

    def backtrack(self, nums, k, path, res, n):
        if sum(path) > n:
            return
        if len(path) == k:
            if sum(path) == n:
                res.append(path[:])
            return
        if len(path) > k:
            return
        for i in range(len(nums)):
            path.append(nums[i])
            self.backtrack(nums[i+1:], k, path, res, n)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 7))