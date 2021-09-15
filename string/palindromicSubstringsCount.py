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
        for _sub_len in range(1, s_len + 1):
            idx = 0
            while idx < s_len:
                sub_str = s[idx:idx + _sub_len]
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

    def manacher2(self, s):
        s_new = "".join(("^#", "#".join(s), "#$"))

        # 用 C 表示回文串的中心，用 R 表示回文串的右边半径坐标，所以 R = C + P[ C ] 。C 和 R 所对应的回文串是当前循环中 R 最靠右的回文串。
        # 用 i_mirror 表示当前需要求的第 i 个字符关于 C 对应的下标
        # 有三种情况将会造成直接赋值为 P [ i_mirror ] 是不正确的
        # 超出了 R
        # 过了最右的 R ，此时不能利用对称性了，但我们一定可以扩展到 R 的. 我们只需要比较 T [ R+1 ] 和 T [ R+1 ]关于 i 的对称点就行了
        # P [ i_mirror ] 遇到了原字符串的左边界
        # i 等于了 R
        c = 0
        r = 0
        n = len(s_new)
        p = [0] * n  # 从中心扩展的长度数组
        for i in range(1, n-1):
            i_mirror = 2 * c - i
            if r > i:
                p[i] = min(r - i, p[i_mirror])
            else:
                p[i] = 0

            # 碰到之前讲的三种情况时候，需要利用中心扩展法
            while s_new[i + 1 + p[i]] == s_new[i - 1 - p[i]]:
                p[i] += 1

            # 判断是否需要更新 R
            if i + p[i] > r:
                c = i
                r = i + p[i]
        max_length = 0
        idx = 0
        for i in range(1, n-1):
            if p[i] > max_length:
                max_length = p[i]
                idx = i
        start = int((idx - max_length) / 2)
        return s[start:start + max_length]


s = Solution()
s_str = "babad"
print(s.manacher2(s_str))
