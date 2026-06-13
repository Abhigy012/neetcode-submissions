# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        for i in range(n):
            temp = temp.next
        temp1 = head
        if temp == None:
            return head.next
        while temp and temp.next != None:
            temp1 = temp1.next
            temp = temp.next
        temp1.next = temp1.next.next
        return head


        