# 如果字符串 s 中 不存在 两个不同字符 频次 相同的情况，就称 s 是 优质字符串 。
#
#  给你一个字符串 s，返回使 s 成为 优质字符串 需要删除的 最小 字符数。
#
#  字符串中字符的 频次 是该字符在字符串中的出现次数。例如，在字符串 "aab" 中，'a' 的频次是 2，而 'b' 的频次是 1 。
#
#
#
#  示例 1：
#
#
# 输入：s = "aab"
# 输出：0
# 解释：s 已经是优质字符串。
#
#
#  示例 2：
#
#
# 输入：s = "aaabbbcc"
# 输出：2
# 解释：可以删除两个 'b' , 得到优质字符串 "aaabcc" 。
# 另一种方式是删除一个 'b' 和一个 'c' ，得到优质字符串 "aaabbc" 。
#
#  示例 3：
#
#
# 输入：s = "ceabaacb"
# 输出：2
# 解释：可以删除两个 'c' 得到优质字符串 "eabaab" 。
# 注意，只需要关注结果字符串中仍然存在的字符。（即，频次为 0 的字符会忽略不计。）
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10⁵
#  s 仅含小写英文字母
#
#  Related Topics 贪心 字符串 排序 👍 38 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        if len(s) == 1:
            return 0
        cnt_d = Counter(s)
        sort_cnt = sorted(cnt_d.values(), reverse=True)
        n = len(sort_cnt)
        i = 1
        total = 0
        while i < n:
            # 前一个数的频次为0, 后续的直接删除
            if sort_cnt[i - 1] == 0:
                total += sort_cnt[i]
                sort_cnt[i] = 0
            elif sort_cnt[i] > sort_cnt[i - 1] - 1:
                # 需要删除的个数为 sort_cnt[i] - (sort_cnt[i-1] - 1) 个数
                total += sort_cnt[i] - (sort_cnt[i - 1] - 1)
                sort_cnt[i] = sort_cnt[i - 1] - 1
            i += 1
        return total


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().minDeletions("aaabbbcc"))
