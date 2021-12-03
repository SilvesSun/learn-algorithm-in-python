# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
#  示例 1:
#
#  输入: num1 = "2", num2 = "3"
# 输出: "6"
#
#  示例 2:
#
#  输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
#  说明：
#
#
#  num1 和 num2 的长度小于110。
#  num1 和 num2 只包含数字 0-9。
#  num1 和 num2 均不以零开头，除非是数字 0 本身。
#  不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#  Related Topics 数学 字符串 模拟
#  👍 775 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        m,n分别表示num1 和 num2d的长度, 并且均不为0. 则乘积的长度为 m+n-1或者 m+n
        由于两数相乘的最大长度为 m+n, 创建一个 m+n 的数组存储乘积. 对于任意的 0 <=i<m, 0<=j<n, nums1[i]*nums2[j]的结果位于 ansArr[i+j+1],
        如果ansArr[i+j+1] >=10, 进位加到ansArr[i+j]

        时间复杂度为 O(mn)
        空间复杂度O(m+n)
        """
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)
        ans_arr = [0] * (m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                ans_arr[i+j+1] += int(num1[i]) * int(num2[j])

        for i in range(m+n-1, 0, -1):
            ans_arr[i-1] += ans_arr[i] // 10
            ans_arr[i] %= 10

        index = 1 if ans_arr[0] == 0 else 0
        ans = "".join(str(x) for x in ans_arr[index:])
        return ans