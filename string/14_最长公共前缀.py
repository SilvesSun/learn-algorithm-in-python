from pprint import pprint
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1: return ""
        if len(strs) == 1: return strs[0]

        # 获取字符串数组中长度最小的值
        strs = sorted(strs, key=lambda x: len(x))
        base = strs[0]
        idx = 0
        eq = True
        while idx < len(base):
            for i in range(1, len(strs)):
                s = strs[i]
                if not s:
                    eq = False
                    break
                if base[idx] != s[idx]:
                    eq = False
                    break
            if not eq:
                break
            idx += 1
        return base[:idx] if idx else ""


if __name__ == '__main__':
    pprint(Solution().longestCommonPrefix(["ab", "a"]))
