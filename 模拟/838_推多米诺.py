# n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。
#
#  每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
#
#  如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。
#
#  就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。
#
#  给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：
#
#
#  dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
#  dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
#  dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
#
#
#  返回表示最终状态的字符串。
#
#
#  示例 1：
#
#
# 输入：dominoes = "RR.L"
# 输出："RR.L"
# 解释：第一张多米诺骨牌没有给第二张施加额外的力。
#
#
#  示例 2：
#
#
# 输入：dominoes = ".L.R...LR..L.."
# 输出："LL.RR.LLRRLL.."
#
#
#
#
#  提示：
#
#
#  n == dominoes.length
#  1 <= n <= 10⁵
#  dominoes[i] 为 'L'、'R' 或 '.'
#
#  Related Topics 双指针 字符串 动态规划 👍 212 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        初始的RL一定不会变，需要我们处理的是原始串每两个字母之间的“.”们：
        1、LL之间的全L；
        2、RR之间的全R；
        3、LR不变，RL中间靠；
        4、最左边默认有个L，最右边默认有个R，这样方便处理
        """
        s = list(dominoes)
        n = len(s)
        i = 0
        left = 'L'
        while i < n:
            # 原本不被操作的才会变化, 先找到一段连续的 .
            j = i
            while j < n and s[j] == '.':
                j += 1
            right = s[j] if j < n else 'R'
            if left == right:
                # 方向相同，那么这些竖立骨牌也会倒向同一方向
                while i < j:
                    s[i] = left
                    i += 1
            elif left == 'R' and right == 'L':
                k = j - 1
                while i < k:
                    s[i] = 'R'
                    s[k] = 'L'
                    i += 1
                    k -= 1
            left = right
            i = j + 1

        return ''.join(s)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().pushDominoes(".L.R...LR..L.."))
