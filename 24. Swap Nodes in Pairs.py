# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        self.swap(head)
        return pre
    
    def swap(self, head):
        if not head or not head.next:
            pass
        else:
            head.val, head.next.val = head.next.val, head.val
            self.swap(head.next.next)
        