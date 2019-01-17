class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        Given a string, your task is to count how many palindromic substrings in this string.

        The substrings with different start indexes or end indexes are counted as different substrings even they consist
        of same characters.
        """
        s_len = len(s)
        total = 0
        for _sub_len in range(1, s_len+1):
            idx = 0
            while idx < s_len:
                sub_str = s[idx:idx+_sub_len]
                if sub_str == sub_str[::-1] and len(sub_str) == _sub_len:
                    total += 1
                idx += 1
        return total

    def manacher(self, s):
        s_new = "".join(("$#", "#".join(s), "#"))
        p = [0]
        center = 0
        mx = 0
        for i in range(1, len(s_new)):
            if i > mx:
                p.append(0)
            else:
                p.append(min(mx - i, p[2 * center - i]))
            while (i - p[i] - 1) > 0 and (i + p[i] + 1) < len(s_new) and s_new[i - p[i] - 1] == s_new[i + p[i] + 1]:
                p[i] += 1
            if p[i] > mx - center:
                center = i
                mx = i + p[i]
        return p

    def countSubstrings2(self, s):
        return sum((max_len + 1) // 2 for max_len in self.manacher(s))


s = Solution()
s_str = "abcba"
print(s.countSubstrings2(s_str))

