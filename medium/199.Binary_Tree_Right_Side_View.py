# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # print right most element in every level
        if root is None:
            return []
        
        stack, output = [root], []
        while stack:
            output.append(stack[-1].val)
            level_len = len(stack)
            for i in range(level_len):
                node = stack.pop(0)    
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return output
        
