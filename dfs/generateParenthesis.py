class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        backtracking dfs
        """
        res = []
        if n:
            self.gen(n, n, '', res)
        return res

    def gen(self, l, r, s, res):
        if l == 0 and r == 0:
            res.append(s)
        if l > 0:
            self.gen(l-1, r, s+'(', res)
        if r > l:
            self.gen(l, r-1, s+')', res)


s = Solution()
print(s.generateParenthesis(3))