# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def heightofTree(root: Optional[TreeNode]) -> int:
    if root == None:
            return 0
    lefth , righth = 0 , 0
    if root.left:
        lefth = heightofTree(root.left)
    if root.right:
        righth = heightofTree(root.right)
    return max(lefth , righth) + 1

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = [root]
        dia = 0
        while len(q):
            currNode = q.pop(0)
            dia = max(dia , heightofTree(currNode.left) + heightofTree(currNode.right))
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        return dia


        