# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
#
#  示例 1 :
#
#
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
#
#
#  示例 2 :
#
#
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
#
#
#  注意:
#
#
#  给定数字的范围是 [0, 10⁸]
#
#  Related Topics 贪心 数学 👍 214 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        将数组转为字符串数组方便遍历每一个数字
        从后往前遍历，避免1993交换后出现9193而不是9913
        用一个数组记录从后往前的每一个数对应的最大值的索引比如1993，从3开始遍历，最大值是3，3的索引是3，遍历到1时，在已经遍历过的元素中最大是9，所以maxArr[0]是9的索引2，最后maxArr =[2,2,2,3]
        再从头遍历原数组，比如chars[0] = 1,和他应该对应的最大值chars[maxArr[0]] = chars[2] = 9不相等 则交换
        再举个例子98368，maxArr = [0,4,4,4,4],chars[0] = chars[maxArr[0]] = 9 跳过
        chars[1] = 8, chars[maxArr[1]] = chars[4] = 8 相等 继续跳过
        chars[2] = 3, chars[maxArr[3]] = chars[4] = 8 不相等，交换
        只要交换完成则跳出循环
        """
        ns = list(str(num))
        n = len(ns)

        cur_max = n - 1
        right_max_idx = [0] * n

        # 找到每个位置右边最大的值
        for i in range(n - 1, -1, -1):
            if ns[i] > ns[cur_max]:
                cur_max = i
            right_max_idx[i] = cur_max

        for i in range(n):
            right_max = right_max_idx[i]
            if ns[i] != ns[right_max]:
                # 需要交换
                ns[i], ns[right_max] = ns[right_max], ns[i]
                break
        return int(''.join(ns))


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().maximumSwap(2736))
