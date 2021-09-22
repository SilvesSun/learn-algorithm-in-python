# coding=utf-8
# 给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的
# 唯一组合。
#
#  candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。
#
#  对于给定的输入，保证和为 target 的唯一组合数少于 150 个。
#
#
#
#  示例 1：
#
#
# 输入: candidates = [2,3,6,7], target = 7
# 输出: [[7],[2,2,3]]
#
#
#  示例 2：
#
#
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
#
#  示例 3：
#
#
# 输入: candidates = [2], target = 1
# 输出: []
#
#
#  示例 4：
#
#
# 输入: candidates = [1], target = 1
# 输出: [[1]]
#
#
#  示例 5：
#
#
# 输入: candidates = [1], target = 2
# 输出: [[1,1]]
#
#
#
#
#  提示：
#
#
#  1 <= candidates.length <= 30
#  1 <= candidates[i] <= 200
#  candidate 中的每个元素都是独一无二的。
#  1 <= target <= 500
#
#  Related Topics 数组 回溯
#  👍 1537 👎 0

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
            self.helper(candidates, target - candidates[i], i, vlist + [candidates[i]])

    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        path = []

        def backtrack(candidates, target, path, start, total):
            if total > target: return
            if total == target:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if total + candidates[i] > target: return
                total += candidates[i]
                path.append(candidates[i])
                backtrack(candidates, target, path, i, total)  # start = i 表示可以重复选取
                total -= candidates[i]
                path.pop()

        backtrack(candidates, target, path, 0, 0)
        return res


candidates = [2, 3, 6, 7]
target = 7

s = Solution()
print(s.combinationSum2(candidates, target))
