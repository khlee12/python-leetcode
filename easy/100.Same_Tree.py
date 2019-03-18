# 100. Same Tree
# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and p==q:
            return True
        if p is None or q is None:
            return False
        
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1.val != node2.val:
                return False
            
            if not node1.right is None and not node2.right is None:
                stack1.append(node1.right)
                stack2.append(node2.right)
            if not node1.left is None and not node2.left is None:
                stack1.append(node1.left)
                stack2.append(node2.left)
            if (not node1.left is None and node2.left is None) or (node1.left is None and not node2.left is None) or (not node1.right is None and node2.right is None) or (node1.right is None and not node2.right is None):
                return False
        
        return True
            
