# 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
#
#  如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。
#
#
#
#  示例 1：
#
#
# 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# 输出："apple"
#
#
#  示例 2：
#
#
# 输入：s = "abpcplea", dictionary = ["a","b","c"]
# 输出："a"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  1 <= dictionary.length <= 1000
#  1 <= dictionary[i].length <= 1000
#  s 和 dictionary[i] 仅由小写英文字母组成
#
#  Related Topics 数组 双指针 字符串 排序
#  👍 185 👎 0
from typing import List
from itertools import groupby


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ds = list(sorted(dictionary, key=lambda x: (len(x), x), reverse=True))
        longest = ''
        for t in ds:
            if self.isValid(s, t):
                if len(t) > len(longest):
                    longest = t
                elif len(t) == len(longest):
                    if t < longest:
                        longest = t
            if len(t) < len(longest):
                return longest
        return longest

    def isValid(self, str1, str2):
        n1 = len(str1)
        n2 = len(str2)
        i1, i2 = 0, 0
        while i1 < n1 and i2 < n2:
            if str1[i1] != str2[i2]:
                i1 += 1
            else:
                i1 += 1
                i2 += 1
        return i2 == n2


if __name__ == '__main__':
    print(Solution().findLongestWord(s = "abpcplea", dictionary = ["a","b","c"]))
