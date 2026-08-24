# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # intuition: the diameter would be the depth of the left subtree plus the depth of the right subtree. we get the leftdepth and rightdepth of each node using the maxdepth function from last exercise, which finds the maximum depth of a node. then, we get the diameter simply by adding them together. we recursively call the function on the left and right subtree from the current node to iterative pass through the tree and find the greatest diameter. the largest diameter going down each direction is passed up, and the current diameter of the node plus the largest diameter from the two trees is returned.
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        diameter = leftDepth + rightDepth
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)
        
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1