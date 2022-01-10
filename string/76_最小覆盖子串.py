# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
#
#
#  注意：
#
#
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
#
#  示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#
#
#  示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
#
#
#  示例 3:
#
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
#
#
#  提示：
#
#
#  1 <= s.length, t.length <= 105
#  s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ Related Topics 哈希表 字符串 滑动窗口
#  👍 1539 👎 0

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        滑动窗口解题
        思路是通过map容器记录需要查找的数组各个字母出现的频数，在遍历s数组同时记录当前频数和符合需要查找的数组元素的个数。
        滑动窗口右边界不断拓展直到寻找的满足的条件后左边界收缩寻找最优解。

        如何判断满足条件
        每次遍历一个s中的元素就放入s的map容器（也就是窗口的频数）增加该元素的频数 记录窗口下的所有元素的频数
        当某元素同时存在于s和t数组时 判断元素在s中的频数若小于在t中的频数 用变量distant统计窗口内满足条件的元素个数
        当distant值和t的长度相等时说明满足条件 频数相等时distant不增加 意思是distant统计的是窗口中满足了t中元素的个数。

        如何收缩左区间
        在左区间收缩时判断收缩的元素的在s中和t中的频数 s中频数大于等于t中频数时说明窗口中的该元素在t中仍然时满足的
        直到该元素在窗口中的频数小于在t中的频数说明该元素少了 distant减少 移动右窗口

        """
        counter = Counter(t)
        hs = defaultdict(int)
        cnt = 0
        res = ''
        left = 0
        right = 0
        while right < len(s):
            c = s[right]
            hs[c] += 1
            if hs[c] <= counter[c]:
                # 遇到了一个新的字符先加进了hs，所以相等的情况cnt也+1
                cnt += 1
            # 窗口内元素都符合，开始压缩窗口
            while left <= right and hs[s[left]] > counter[s[left]]:
                hs[s[left]] -= 1
                left += 1
            if cnt == len(t):
                if not res or (right-left+ 1) < len(res):
                    res = s[left: right + 1]
            right += 1
        return res


if __name__ == '__main__':
    print(Solution().minWindow(s="abc", t="ab"))
