class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        nums = list(range(1, n + 1))
        self.backtrack(nums, [], res)
        return len(res)

    def backtrack(self, nums, path, res):
        if path and (not path[-1] % len(path) == 0) and (not len(path) % path[-1] == 0):
            return

        if not nums:
            p = path[:]
            res.append(p)
            return
        for i in range(len(nums)):
            # if i and nums[i] == nums[i - 1]: continue
            path.append(nums[i])
            self.backtrack(nums[:i] + nums[i + 1:], path, res)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    s.countArrangement(2)
