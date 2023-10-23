# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         add_list = []
#         while head:
#             if head in add_list:
#                 return True
#             else:
#                 add_list.append(head)
#                 head = head.next
#         return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not (head and head.next):
            return False
        
        slower = head
        faster = head.next

        while slower != faster:
            if faster and faster.next:
                slower = slower.next
                faster = faster.next.next
            else:
                return False
        return True