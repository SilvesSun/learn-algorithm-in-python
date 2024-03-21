# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
#
#
#
#  示例 1：
#
#
# 输入:a = "11", b = "1"
# 输出："100"
#
#  示例 2：
#
#
# 输入：a = "1010", b = "1011"
# 输出："10101"
#
#
#
#  提示：
#
#
#  1 <= a.length, b.length <= 10⁴
#  a 和 b 仅由字符 '0' 或 '1' 组成
#  字符串如果不是 "0" ，就不含前导零
#
#
#  Related Topics 位运算 数学 字符串 模拟 👍 1177 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)
        add = 0
        ans = ''
        while n1 or n2:
            num1 = int(a[n1-1]) if n1 else 0
            num2 = int(b[n2 - 1]) if n2 else 0
            t = num1 + num2 + add
            if t == 0:
                ans = "0" + ans
                add = 0
            if t == 1:
                ans = '1' + ans
                add = 0
            if t == 2:
                ans = '0' + ans
                add = 1
            if t == 3:
                ans = '1' + ans
                add = 1
            if n1: n1 -= 1
            if n2: n2 -= 1
        if add:
            return '1' + ans
        return ans
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().addBinary(a = "100", b = "110010"))
