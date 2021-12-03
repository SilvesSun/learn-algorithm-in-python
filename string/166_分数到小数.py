# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
#
#  如果小数部分为循环小数，则将循环的部分括在括号内。
#
#  如果存在多个答案，只需返回 任意一个 。
#
#  对于所有给定的输入，保证 答案字符串的长度小于 104 。
#
#
#
#  示例 1：
#
#
# 输入：numerator = 1, denominator = 2
# 输出："0.5"
#
#
#  示例 2：
#
#
# 输入：numerator = 2, denominator = 1
# 输出："2"
#
#
#  示例 3：
#
#
# 输入：numerator = 2, denominator = 3
# 输出："0.(6)"
#
#
#  示例 4：
#
#
# 输入：numerator = 4, denominator = 333
# 输出："0.(012)"
#
#
#  示例 5：
#
#
# 输入：numerator = 1, denominator = 5
# 输出："0.2"
#
#
#
#
#  提示：
#
#
#  -231 <= numerator, denominator <= 231 - 1
#  denominator != 0
#
#  Related Topics 哈希表 数学 字符串
#  👍 341 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 整数部分
        if numerator % denominator == 0:
            return str(numerator // denominator)
        res = []
        if (numerator < 0) != (denominator < 0):
            res.append('-')

        # 全部转为正数
        numerator = abs(numerator)
        denominator = abs(denominator)

        # 整数部分
        res.append(str(numerator // denominator))
        res.append('.')

        # 小数部分
        d = {}
        remain = numerator % denominator
        while remain and remain not in d:
            d[remain] = len(res)
            remain *= 10
            res.append(str(remain // denominator))
            remain %= denominator
        # 存在循环
        if remain:
            insert_idx = d[remain]
            res.insert(insert_idx, '(')
            res.append(')')
        return ''.join(res)
