
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head:[ListNode]) -> [ListNode]:
        if not head:
            return None

        List = []

        while head:
            List.append(head)
            head = head.next
        List.reverse()
        head = ListNode(0)
        current = head
        
        for i in List:
            current.next = ListNode(i.val) # if I assign node directly from the list, all node will share same memory addresses, leading unexpected behavior.
            current = current.next
        
        return head.next
    
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)

# print(Solution().reverseList(head))