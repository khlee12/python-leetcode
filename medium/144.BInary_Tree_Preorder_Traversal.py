# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # preorder: 
        #   print TreeNode.val
        #   print TreeNode.left
        #   print TreeNode.right
        if root is None:
            return []
        
        stack, output = [root], []
        while stack:
            curr = stack.pop()
            output.append(curr.val)
            if not curr.right is None:
                stack.append(curr.right)
            if not curr.left is None:
                stack.append(curr.left)
                
        return output
