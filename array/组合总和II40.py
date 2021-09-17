# coding:utf-8
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
#  candidates 中的每个数字在每个组合中只能使用一次。
#
#  注意：解集不能包含重复的组合。
#
#
#
#  示例 1:
#
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#  示例 2:
#
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
#
#
#
#  提示:
#
#
#  1 <= candidates.length <= 100
#  1 <= candidates[i] <= 50
#  1 <= target <= 30
#
#  Related Topics 数组 回溯
#  👍 687 👎 0

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        self.res = []
        self.helper(candidates, target, 0, [])
        return self.res

    def helper(self, candidates, target, start, vlist):
        if target == 0:
            return self.res.append(vlist)
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            if i > start and candidates[i] == candidates[i - 1]: continue
            self.helper(candidates, target - candidates[i], i+1, vlist + [candidates[i]])



candidates = [2,3,6,7]
target = 5

s = Solution().combinationSum2(candidates, target)
print(s)

