# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
#  示例 2：
#
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
#
#
#  提示：
#
#
#  链表中节点数目为 n
#  1 <= n <= 500
#  -500 <= Node.val <= 500
#  1 <= left <= right <= n
#
#
#
#
#  进阶： 你可以使用一趟扫描完成反转吗？
#  Related Topics 链表
#  👍 1092 👎 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        整体思想是：在需要反转的区间里，每遍历到一个节点，让这个新节点来到反转部分的起始位置
        使用三个指针变量 pre、curr、next 来记录反转的过程中需要的变量，它们的意义如下：
        curr：指向待反转区域的第一个节点 left；
        next：永远指向 curr 的下一个节点，循环过程中，curr 变化以后 next 会变化；
        pre：永远指向待反转区域的第一个节点 left 的前一个节点，在循环过程中不变

        先将 curr 的下一个节点记录为 next；
        执行操作 ①：把 curr 的下一个节点指向 next 的下一个节点；
        执行操作 ②：把 next 的下一个节点指向 pre 的下一个节点；
        执行操作 ③：把 pre 的下一个节点指向 next
        """
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            _next = cur.next
            cur.next = _next.next
            _next.next = pre.next
            pre.next = _next

        return dummy_node.next