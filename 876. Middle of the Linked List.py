# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        count = 0
        
        while head:
            count += 1
            head = head.next
        
        for _ in range(count//2):
            pre = pre.next
        
        return pre