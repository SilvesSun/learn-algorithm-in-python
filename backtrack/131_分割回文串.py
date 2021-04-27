class Solution(object):
    def partition(self, s):
        res = []
        self.backtrack(s, 0, [], res)
        return res

    def backtrack(self, s, start, path, res):
        if start == len(s):
            res.append(path[:])
            return
        for i in range(start, len(s)):
            new_s = s[start: i + 1]
            if not self.is_valid(new_s):
                continue
            path.append(new_s)
            self.backtrack(s, i + 1, path, res)
            path.pop()

    def is_valid(self, s):
        if not s or len(s) == 1:
            return True
        if s == s[::-1]:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.partition('aab'))
