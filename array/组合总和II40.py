# coding:utf-8


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []

        return self.res

    def helper(self, candidates, target, start, vlist):
        if target == 0:
            return self.res.append(vlist)
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            self.helper(candidates, target - candidates[i], i, vlist + [candidates[i]])



candidates = [2,3,6,7]
target = 7

s = Solution()

