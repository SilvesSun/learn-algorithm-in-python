# coding=utf-8
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        tag: array, dfs
        """

        candidates.sort()
        self.res = []
        self.helper(candidates, target, 0, [])
        print(self.res)
        return self.res

    def helper(self, candidates, target, start, vlist):
        if target == 0:
            return self.res.append(vlist)
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            self.helper(candidates, target-candidates[i], i, vlist+[candidates[i]])


candidates = [2,3,6,7]
target = 7

s = Solution()
s.combinationSum(candidates, target)