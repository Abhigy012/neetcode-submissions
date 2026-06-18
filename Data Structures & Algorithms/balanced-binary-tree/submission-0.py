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
        if lefth == -1 or righth == -1:
            return -1
        if max(lefth , righth) - min(lefth, righth) > 1: 
            return -1
        return max(lefth , righth) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        lefth = self.maxDepth(root.left)
        righth = self.maxDepth(root.right)
        if lefth == -1 or righth == -1:
            return False
        if max(lefth , righth) - min(lefth, righth) > 1: 
            return False
        return True
        