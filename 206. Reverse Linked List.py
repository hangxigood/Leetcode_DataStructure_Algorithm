
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# list 

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
    
# recursion

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursion(head, None)
        
    def recursion(self, head, pre):
        if not head:
            return pre
        else:
            next_node = head.next
            head.next = pre
            return self.recursion(next_node, head)
        
        