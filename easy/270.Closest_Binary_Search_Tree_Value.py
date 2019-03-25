# 270. Closest Binary Search Tree Value
# https://leetcode.com/problems/closest-binary-search-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stacks = [root]
        _min = sys.maxsize
        output = None
        while stacks:
            node = stacks.pop()
            if node.val < target:
                if _min != min(_min, abs(node.val-target)):
                    output = node.val
                    _min = min(_min, abs(node.val-target))
                if node.right:
                    stacks.append(node.right)
            elif node.val > target:
                if _min != min(_min, abs(node.val-target)):
                    output = node.val
                    _min = min(_min, abs(node.val-target))
                if node.left:
                    stacks.append(node.left)
            else:
                return node.val
        return output
            
