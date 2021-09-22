"""
描述
给定一个数组arr，返回arr的最长无重复元素子数组的长度，无重复指的是所有数字都不相同。
子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组

"""
from collections import defaultdict


class Solution:
    def maxLength(self, arr):
        l = []
        res = 0
        for i in arr:
            while i in l:
                l.pop(0)
            l.append(i)
            res = max(res, len(l))
        return res


print(Solution().maxLength([2,2,3,4,8,99,3]))
