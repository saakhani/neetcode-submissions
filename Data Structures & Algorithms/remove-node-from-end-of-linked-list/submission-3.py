# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        firstNode = head
        secondNode = head
        prevNode = head
        count = 0
        while count < n:
            firstNode = firstNode.next
            count += 1
        while firstNode:
            firstNode = firstNode.next
            prevNode = secondNode
            secondNode = secondNode.next
        
        if (head == secondNode):
            return head.next
        
        prevNode.next = secondNode.next

        
        return head
        


        