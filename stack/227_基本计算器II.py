# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
#  整数除法仅保留整数部分。
#
#
#
#
#
#  示例 1：
#
#
# 输入：s = "3+2*2"
# 输出：7
#
#
#  示例 2：
#
#
# 输入：s = " 3/2 "
# 输出：1
#
#
#  示例 3：
#
#
# 输入：s = " 3+5 / 2 "
# 输出：5
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 3 * 10⁵
#  s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
#  s 表示一个 有效表达式
#  表达式中的所有整数都是非负整数，且在范围 [0, 2³¹ - 1] 内
#  题目数据保证答案是一个 32-bit 整数
#
#
#
#  Related Topics 栈 数学 字符串 👍 534 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        """
        双栈解决通用表达式
        nums 存放所有的数字, ops存放所有的操作, map存放操作的优先级

        遍历字符串, 分几种情况
        1. (, 加入ops
        2. ), 使用现有的nums 和 ops计算, 直到遇到最近的左括号为止, 计算结果放到nums
        3. 数字, 从当前位置一直取, 将连续的数字整体取出, 加入nums
        4. + - * / ^ %, 操作放入ops, 存入之前将优先级比当前运算符优先级高/同等的先算完, 使用现有的 nums 和 ops 计算, 直到没有操作或者遇到左括号, 计算结果放入nums
        """
        nums = []
        ops = []
        s = s.replace(' ', '')
        s = '(' + s + ')'
        op_map = {
            '+': 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "%": 2,
            "^": 3
        }
        i = 0
        cs = list(s)
        n = len(cs)
        while i < n:
            c = cs[i]
            if c == '(':
                ops.append(c)
            elif c == ')':
                # 计算到最近的左括号
                while ops:
                    if ops[-1] != '(':
                        self.calc(nums, ops)
                    else:
                        ops.pop()
                        break
            else:
                if c.isdigit():
                    u = 0
                    j = i
                    while j < n and cs[j].isdigit():
                        u = u * 10 + ord(cs[j]) - ord('0')
                        j += 1
                    i = j - 1
                    nums.append(u)
                else:
                    if i and (cs[i-1] == '(' or cs[i-1] == '+' or cs[i-1] == '-'):
                        nums.append(0)
                    while ops and ops[-1] != '(':
                        # 看前一个操作符的优先级
                        prev = ops[-1]
                        if op_map.get(prev) >= op_map.get(c):
                            self.calc(nums, ops)
                        else:
                            break
                    ops.append(c)
            i += 1
        return nums[-1]

    def calc(self, nums, ops):
        print(nums, ops)
        if not nums or len(nums) < 2: return
        if not ops: return
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        ans = 0
        if op == '+':
            ans = a + b
        elif op == '-':
            ans = a - b
        elif op == '*':
            ans = a * b
        elif op == '/':
            ans = a / b
        elif op == '^':
            ans = a ** b
        elif op == '%':
            ans = a % b
        nums.append(int(ans))
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().calculate(" 3+5 / 2 "))