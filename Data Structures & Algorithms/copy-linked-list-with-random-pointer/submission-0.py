
# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head
        mpp = dict()
        dummyNode = Node(-1)
        temp = dummyNode
        curr = head
        while ((curr) and (mpp.get(curr) == None)):
            newNode = Node(curr.val)
            temp.next = newNode
            mpp[curr] = newNode
            curr = curr.next
            temp = temp.next
        for [key,value] in mpp.items():
            value.random = mpp.get(key.random , None)
        return dummyNode.next


        