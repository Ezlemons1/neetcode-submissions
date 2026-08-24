# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.check = True
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if abs(leftDepth - rightDepth) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1