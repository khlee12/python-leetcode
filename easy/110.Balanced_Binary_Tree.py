# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)
            if abs(left-right) > 1:
                self.flag = True
            return 1+max(left, right)
        
        
        if root is None:
            return True
        
        self.flag = False
        
        height(root)
        
        return not self.flag
