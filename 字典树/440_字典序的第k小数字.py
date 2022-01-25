# 给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。
#
#  注意：1 ≤ k ≤ n ≤ 10⁹。
#
#  示例 :
#
#
# 输入:
# n: 13   k: 2
#
# 输出:
# 10
#
# 解释:
# 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
#
#  Related Topics 字典树 👍 261 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1  # 去掉第一个0节点
        while k:
            num = self.cal_steps(n, cur, cur + 1)
            # 第k个数不在以cur为根节点的树上, cur在字典序数组中从左往右移动
            if num <= k:
                cur += 1
                k -= num
            #  在子树中, cur在字典序数组中从上往下移动
            else:
                cur *= 10
                k -= 1
        return cur

    def cal_steps(self, n, first, last):
        num = 0
        while first <= n:
            num += min(n + 1, last) - first
            first *= 10
            last *= 10
        return num


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().findKthNumber(13, 2))
