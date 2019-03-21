# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stacks, output = [root], []
        while stacks:
            node = stacks.pop()
            output.append(node.val)
            if node.left:
                stacks.append(node.left)
            if node.right:
                stacks.append(node.right)
        return output[::-1]
            
    
