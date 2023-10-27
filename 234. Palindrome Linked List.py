# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_list = []
        pre = head

        while head:
            node_list.append(head)
            head = head.next

        while node_list:
            if node_list.pop().val == pre.val:
                pre = pre.next
            else:
                return False
            
        return True