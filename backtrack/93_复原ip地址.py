class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) > 12:
            return []
        self.backtrack(s, 0, [], res)
        return res

    def backtrack(self, s, idx, path, res):
        if len(path) == 4:
            if idx == len(s):
                res.append(".".join(path[:]))
                return
        for i in range(idx + 1, min(idx + 4, len(s) + 1)):
            string = s[idx: i]
            if not 0 <= int(string) <= 255:
                continue
            # 当字符串不为'0'且以0开头时, 无效
            if string != '0' and string.lstrip('0') != string:
                continue
            path.append(string)
            self.backtrack(s, i, path, res)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("101023"))
