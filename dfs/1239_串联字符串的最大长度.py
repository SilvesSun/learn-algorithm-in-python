# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
#
#  请返回所有可行解 s 中最长长度。
#
#
#
#  示例 1：
#
#  输入：arr = ["un","iq","ue"]
# 输出：4
# 解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
#
#
#  示例 2：
#
#  输入：arr = ["cha","r","act","ers"]
# 输出：6
# 解释：可能的解答有 "chaers" 和 "acters"。
#
#
#  示例 3：
#
#  输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
# 输出：26
#
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 16
#  1 <= arr[i].length <= 26
#  arr[i] 中只含有小写英文字母
#
#  Related Topics 位运算 数组 字符串 回溯 👍 194 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxLength(self, arr):
        result = 0
        temp = []

        # 检查是否满足字符唯一的条件
        def can_add(current, temp):
            concat_str = ''.join(temp)
            for c in current:
                if c in concat_str:
                    return False
            return True

        # 检查字符串本身有没有重复的字符
        def is_distinct(current):
            return len(set(current)) == len(current)

        def backtrace(start, temp, arr):

            nonlocal result
            result = max(result, len(''.join(temp)))

            for i in range(start, len(arr)):

                # 这里可以控制谁要加进来, 谁可以继续回溯和pop
                if can_add(arr[i], temp) and is_distinct(arr[i]):
                    temp.append(arr[i])
                    backtrace(i + 1, temp, arr)
                    temp.pop()

        backtrace(0, temp, arr)

        return result


if __name__ == '__main__':
    print(Solution().maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))
