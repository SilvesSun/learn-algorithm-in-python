# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
#  注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
#
#
#
#  示例 1：
#
#
# 输入：s = "1 + 1"
# 输出：2
#
#
#  示例 2：
#
#
# 输入：s = " 2-1 + 2 "
# 输出：3
#
#
#  示例 3：
#
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 3 * 10⁵
#  s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
#  s 表示一个有效的表达式
#  '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
#  '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
#  输入中不存在两个连续的操作符
#  每个数字和运行的计算将适合于一个有符号的 32位 整数
#
#  Related Topics 栈 递归 数学 字符串 👍 713 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        nums = deque()
        ops = deque()

        #  为了防止第一个数为负数，先往 nums 加个 0
        nums.append(0)
        s = s.replace(' ', '')
        cs = list(s)
        n = len(cs)
        i = 0
        while i < n:
            c = cs[i]
            if c == '(':
                ops.append(c)
            elif c == ')':
                # 使用现有的 nums 和 ops 进行计算，直到遇到左边最近的一个左括号为止，计算结果放到 nums
                while ops:
                    op = ops[-1]
                    if op != '(':
                        self.calc(nums, ops)
                    else:
                        ops.pop()
                        break
            else:
                if c.isdigit():
                    u = 0
                    j = i
                    while j < n and cs[j].isdigit():
                        u = u * 10 + int(cs[j])
                        j += 1
                    i = j - 1
                    nums.append(u)
                else:
                    if i > 0 and (cs[i - 1] == '(' or cs[i - 1] == '+' or cs[i - 1] == '-'):
                        nums.append(0)
                    while ops and ops[-1] != '(':
                        self.calc(nums, ops)
                    ops.append(c)
            i += 1

        while ops:
            self.calc(nums, ops)
        return nums[-1]

    def calc(self, nums, ops):
        if not nums or len(nums) < 2: return
        if not ops: return
        op = ops.pop()
        b = nums.pop()
        a = nums.pop()
        nums.append(a + b if op == '+' else a - b)

    def calculate2(self, s: str) -> int:
        """
        只有加减法，可以把括号全都展开来写，例如 2 - （1 - 3）展开成 2 - 1 + 3
        """
        stack = [1]  # 记录当前符号, 初始为正
        res = 0
        num = 0
        op = 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                continue
            # 计算一个运算符
            res += op * num
            # 重置
            num = 0
            if c == '+':
                op = stack[-1]
            elif c == '-':
                op = -stack[-1]
            elif c == '(':
                stack.append(op)
            elif c == ')':
                stack.pop()
        # 计算最后一个数
        res += op * num
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
