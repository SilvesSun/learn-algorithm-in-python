# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
#
#  你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
#
#
#
#  示例 1：
#
#
# 输入：num1 = "11", num2 = "123"
# 输出："134"
#
#
#  示例 2：
#
#
# 输入：num1 = "456", num2 = "77"
# 输出："533"
#
#
#  示例 3：
#
#
# 输入：num1 = "0", num2 = "0"
# 输出："0"
#
#
#
#
#
#
#  提示：
#
#
#  1 <= num1.length, num2.length <= 104
#  num1 和num2 都只包含数字 0-9
#  num1 和num2 都不包含任何前导零
#
#  Related Topics 数学 字符串 模拟
#  👍 477 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            num1, num2 = num2, num1
        num2 = num2.rjust(len(num1), '0')
        idx = len(num1)-1
        r = 0
        res = ""
        while idx >= 0:
            t = int(num1[idx]) + int(num2[idx]) + r
            r = t // 10
            res = str(t % 10) + res
            idx -= 1
        return "1" + res if r else res


if __name__ == '__main__':
    print(Solution().addStrings(num1="1", num2="9"))
