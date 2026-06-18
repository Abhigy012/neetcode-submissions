# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        lefth , righth = 0 , 0
        if root.left:
            lefth = self.maxDepth(root.left)
        if root.right:
            righth = self.maxDepth(root.right)
        return max(lefth , righth) + 1
        