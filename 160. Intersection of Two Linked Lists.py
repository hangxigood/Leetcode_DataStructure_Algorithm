# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode):
#         tempB = headB
#         while headA:
#             while headB:
#                 if headA == headB:
#                     return headA
#                 else:
#                     headB = headB.next
#             headA = headA.next
#             headB = tempB
#         return None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # pa先遍历headA，然后再遍历headB
            # pb先遍历headB，然后再遍历headA
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # 只有两种方式结束循环，一种是pa和pb所指相同，另一种是headA和headB都已经遍历完仍然没有找到。

# test
intersection_node = ListNode(8)

# Creating the first linked list: 4 -> 1 -> 8 (intersection node)
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = intersection_node

# Creating the second linked list: 5 -> 6 -> 1 -> 8 (intersection node)
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = intersection_node

print(Solution().getIntersectionNode(headA, headB).val)