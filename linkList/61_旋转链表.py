# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#
#
#  示例 2：
#
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
#
#
#  提示：
#
#
#  链表中节点的数目在范围 [0, 500] 内
#  -100 <= Node.val <= 100
#  0 <= k <= 2 * 10⁹
#
#
#  Related Topics 链表 双指针 👍 1037 👎 0
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self:
            print(f"{self.val}, {self.next=}")

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 首先查看链表的长度
        if k == 0 or not head or not head.next:
            return head
        p = head
        n = 1
        while p.next:
            n += 1
            p = p.next

        # 由于可以看作一个循环, 取余得只需要移动的最小步数
        step = n - k % n

        if step == 0:
            return head
        p.next = head
        while step:
            p = p.next
            step -= 1
        ret = p.next
        p.next = None
        return ret
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # l0 = ListNode(0)
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    # l0.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    ans = Solution().rotateRight(l1, 2)
    # print(ans)
    while ans:
        print(ans.val)
        ans = ans.next