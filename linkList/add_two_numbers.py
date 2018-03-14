class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        mul = 1
        r1, r2 = 0, 0

        while l1:
            r1 += l1.val * mul
            l1 = l1.next
            mul *= 10
        mul = 1
        while l2:
            r2 += l2.val * mul
            l2 = l2.next
            mul *= 10

        # 加和后转换成字符串，转置后再把每个元素还原成int
        r = list(map(int, str(r1 + r2)))[::-1]

        # 生成结果的链表，将列表的第一个值赋值给链表
        res = ListNode(r[0])

        # 因为要返回链表的头部，所以我们定义一个temp变量去用来循环生成链表
        temp = res
        for i in r[1::]:
            te = ListNode(i)
            temp.next = te
            temp = te
        return res


