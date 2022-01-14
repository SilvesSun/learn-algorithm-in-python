# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。
#
#
#
#  示例 1：
#
#
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#
#
#  示例 2：
#
#
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10⁴
#  s 由小写英文字母组成
#  1 <= words.length <= 5000
#  1 <= words[i].length <= 30
#  words[i] 由小写英文字母组成
#
#  Related Topics 哈希表 字符串 滑动窗口 👍 591 👎 0


from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        基础思路, 按照串联words的长度为窗口, 逐位判断是否可以形成需要的子串. 由于不在乎words的顺序, 所以用dict统计单词出现的次数即可
        """
        step = len(words[0])
        n = len(words) * step
        if len(s) < n:
            return []
        i = 0
        j = i + n
        hw = Counter(words)
        ls = len(s)
        ans = []
        while j <= ls:
            sub_words = [s[i: i+step] for i in range(i, j, step)]
            hs = Counter(sub_words)
            if hs == hw:
                ans.append(i)
            i += 1
            j += 1
        return ans


if __name__ == '__main__':
    print(Solution().findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","good"]))
