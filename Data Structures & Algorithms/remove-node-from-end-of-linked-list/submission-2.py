# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currentNode = head
        length = 0
        while currentNode:
            currentNode = currentNode.next
            length += 1
        currentNode = head
        prevNode = head
        for i in range(0, length - n):
            prevNode = currentNode
            currentNode = currentNode.next
        
        nodeToDel = currentNode
        if (head == nodeToDel):
            return head.next
        
        prevNode.next = currentNode.next

        
        return head
        


        