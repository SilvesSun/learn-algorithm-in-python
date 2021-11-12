# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#
#
#
#
#  示例 1：
#
#
# 输入：s = "()"
# 输出：true
#
#
#  示例 2：
#
#
# 输入：s = "()[]{}"
# 输出：true
#
#
#  示例 3：
#
#
# 输入：s = "(]"
# 输出：false
#
#
#  示例 4：
#
#
# 输入：s = "([)]"
# 输出：false
#
#
#  示例 5：
#
#
# 输入：s = "{[]}"
# 输出：true
#
#
#
#  提示：
#
#
#  1 <= s.length <= 104
#  s 仅由括号 '()[]{}' 组成
#
#  Related Topics 栈 字符串
#  👍 2755 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        pair_dic = {
            '(': ')',
            '{': '}',
            '[': ']',
            '?': '?'
        }
        stack = ['?']
        for c in s:
            if c in pair_dic:  # 说明是左括号, 直接入栈
                stack.append(c)
            else:
                # 右括号, 看和是否能形成有效的括号
                if pair_dic[stack.pop()] != c:
                    return False
        return stack == ['?']
# leetcode submit region end(Prohibit modification and deletion)
