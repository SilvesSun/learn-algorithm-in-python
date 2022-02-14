# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
#  你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
#
#
#  示例1：
#
#
#
#
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
#
#
#  示例2：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
#
#
#  示例3：
#
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
#
#
#  提示：
#
#
#  链表的长度范围为 [1, 100]
#  0 <= node.val <= 9
#  输入数据保证链表代表的数字无前导 0
#
#
#
#
#  进阶：如果输入链表不能翻转该如何解决？
#  Related Topics 栈 链表 数学 👍 480 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r1 = 0
        mul = 10
        while l1:
            r1 = r1 * mul + l1.val
            l1 = l1.next
        r2 = 0
        mul = 10
        while l2:
            r2 = r2 * mul + l2.val
            l2 = l2.next
        sum_r = list(map(int, str(r1 + r2)))

        res = ListNode(sum_r[0])
        t = res
        for i in sum_r[1:]:
            tn = ListNode(i)
            t.next = tn
            t = tn
        return res
    # leetcode submit region end(Prohibit modification and deletion)
