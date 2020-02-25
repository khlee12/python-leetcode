'''
96. Unique Binary Search Trees
Medium
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class Solution:
    def numTrees(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        if n==2:
            return 2
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            temp_sum = 0
            for j in range(i):
                temp_sum += dp[j]*dp[i-j-1]
            dp[i] = temp_sum
        return dp[-1]
