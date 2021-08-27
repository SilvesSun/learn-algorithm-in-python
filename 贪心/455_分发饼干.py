class Solution:
    def findContentChildren(self, g, s) -> int:
        """
        局部最优就是⼤饼⼲喂给胃⼝⼤的，充分利⽤饼⼲尺⼨喂饱⼀个，全局最优就是喂饱尽可能多的⼩孩。
        可以尝试使⽤贪⼼策略，先将饼⼲数组和⼩孩数组排序。
        然后从后向前遍历⼩孩数组，⽤⼤饼⼲优先满⾜胃⼝⼤的，并统计满⾜⼩孩数量。
        """
        g.sort()
        s.sort()
        n = len(s) - 1
        res = 0
        for i in range(len(g) - 1, -1, -1):
            if n >= 0 and s[n] >= g[i]:
                res += 1
                n -= 1
        return res