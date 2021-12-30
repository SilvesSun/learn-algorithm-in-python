# 给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。
#
#  返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。
#
#
#
#  示例 1：
#
#
# 输入：s = "banana"
# 输出："ana"
#
#
#  示例 2：
#
#
# 输入：s = "abcd"
# 输出：""
#
#
#
#
#  提示：
#
#
#  2 <= s.length <= 3 * 104
#  s 由小写英文字母组成
#
#  Related Topics 字符串 二分查找 后缀数组 滑动窗口 哈希函数 滚动哈希
#  👍 191 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
        Rabin-Karp的预处理时间是O(m)，匹配时间O( ( n - m + 1 ) m )
        """
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        a = 26
        mod = 2 ** 64 - 1
        left, right = 1, n
        length = 0
        start = 0
        while left < right:
            m = left + (right - left) // 2
            idx = self.check(nums, n, mod, a, m)
            # 说明存在
            if idx != -1:
                left = m + 1
                length = m
                start = idx
            else:
                right = m
        return s[start: start + length] if start != -1 else ""

    def check(self, nums, n, mod, a, m):
        h = 0
        for i in range(m):
            h = (h * a + nums[i]) % mod
        # already seen hashes of strings of length L
        seen = {h}
        al = pow(a, m, mod)
        for start in range(1, n - m + 1):
            h = (h * a - nums[start - 1] * al + nums[start + m - 1]) % mod
            if h in seen:
                return start
            seen.add(h)
        return -1

        # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().longestDupSubstring(s="banana"))
