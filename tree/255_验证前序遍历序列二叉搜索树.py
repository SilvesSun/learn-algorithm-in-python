# 给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
#
#  你可以假定该序列中的数都是不相同的。
#
#  参考以下这颗二叉搜索树：
#
#       5
#     / \
#    2   6
#   / \
#  1   3
#
#  示例 1：
#
#  输入: [5,2,6,1,3]
# 输出: false
#
#  示例 2：
#
#  输入: [5,2,1,3,6]
# 输出: true
#
#  进阶挑战：
#
#  您能否使用恒定的空间复杂度来完成此题？
#  Related Topics 栈 树 二叉搜索树 递归 二叉树 单调栈
#  👍 127 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
        二叉搜索树的前序遍历有以下特点：
        如果出现递减序列，则是左子树，否则是右子树；
        右子树一定是递增的
        """
        stack = []
        min_n = float('-inf')
        for i in range(len(preorder)):
            if preorder[i] < min_n:
                return False
            while stack and preorder[i] > stack[-1]:
                min_n = stack.pop()
            stack.append(preorder[i])
        return True


if __name__ == '__main__':
    print(Solution().verifyPreorder([5, 2, 6, 1, 3]))
