# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
               5
           4       8
         11       13 4
        7  2
            1
        
        '''
        def dfs(root):
            nonlocal max_gain
            #inorder
            if not root:
                return 0
            
            left_gain = max(dfs(root.left), 0) # 如果path里面存在负数， 不加到path里
            right_gain = max(dfs(root.right), 0) # 即， 只将整数放入到path里
            max_gain = max(max_gain, left_gain+right_gain+root.val)
            # print(max_gain)
            return max(left_gain,right_gain)+root.val # 当前node能get的最大sum
        
        max_gain = -sys.maxsize
        dfs(root)
        return max_gain
