# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
#
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
#  请将其重新排列后变为：
#
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例 1：
#
#
#
#
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
#
#  示例 2：
#
#
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
#
#
#
#  提示：
#
#
#  链表的长度范围为 [1, 5 * 10⁴]
#  1 <= node.val <= 1000
#
#  Related Topics 栈 递归 链表 双指针 👍 764 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 首先找到链表的中间节点
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 翻转从中间节点后的链表
        mid = slow
        # print(f"slow: {slow}")
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)

        # 合并
        # print(f"start merge\n-{l1},\n-{l2}")
        while l1 and l2:
            l1_t = l1.next
            l2_t = l2.next
            l1.next = l2
            l1 = l1_t

            l2.next = l1
            l2 = l2_t

    def reverseList(self, head):
        if not head:
            return None
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
# leetcode submit region end(Prohibit modification and deletion)
