# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

# intuition: instead of brute forcing this question, finding the height of the left and right subtree for every node and determining if the tree is valid every time by doing abs(left - right) < 1, instead utilize a dfs function that returns two items in a list: a boolean and an integer. the boolean represents if the tree is valid and the integer represents the difference in the height between the left and right subtree. do an AND boolean operation using the boolean from recursive call from the left and right subtree, as well as the height difference check betweeen the two subtree heights. the function will return True only when the tree has been balanced through each of the subtrees, and if the difference is less than or equal to 1. return the first element as that is the boolean that will have kept updating throughout the tree.