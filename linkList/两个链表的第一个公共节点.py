class Solution:
    def get_intersection_node(self, headA, headB):
        if headA is None or headB is None: return None
        p1 = headA
        p2 = headB
        while p1.val != p2.val:
            p1 = p1.next if p1.next else headB
            p2 = p2.next if p2.next else headA
        return p1.val