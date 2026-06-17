# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [[root,1]]
        maxi = 0
        while len(q):
            [node , currD] = q.pop(0)
            maxi = max(maxi, currD)
            if node.left:
                q.append([node.left , currD+1])
            if node.right:
                q.append([node.right , currD+1])
        return maxi
        